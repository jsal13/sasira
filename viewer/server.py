#!/usr/bin/env python3
"""
Sasiran Markdown Viewer - Flask Server with Hot Reload
Serves markdown files as HTML with navigation
"""

import urllib.parse
from pathlib import Path
import html

try:
    import markdown
except ImportError:
    print("Installing markdown package...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

try:
    from flask import Flask, send_file, jsonify, abort
except ImportError:
    print("Installing Flask...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    from flask import Flask, send_file, jsonify, abort

app = Flask(__name__, static_folder=".")

# Cache the base path to avoid repeated Path operations
BASE_PATH = Path(__file__).parent.parent


def convert_sources_to_table(md_content):
    """Convert sources markdown to table format with Sasiran and Notes columns"""

    # First convert non-text sections normally
    lines = md_content.split("\n")

    # Find where the ## Texts section starts
    texts_start = -1
    for i, line in enumerate(lines):
        if line.strip() == "## Texts":
            texts_start = i
            break

    if texts_start == -1:
        # No Texts section found, process normally
        return markdown.markdown(md_content, extensions=["tables", "codehilite"])

    # Process header content normally
    header_content = "\n".join(lines[: texts_start + 1])
    header_html = markdown.markdown(header_content, extensions=["tables", "codehilite"])

    # Parse text entries
    text_entries = []
    current_entry = {}

    for line in lines[texts_start + 1 :]:
        line = line.strip()
        if line.startswith("### "):
            # Start new entry
            if current_entry:
                text_entries.append(current_entry)
            current_entry = {"title": line[4:]}  # Remove ### prefix
        elif line.startswith("**Sasiran:** "):
            current_entry["sasiran"] = line[13:]  # Remove **Sasiran:** prefix
        elif line.startswith("**Notes:** "):
            current_entry["notes"] = line[11:]  # Remove **Notes:** prefix

    # Add last entry
    if current_entry:
        text_entries.append(current_entry)

    # Create table HTML
    table_html = """
<table class="sources-table">
    <thead>
        <tr>
            <th>Sasiran</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
"""

    for entry in text_entries:
        sasiran_text = html.escape(entry.get("sasiran", ""))
        notes_text = html.escape(entry.get("notes", ""))
        table_html += f"""        <tr>
            <td class="sasiran-text">{sasiran_text}</td>
            <td>{notes_text}</td>
        </tr>
"""

    table_html += """    </tbody>
</table>"""

    return header_html + table_html


def scan_markdown_files(base_path):
    """Scan for markdown files and return structured data"""
    files = {}

    for item in base_path.iterdir():
        if item.name in [".git", "__pycache__", "viewer", "game"]:
            continue

        if item.is_dir():
            # Scan directory for markdown files
            dir_files = {}
            for md_file in item.glob("**/*.md"):
                rel_path = md_file.relative_to(item)
                title = extract_title(md_file)
                dir_files[str(rel_path)] = {
                    "title": title,
                    "path": str(md_file.relative_to(base_path)),
                }

            if dir_files:  # Only include directories with markdown files
                files[item.name] = dir_files

        elif item.suffix == ".md":
            # Individual markdown file
            title = extract_title(item)
            files[item.name] = {
                "title": title,
                "path": str(item.relative_to(base_path)),
            }

    return files


def extract_title(file_path):
    """Extract title from markdown file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            # Only read first few lines to find title, more efficient
            for _ in range(20):  # Check first 20 lines max
                line = f.readline()
                if not line:  # End of file
                    break
                if line.strip().startswith("# "):
                    return line.strip()[2:].strip()
            return file_path.stem
    except Exception:
        return file_path.stem


@app.route("/")
@app.route("/index.html")
def serve_index():
    """Serve the index.html file"""
    try:
        index_path = Path(__file__).parent / "index.html"
        return send_file(index_path)
    except Exception as e:
        abort(500, description=f"Error serving index: {str(e)}")


@app.route("/api/files")
def serve_files_api():
    """Serve the file structure as JSON"""
    files = scan_markdown_files(BASE_PATH)
    return jsonify(files)


@app.route("/view/<path:file_path>")
def serve_markdown_file(file_path):
    """Serve a markdown file as HTML"""
    try:
        # Decode URL encoding
        file_path = urllib.parse.unquote(file_path)

        # Construct full path
        full_path = BASE_PATH / file_path

        # Security check - ensure file is within base directory
        if not str(full_path.resolve()).startswith(str(BASE_PATH.resolve())):
            abort(403, description="Access denied")

        if not full_path.is_file():
            abort(404, description="File not found")

        # Read and convert markdown
        with open(full_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Check if this is a sources file and apply special table formatting
        if file_path.startswith("sources/"):
            html_content = convert_sources_to_table(md_content)
        else:
            # Convert to HTML normally
            html_content = markdown.markdown(
                md_content, extensions=["tables", "codehilite"]
            )

            # Add HTML line breaks before any "Notes:" sections (handle various formats)
            html_content = html_content.replace(
                "<strong>Notes:</strong>", "<br/><strong>Notes:</strong>"
            )
            html_content = html_content.replace(
                "<em><strong>Notes:</strong></em>",
                "<br/><em><strong>Notes:</strong></em>",
            )

        return html_content

    except Exception as e:
        abort(500, description=f"Server error: {str(e)}")


def run_viewer(port=8001, debug=True):
    """Run the Flask markdown viewer server"""
    print("📚 Sasiran Markdown Viewer starting...")
    print(f"📍 Server running at: http://localhost:{port}")
    print("🔍 Browse all markdown files in your project")
    print("🔄 Hot reload enabled - files will auto-refresh")
    print("⏹️  Press Ctrl+C to stop the server")

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    run_viewer(port)

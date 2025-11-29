#!/usr/bin/env python3
"""
Sasiran Markdown Viewer - Simple Local Server
Serves markdown files as HTML with navigation
"""

import http.server
import socketserver
import os
import json
import urllib.parse
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Installing markdown package...")
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown


class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        if path == "/" or path == "/index.html":
            self.serve_index()
        elif path == "/api/files":
            self.serve_files_api()
        elif path.startswith("/view/"):
            file_path = path[6:]  # Remove '/view/' prefix
            self.serve_markdown_file(file_path)
        else:
            super().do_GET()

    def serve_index(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sasiran Markdown Viewer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Georgia', 'Times New Roman', serif;
            line-height: 1.6;
            color: #2F1B14;
            background-color: #FAF0E6;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(139, 69, 19, 0.2);
            overflow: hidden;
        }
        
        header {
            background: #8B4513;
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        header h1 {
            font-size: 2rem;
            margin-bottom: 10px;
        }
        
        .subtitle {
            font-style: italic;
            opacity: 0.9;
        }
        
        .content {
            display: flex;
        }
        
        .sidebar {
            width: 300px;
            background: #F5F5DC;
            padding: 20px;
            border-right: 1px solid #DEB887;
            max-height: 80vh;
            overflow-y: auto;
        }
        
        .main-content {
            flex: 1;
            padding: 30px;
            max-height: 80vh;
            overflow-y: auto;
        }
        
        .folder {
            margin-bottom: 15px;
        }
        
        .folder-title {
            font-weight: bold;
            color: #8B4513;
            margin-bottom: 8px;
            padding: 8px;
            background: #DEB887;
            border-radius: 4px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .folder-content {
            margin-left: 15px;
            display: none;
        }
        
        .folder.open .folder-content {
            display: block;
        }
        
        .folder-toggle {
            font-size: 0.8rem;
            transition: transform 0.3s;
        }
        
        .folder.open .folder-toggle {
            transform: rotate(90deg);
        }
        
        .file-link {
            display: block;
            padding: 8px 12px;
            margin: 2px 0;
            background: white;
            border: 1px solid #DEB887;
            border-radius: 4px;
            text-decoration: none;
            color: #2F1B14;
            transition: background-color 0.3s;
        }
        
        .file-link:hover {
            background: #D2B48C;
            color: white;
        }
        
        .file-link.active {
            background: #8B4513;
            color: white;
        }
        
        .welcome-message {
            text-align: center;
            padding: 60px 20px;
            color: #8B4513;
        }
        
        .welcome-message h2 {
            margin-bottom: 20px;
        }
        
        .welcome-message p {
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.8;
        }
        
        /* Markdown content styling */
        .markdown-content h1 { color: #8B4513; margin-bottom: 20px; }
        .markdown-content h2 { color: #CD853F; margin: 25px 0 15px 0; }
        .markdown-content h3 { color: #D2B48C; margin: 20px 0 10px 0; }
        .markdown-content h4 { color: #8B4513; margin: 15px 0 8px 0; }
        .markdown-content p { margin-bottom: 15px; }
        .markdown-content ul, .markdown-content ol { margin: 15px 0; padding-left: 30px; }
        .markdown-content li { margin-bottom: 8px; }
        .markdown-content blockquote { 
            border-left: 4px solid #8B4513; 
            padding-left: 15px; 
            margin: 20px 0; 
            color: #555; 
            font-style: italic;
        }
        .markdown-content code {
            background: #F5F5DC;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        .markdown-content pre {
            background: #F5F5DC;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 20px 0;
        }
        .markdown-content table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        .markdown-content th, .markdown-content td {
            border: 1px solid #DEB887;
            padding: 12px;
            text-align: left;
        }
        .markdown-content th {
            background: #8B4513;
            color: white;
        }
        .markdown-content tr:nth-child(even) {
            background: #FAF0E6;
        }
        
        @media (max-width: 768px) {
            .content {
                flex-direction: column;
            }
            .sidebar {
                width: 100%;
                max-height: 300px;
            }
            .main-content {
                max-height: 60vh;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 Sasiran Markdown Viewer</h1>
            <p class="subtitle">Browse and view all project documentation</p>
        </header>
        
        <div class="content">
            <nav class="sidebar" id="sidebar">
                <div id="file-tree">
                    Loading files...
                </div>
            </nav>
            
            <main class="main-content" id="main-content">
                <div class="welcome-message">
                    <h2>Welcome to the Sasiran Project Viewer</h2>
                    <p>Select a file from the sidebar to view its contents. This viewer displays all markdown files in the project, including sources, solutions, and reference materials.</p>
                </div>
            </main>
        </div>
    </div>
    
    <script>
        class MarkdownViewer {
            constructor() {
                this.files = {};
                this.currentFile = null;
                this.init();
            }
            
            async init() {
                await this.loadFiles();
                this.renderFileTree();
            }
            
            async loadFiles() {
                try {
                    const response = await fetch('/api/files');
                    this.files = await response.json();
                } catch (error) {
                    console.error('Error loading files:', error);
                    document.getElementById('file-tree').innerHTML = 'Error loading files.';
                }
            }
            
            renderFileTree() {
                const tree = document.getElementById('file-tree');
                tree.innerHTML = '';
                
                // Sort folders and files
                const sortedKeys = Object.keys(this.files).sort();
                
                sortedKeys.forEach(key => {
                    const item = this.files[key];
                    
                    if (typeof item === 'object' && !item.title) {
                        // It's a folder
                        this.renderFolder(tree, key, item);
                    } else {
                        // It's a file
                        this.renderFile(tree, key, item);
                    }
                });
            }
            
            renderFolder(parent, folderName, folderContent) {
                const folderDiv = document.createElement('div');
                folderDiv.className = 'folder';
                
                const folderTitle = document.createElement('div');
                folderTitle.className = 'folder-title';
                folderTitle.innerHTML = `<span class="folder-toggle">▶</span> 📁 ${folderName}`;
                folderTitle.addEventListener('click', () => {
                    folderDiv.classList.toggle('open');
                });
                
                const folderContentDiv = document.createElement('div');
                folderContentDiv.className = 'folder-content';
                
                Object.keys(folderContent).sort().forEach(fileName => {
                    this.renderFile(folderContentDiv, fileName, folderContent[fileName], `${folderName}/${fileName}`);
                });
                
                folderDiv.appendChild(folderTitle);
                folderDiv.appendChild(folderContentDiv);
                parent.appendChild(folderDiv);
            }
            
            renderFile(parent, fileName, fileData, fullPath = null) {
                const link = document.createElement('a');
                link.className = 'file-link';
                link.href = '#';
                link.textContent = `📄 ${fileData.title || fileName}`;
                
                const path = fullPath || fileName;
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.loadFile(path);
                    
                    // Update active state
                    document.querySelectorAll('.file-link').forEach(l => l.classList.remove('active'));
                    link.classList.add('active');
                });
                
                parent.appendChild(link);
            }
            
            async loadFile(path) {
                try {
                    const response = await fetch(`/view/${encodeURIComponent(path)}`);
                    const html = await response.text();
                    
                    const mainContent = document.getElementById('main-content');
                    mainContent.innerHTML = `<div class="markdown-content">${html}</div>`;
                    
                    this.currentFile = path;
                    
                } catch (error) {
                    console.error('Error loading file:', error);
                    document.getElementById('main-content').innerHTML = '<p>Error loading file.</p>';
                }
            }
        }
        
        // Initialize when page loads
        new MarkdownViewer();
    </script>
</body>
</html>"""

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def serve_files_api(self):
        """Serve the file structure as JSON"""
        base_path = Path(
            __file__
        ).parent.parent  # Go up one level from viewer to sasira
        files = self.scan_markdown_files(base_path)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(files, indent=2).encode())

    def scan_markdown_files(self, base_path):
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
                    title = self.extract_title(md_file)
                    dir_files[str(rel_path)] = {
                        "title": title,
                        "path": str(md_file.relative_to(base_path)),
                    }

                if dir_files:  # Only include directories with markdown files
                    files[item.name] = dir_files

            elif item.suffix == ".md":
                # Individual markdown file
                title = self.extract_title(item)
                files[item.name] = {
                    "title": title,
                    "path": str(item.relative_to(base_path)),
                }

        return files

    def extract_title(self, file_path):
        """Extract title from markdown file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Look for first # heading
                for line in content.split("\n"):
                    if line.strip().startswith("# "):
                        return line.strip()[2:].strip()
                return file_path.stem
        except Exception:
            return file_path.stem

    def serve_markdown_file(self, file_path):
        """Serve a markdown file as HTML"""
        try:
            # Decode URL encoding
            file_path = urllib.parse.unquote(file_path)

            # Construct full path
            base_path = Path(__file__).parent.parent
            full_path = base_path / file_path

            # Security check - ensure file is within base directory
            if not str(full_path.resolve()).startswith(str(base_path.resolve())):
                self.send_error(403, "Access denied")
                return

            if not full_path.exists() or not full_path.is_file():
                self.send_error(404, "File not found")
                return

            # Read and convert markdown
            with open(full_path, "r", encoding="utf-8") as f:
                md_content = f.read()

            # Convert to HTML
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
            html_content = html_content.replace("**Notes:**", "<br/>**Notes:**")
            # Handle case where Notes: appears without bold formatting
            html_content = html_content.replace("Notes:", "<br/>Notes:")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode())

        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")


def run_viewer(port=8001):
    """Run the markdown viewer server"""
    handler = MarkdownHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("📚 Sasiran Markdown Viewer starting...")
        print(f"📍 Server running at: http://localhost:{port}")
        print("🔍 Browse all markdown files in your project")
        print("⏹️  Press Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Viewer stopped.")


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8001
    run_viewer(port)

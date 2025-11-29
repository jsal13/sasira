#!/usr/bin/env python3
"""
Sasiran Language Game - Local Web Server
Serves the Sasiran language learning game content via a local web interface.
"""

import http.server
import socketserver
import os
import json
import markdown
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse


class SasiranGameHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Route handling
        if path == "/" or path == "/index.html":
            self.serve_index()
        elif path == "/api/sources":
            self.serve_sources_api()
        elif path == "/api/solutions":
            self.serve_solutions_api()
        elif path == "/api/reference":
            self.serve_reference_api()
        elif path.startswith("/game"):
            self.serve_game_page()
        elif path.startswith("/reference"):
            self.serve_reference_page()
        else:
            # Serve static files (CSS, JS, etc.)
            super().do_GET()

    def serve_index(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sasiran Language Game</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🏛️ Sasiran Language Game</h1>
            <p class="subtitle">Decipher the Ancient Whispered Tongue</p>
        </header>
        
        <nav class="main-nav">
            <a href="/game" class="nav-button">🎮 Play Game</a>
            <a href="/reference" class="nav-button">📖 Reference Materials</a>
            <a href="/solutions" class="nav-button">🗝️ Solutions</a>
        </nav>
        
        <main>
            <section class="intro">
                <h2>Welcome, Archaeological Linguist</h2>
                <p>You have been called to decipher mysterious texts discovered in ancient ruins. 
                These inscriptions are written in <strong>Sasiran</strong>, the "Whispered Tongue" 
                of a lost civilization.</p>
                
                <div class="game-features">
                    <div class="feature">
                        <h3>🔍 Discover Texts</h3>
                        <p>Explore archaeological sites and examine inscriptions found in marketplaces, 
                        temples, and sacred archives.</p>
                    </div>
                    <div class="feature">
                        <h3>📚 Build Vocabulary</h3>
                        <p>Use the reference materials to understand Sasiran grammar, vocabulary, 
                        and sentence structure.</p>
                    </div>
                    <div class="feature">
                        <h3>🧩 Translate Texts</h3>
                        <p>Progress from simple merchant records to complex prophetic inscriptions 
                        as your skills develop.</p>
                    </div>
                </div>
            </section>
        </main>
        
        <footer>
            <p>Sasiran Language Project - A constructed language inspired by Akkadian and Egyptian</p>
        </footer>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def serve_game_page(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sasiran Game - Play</title>
    <link rel="stylesheet" href="style.css">
    <script src="game.js" defer></script>
</head>
<body>
    <div class="container">
        <header>
            <h1><a href="/">🏛️ Sasiran Language Game</a></h1>
            <nav class="breadcrumb">
                <a href="/">Home</a> > <span>Game</span>
            </nav>
        </header>
        
        <main class="game-main">
            <aside class="difficulty-selector">
                <h3>Choose Difficulty</h3>
                <button class="difficulty-btn active" data-level="01">Beginner</button>
                <button class="difficulty-btn" data-level="02">Intermediate</button>
                <button class="difficulty-btn" data-level="03">Advanced</button>
            </aside>
            
            <section class="game-content">
                <div class="site-selector" id="site-selector">
                    <h2>Select Archaeological Site</h2>
                    <div id="site-list"></div>
                </div>
                
                <div class="text-viewer" id="text-viewer" style="display: none;">
                    <div class="site-context">
                        <h2 id="site-title"></h2>
                        <div id="site-context" class="context-box"></div>
                    </div>
                    
                    <div class="texts-container">
                        <h3>Discovered Texts</h3>
                        <div id="texts-list"></div>
                    </div>
                    
                    <div class="translation-area">
                        <h4>Your Translation:</h4>
                        <textarea id="translation-input" placeholder="Enter your translation here..."></textarea>
                        <button id="check-translation">Check Translation</button>
                        <button id="reveal-solution">Reveal Solution</button>
                    </div>
                    
                    <div id="feedback" class="feedback"></div>
                </div>
            </section>
            
            <aside class="quick-reference">
                <h3>Quick Reference</h3>
                <div class="ref-section">
                    <h4>Common Words</h4>
                    <div class="word-list" id="common-words"></div>
                </div>
                <div class="ref-section">
                    <h4>Grammar</h4>
                    <div class="grammar-notes">
                        <p><strong>Word Order:</strong> Subject-Object-Verb (SOV)</p>
                        <p><strong>Past:</strong> verb + უმ</p>
                        <p><strong>Future:</strong> verb + ალ</p>
                        <p><strong>Plural:</strong> noun + იმ</p>
                    </div>
                </div>
            </aside>
        </main>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def serve_reference_page(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sasiran Reference Materials</title>
    <link rel="stylesheet" href="style.css">
    <script src="reference.js" defer></script>
</head>
<body>
    <div class="container">
        <header>
            <h1><a href="/">🏛️ Sasiran Language Game</a></h1>
            <nav class="breadcrumb">
                <a href="/">Home</a> > <span>Reference</span>
            </nav>
        </header>
        
        <main class="reference-main">
            <nav class="reference-nav">
                <button class="ref-tab active" data-tab="dictionary">Dictionary</button>
                <button class="ref-tab" data-tab="examples">Example Sentences</button>
                <button class="ref-tab" data-tab="grammar">Grammar Guide</button>
            </nav>
            
            <section class="reference-content">
                <div id="dictionary" class="ref-content active">
                    <div id="dictionary-content"></div>
                </div>
                <div id="examples" class="ref-content">
                    <div id="examples-content"></div>
                </div>
                <div id="grammar" class="ref-content">
                    <div id="grammar-content"></div>
                </div>
            </section>
        </main>
    </div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def serve_sources_api(self):
        sources_data = self.load_markdown_files("../sources")
        self.send_json_response(sources_data)

    def serve_solutions_api(self):
        solutions_data = self.load_markdown_files("../solutions")
        self.send_json_response(solutions_data)

    def serve_reference_api(self):
        reference_data = self.load_markdown_files("../reference")
        self.send_json_response(reference_data)

    def load_markdown_files(self, directory):
        base_path = Path(__file__).parent / directory
        data = {}

        if not base_path.exists():
            return data

        for item in base_path.iterdir():
            if item.is_dir():
                data[item.name] = {}
                for file in item.iterdir():
                    if file.suffix == ".md":
                        with open(file, "r", encoding="utf-8") as f:
                            content = f.read()
                            data[item.name][file.stem] = {
                                "raw": content,
                                "html": markdown.markdown(content),
                                "title": self.extract_title(content),
                            }
            elif item.suffix == ".md":
                with open(item, "r", encoding="utf-8") as f:
                    content = f.read()
                    data[item.stem] = {
                        "raw": content,
                        "html": markdown.markdown(content),
                        "title": self.extract_title(content),
                    }

        return data

    def extract_title(self, content):
        # Extract first # heading as title
        match = re.search(r"^# (.+)$", content, re.MULTILINE)
        return match.group(1) if match else "Untitled"

    def send_json_response(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())


def run_server(port=8000):
    """Run the Sasiran game server on the specified port."""
    handler = SasiranGameHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🏛️  Sasiran Language Game Server starting...")
        print(f"📍 Server running at: http://localhost:{port}")
        print(f"🎮 Open your browser and visit the URL above to play!")
        print(f"⏹️  Press Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n🛑 Server stopped.")


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)

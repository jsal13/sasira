# 📚 Sasiran Markdown Viewer

A lightweight local web server for browsing and viewing all markdown files in the Sasiran project.

## Quick Start

1. **Navigate to the viewer directory:**
   ```bash
   cd viewer
   ```

2. **Run the viewer:**
   ```bash
   python3 view.py
   ```
   
   Or specify a custom port:
   ```bash
   python3 view.py 8080
   ```

3. **Open your browser:**
   - Go to `http://localhost:8001` (or your custom port)
   - Browse all markdown files with a clean interface

## Features

### 📁 **File Tree Navigation**
- **Hierarchical view** of all project folders and files
- **Expandable folders** with click-to-toggle functionality
- **Automatic file discovery** - finds all `.md` files in the project
- **Clean organization** with folders and individual files

### 📄 **Markdown Rendering**
- **Live HTML conversion** of markdown files
- **Styled output** with proper typography and formatting
- **Table support** with clean borders and styling
- **Code syntax highlighting** for code blocks
- **Responsive design** that works on different screen sizes

### 🎨 **Clean Interface**
- **Archaeological theme** matching the project aesthetic
- **Sidebar navigation** with file tree
- **Main content area** for viewing documents
- **Active file highlighting** to show current selection

### 🔍 **Smart Content Detection**
- **Automatic title extraction** from markdown files
- **Security checks** to prevent directory traversal
- **Error handling** for missing or inaccessible files
- **File type filtering** (only shows markdown files)

## Project Structure Coverage

The viewer automatically discovers and displays:

```
📁 sources/           # Archaeological source texts
├── 01/              # Beginner difficulty
├── 02/              # Intermediate difficulty  
└── 03/              # Advanced difficulty

📁 solutions/        # Translation solutions
├── 01/              # Beginner solutions
├── 02/              # Intermediate solutions
└── 03/              # Advanced solutions

📁 reference/        # Language reference materials
├── dictionary.md    # Sasiran vocabulary
└── example_sentences.md # Practice sentences

📄 Individual files  # Project documentation
├── SASIRAN_CONTEXT_INSTRUCTIONS.md
└── copilot_context.md
```

## Usage Scenarios

### **Quick Reference Lookup**
- Need to check a word in the dictionary? 
- Open viewer → reference → dictionary.md

### **Compare Sources and Solutions**  
- Working on translation? 
- Open sources/01/marketplace.md in one tab
- Open solutions/01/marketplace.md in another

### **Project Documentation Review**
- Browse all project files in organized structure
- Read context instructions and development notes
- Review example sentences and grammar

### **Content Creation Workflow**
- Check existing content before adding new files
- Review writing style and formatting consistency
- Verify link references and file organization

## Technical Details

- **Pure Python** - No external dependencies except `markdown`
- **Auto-installation** - Installs markdown package if needed  
- **Lightweight** - Minimal resource usage
- **Secure** - Path validation prevents directory traversal attacks
- **Fast** - Files are parsed on demand, not pre-loaded

## API Endpoints

- `GET /` - Main viewer interface
- `GET /api/files` - JSON file tree structure
- `GET /view/{filepath}` - Render markdown file as HTML

## Comparison with Game Viewer

| Feature    | Markdown Viewer | Game Interface       |
| ---------- | --------------- | -------------------- |
| Purpose    | File browsing   | Interactive gameplay |
| Complexity | Simple          | Full featured        |
| Load Time  | Fast            | Moderate             |
| Use Case   | Quick reference | Learning/playing     |
| Navigation | File tree       | Guided experience    |

## Perfect For

- **Quick reference** during development
- **Content review** and proofreading  
- **File organization** verification
- **Documentation browsing**
- **Lightweight viewing** without game features

---

**Simple, fast, and effective markdown viewing for the Sasiran project! 📚✨**
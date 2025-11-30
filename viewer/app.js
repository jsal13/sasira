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

        // Only show files from the 'sources' directory
        if (this.files.sources) {
            const sourcesContent = this.files.sources;
            this.renderFolder(tree, 'sources', sourcesContent);
        } else {
            tree.innerHTML = '<p>No sources directory found.</p>';
        }
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
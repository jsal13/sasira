// Sasiran Language Game - Main JavaScript

class SasiranGame {
    constructor() {
        this.currentLevel = '01';
        this.currentSite = null;
        this.currentText = null;
        this.sources = {};
        this.solutions = {};
        this.reference = {};

        this.init();
    }

    async init() {
        await this.loadData();
        this.setupEventListeners();
        this.updateSiteList();
        this.loadQuickReference();
    }

    async loadData() {
        try {
            const [sourcesRes, solutionsRes, referenceRes] = await Promise.all([
                fetch('/api/sources'),
                fetch('/api/solutions'),
                fetch('/api/reference')
            ]);

            this.sources = await sourcesRes.json();
            this.solutions = await solutionsRes.json();
            this.reference = await referenceRes.json();
        } catch (error) {
            console.error('Error loading data:', error);
        }
    }

    setupEventListeners() {
        // Difficulty buttons
        document.querySelectorAll('.difficulty-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelector('.difficulty-btn.active').classList.remove('active');
                btn.classList.add('active');
                this.currentLevel = btn.dataset.level;
                this.updateSiteList();
                this.showSiteSelector();
            });
        });

        // Translation buttons
        const checkBtn = document.getElementById('check-translation');
        const revealBtn = document.getElementById('reveal-solution');

        if (checkBtn) {
            checkBtn.addEventListener('click', () => this.checkTranslation());
        }

        if (revealBtn) {
            revealBtn.addEventListener('click', () => this.revealSolution());
        }
    }

    updateSiteList() {
        const siteList = document.getElementById('site-list');
        if (!siteList) return;

        const levelSources = this.sources[this.currentLevel] || {};
        siteList.innerHTML = '';

        Object.keys(levelSources).forEach(siteKey => {
            const site = levelSources[siteKey];
            const siteItem = document.createElement('div');
            siteItem.className = 'site-item';
            siteItem.innerHTML = `
                <h3>${site.title}</h3>
                <p>Click to explore this archaeological site</p>
            `;

            siteItem.addEventListener('click', () => {
                this.loadSite(siteKey);
            });

            siteList.appendChild(siteItem);
        });
    }

    loadSite(siteKey) {
        this.currentSite = siteKey;
        const site = this.sources[this.currentLevel][siteKey];

        // Update site title and context
        document.getElementById('site-title').textContent = site.title;

        // Extract context from markdown
        const contextMatch = site.raw.match(/## Context\s*([\s\S]*?)(?=## |$)/);
        const context = contextMatch ? contextMatch[1].trim() : 'No context available.';
        document.getElementById('site-context').innerHTML = context;

        // Extract texts
        const textsMatch = site.raw.match(/## Texts\s*([\s\S]*?)$/);
        const textsSection = textsMatch ? textsMatch[1] : '';

        const textsList = document.getElementById('texts-list');
        textsList.innerHTML = '';

        // Parse individual texts
        const textRegex = /### (.+?)\s*\*\*Sasiran:\*\* (.+?)\s*\*\*Notes:\*\* (.+?)(?=###|$)/gs;
        let match;
        let textIndex = 0;

        while ((match = textRegex.exec(textsSection)) !== null) {
            const [, title, sasiran, notes] = match;

            const textItem = document.createElement('div');
            textItem.className = 'text-item';
            textItem.innerHTML = `
                <h4>${title.trim()}</h4>
                <div class="sasiran-text">${sasiran.trim()}</div>
                <p><strong>Notes:</strong> ${notes.trim()}</p>
                <button class="translate-btn" data-index="${textIndex}">Translate This Text</button>
            `;

            textItem.querySelector('.translate-btn').addEventListener('click', () => {
                this.selectText(textIndex, title.trim(), sasiran.trim());
            });

            textsList.appendChild(textItem);
            textIndex++;
        }

        this.showTextViewer();
    }

    selectText(index, title, sasiran) {
        this.currentText = { index, title, sasiran };

        // Clear previous translation
        document.getElementById('translation-input').value = '';
        document.getElementById('feedback').style.display = 'none';

        // Highlight selected text
        document.querySelectorAll('.text-item').forEach((item, i) => {
            if (i === index) {
                item.style.background = 'var(--secondary-color)';
                item.style.border = '2px solid var(--primary-color)';
            } else {
                item.style.background = '#f8f8f8';
                item.style.border = '1px solid var(--border-color)';
            }
        });

        // Scroll to translation area
        document.querySelector('.translation-area').scrollIntoView({ behavior: 'smooth' });
    }

    checkTranslation() {
        if (!this.currentText) {
            alert('Please select a text to translate first.');
            return;
        }

        const userTranslation = document.getElementById('translation-input').value.trim().toLowerCase();
        const solution = this.getSolution(this.currentText.sasiran);

        if (!solution) {
            this.showFeedback('No solution found for this text.', 'incorrect');
            return;
        }

        // Simple similarity check (can be enhanced)
        const similarity = this.calculateSimilarity(userTranslation, solution.toLowerCase());

        if (similarity > 0.7) {
            this.showFeedback('Excellent! Your translation is very close.', 'correct');
        } else if (similarity > 0.4) {
            this.showFeedback('Good attempt! You have some correct elements, but try again.', 'incorrect');
        } else {
            this.showFeedback('Keep trying! Consider checking the reference materials.', 'incorrect');
        }
    }

    revealSolution() {
        if (!this.currentText) {
            alert('Please select a text to translate first.');
            return;
        }

        const solution = this.getSolution(this.currentText.sasiran);

        if (solution) {
            this.showFeedback(`Solution: ${solution}`, 'solution');
            document.getElementById('translation-input').value = solution;
        } else {
            this.showFeedback('Solution not available for this text.', 'incorrect');
        }
    }

    getSolution(sasiranText) {
        const levelSolutions = this.solutions[this.currentLevel];
        if (!levelSolutions || !this.currentSite) return null;

        const siteSolutions = levelSolutions[this.currentSite];
        if (!siteSolutions) return null;

        // Parse solutions from markdown
        const solutionsText = siteSolutions.raw;
        const regex = new RegExp(`\\*\\*Sasiran:\\*\\*\\s*${sasiranText.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&')}\\s*\\*\\*Translation:\\*\\*\\s*"([^"]+)"`, 'i');
        const match = solutionsText.match(regex);

        return match ? match[1] : null;
    }

    calculateSimilarity(str1, str2) {
        const longer = str1.length > str2.length ? str1 : str2;
        const shorter = str1.length > str2.length ? str2 : str1;

        if (longer.length === 0) return 1.0;

        const distance = this.levenshteinDistance(longer, shorter);
        return (longer.length - distance) / longer.length;
    }

    levenshteinDistance(str1, str2) {
        const matrix = [];

        for (let i = 0; i <= str2.length; i++) {
            matrix[i] = [i];
        }

        for (let j = 0; j <= str1.length; j++) {
            matrix[0][j] = j;
        }

        for (let i = 1; i <= str2.length; i++) {
            for (let j = 1; j <= str1.length; j++) {
                if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
                    matrix[i][j] = matrix[i - 1][j - 1];
                } else {
                    matrix[i][j] = Math.min(
                        matrix[i - 1][j - 1] + 1,
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1
                    );
                }
            }
        }

        return matrix[str2.length][str1.length];
    }

    showFeedback(message, type) {
        const feedback = document.getElementById('feedback');
        feedback.textContent = message;
        feedback.className = `feedback ${type}`;
        feedback.style.display = 'block';
    }

    showSiteSelector() {
        document.getElementById('site-selector').style.display = 'block';
        document.getElementById('text-viewer').style.display = 'none';
    }

    showTextViewer() {
        document.getElementById('site-selector').style.display = 'none';
        document.getElementById('text-viewer').style.display = 'block';
    }

    loadQuickReference() {
        const commonWords = document.getElementById('common-words');
        if (!commonWords) return;

        // Extract common words from dictionary
        const dictionary = this.reference.dictionary;
        if (dictionary) {
            const words = [
                'სა - I, me',
                'სი - you',
                'სუ - he/she/it',
                'სარ - to be',
                'სომ - to come',
                'შალ - person',
                'აშ - water',
                'შინ - sun',
                'უშუ - temple'
            ];
            commonWords.innerHTML = words.join('<br>');
        }
    }
}

// Initialize the game when the page loads
if (document.querySelector('.game-main')) {
    new SasiranGame();
}
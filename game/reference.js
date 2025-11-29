// Sasiran Language Reference - JavaScript

class SasiranReference {
    constructor() {
        this.reference = {};
        this.init();
    }

    async init() {
        await this.loadReferenceData();
        this.setupEventListeners();
        this.loadDictionary();
    }

    async loadReferenceData() {
        try {
            const response = await fetch('/api/reference');
            this.reference = await response.json();
        } catch (error) {
            console.error('Error loading reference data:', error);
        }
    }

    setupEventListeners() {
        document.querySelectorAll('.ref-tab').forEach(tab => {
            tab.addEventListener('click', (e) => {
                const tabName = tab.dataset.tab;
                this.switchTab(tabName);
            });
        });
    }

    switchTab(tabName) {
        // Update tab buttons
        document.querySelectorAll('.ref-tab').forEach(tab => {
            tab.classList.remove('active');
        });
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

        // Update content
        document.querySelectorAll('.ref-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabName).classList.add('active');

        // Load content based on tab
        switch (tabName) {
            case 'dictionary':
                this.loadDictionary();
                break;
            case 'examples':
                this.loadExamples();
                break;
            case 'grammar':
                this.loadGrammar();
                break;
        }
    }

    loadDictionary() {
        const content = document.getElementById('dictionary-content');
        if (!content) return;

        const dictionary = this.reference.dictionary;
        if (!dictionary) {
            content.innerHTML = '<p>Dictionary not available.</p>';
            return;
        }

        // Process the markdown content to create a more interactive dictionary
        let html = dictionary.html;

        // Add search functionality
        html = `
            <div class="dictionary-search">
                <input type="text" id="dict-search" placeholder="Search dictionary..." />
            </div>
            <div class="dictionary-content">
                ${html}
            </div>
        `;

        content.innerHTML = html;

        // Add search functionality
        const searchInput = document.getElementById('dict-search');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                this.filterDictionary(e.target.value);
            });
        }
    }

    filterDictionary(searchTerm) {
        const dictContent = document.querySelector('.dictionary-content');
        if (!dictContent) return;

        const sections = dictContent.querySelectorAll('h3, h4, p, li');

        if (!searchTerm) {
            sections.forEach(section => section.style.display = '');
            return;
        }

        sections.forEach(section => {
            const text = section.textContent.toLowerCase();
            if (text.includes(searchTerm.toLowerCase())) {
                section.style.display = '';
                // Show parent heading if a child matches
                let parent = section.previousElementSibling;
                while (parent && (parent.tagName === 'H3' || parent.tagName === 'H4')) {
                    parent.style.display = '';
                    parent = parent.previousElementSibling;
                }
            } else {
                section.style.display = 'none';
            }
        });
    }

    loadExamples() {
        const content = document.getElementById('examples-content');
        if (!content) return;

        const examples = this.reference.example_sentences;
        if (!examples) {
            content.innerHTML = '<p>Example sentences not available.</p>';
            return;
        }

        // Process the examples to make them more interactive
        let html = examples.html;

        // Add difficulty filter
        html = `
            <div class="examples-filter">
                <label>Filter by difficulty:</label>
                <select id="examples-filter">
                    <option value="all">All Examples</option>
                    <option value="simple">Simple Sentences</option>
                    <option value="intermediate">Intermediate Sentences</option>
                    <option value="advanced">Advanced Sentences</option>
                </select>
            </div>
            <div class="examples-content">
                ${html}
            </div>
        `;

        content.innerHTML = html;

        // Add filter functionality
        const filter = document.getElementById('examples-filter');
        if (filter) {
            filter.addEventListener('change', (e) => {
                this.filterExamples(e.target.value);
            });
        }

        // Add click-to-reveal functionality for translations
        this.makeExamplesInteractive();
    }

    filterExamples(difficulty) {
        const examplesContent = document.querySelector('.examples-content');
        if (!examplesContent) return;

        const sections = examplesContent.querySelectorAll('h2');

        sections.forEach(section => {
            const sectionTitle = section.textContent.toLowerCase();
            let shouldShow = false;

            switch (difficulty) {
                case 'all':
                    shouldShow = true;
                    break;
                case 'simple':
                    shouldShow = sectionTitle.includes('simple');
                    break;
                case 'intermediate':
                    shouldShow = sectionTitle.includes('intermediate');
                    break;
                case 'advanced':
                    shouldShow = sectionTitle.includes('advanced') || sectionTitle.includes('sacred');
                    break;
            }

            // Show/hide section and its content
            let element = section;
            while (element && !element.nextElementSibling?.tagName?.startsWith('H2')) {
                element.style.display = shouldShow ? '' : 'none';
                element = element.nextElementSibling;
                if (!element) break;
            }
            if (element && element.tagName?.startsWith('H2')) {
                element.style.display = shouldShow ? '' : 'none';
            }
        });
    }

    makeExamplesInteractive() {
        const examplesContent = document.querySelector('.examples-content');
        if (!examplesContent) return;

        // Find all Sasiran/Translation pairs
        const paras = examplesContent.querySelectorAll('p');

        paras.forEach(para => {
            const text = para.innerHTML;
            if (text.includes('**Sasiran:**') && text.includes('**Translation:**')) {
                // Split into Sasiran and Translation
                const parts = text.split('**Translation:**');
                if (parts.length === 2) {
                    const sasiran = parts[0].replace('**Sasiran:**', '').trim();
                    const translation = parts[1].trim();

                    para.innerHTML = `
                        <div class="example-sentence">
                            <div class="sasiran-line"><strong>Sasiran:</strong> ${sasiran}</div>
                            <div class="translation-line" style="display: none;">
                                <strong>Translation:</strong> ${translation}
                            </div>
                            <button class="reveal-btn" onclick="this.previousElementSibling.style.display = this.previousElementSibling.style.display === 'none' ? 'block' : 'none'; this.textContent = this.textContent === 'Show Translation' ? 'Hide Translation' : 'Show Translation';">Show Translation</button>
                        </div>
                    `;
                }
            }
        });
    }

    loadGrammar() {
        const content = document.getElementById('grammar-content');
        if (!content) return;

        // Create a comprehensive grammar guide
        const grammarGuide = `
            <h2>Sasiran Grammar Reference</h2>
            
            <div class="grammar-section">
                <h3>Basic Word Order</h3>
                <p>Sasiran follows <strong>Subject-Object-Verb (SOV)</strong> order, like Akkadian.</p>
                <div class="grammar-example">
                    <div class="sasiran">სა აш სირ</div>
                    <div class="breakdown">სა (I) + აश (water) + სირ (see) = "I see water"</div>
                </div>
            </div>
            
            <div class="grammar-section">
                <h3>Pronouns</h3>
                <table class="grammar-table">
                    <tr><th>Sasiran</th><th>English</th></tr>
                    <tr><td>სა</td><td>I, me</td></tr>
                    <tr><td>სი</td><td>you (singular)</td></tr>
                    <tr><td>სუ</td><td>he/she/it</td></tr>
                    <tr><td>სარ</td><td>we</td></tr>
                    <tr><td>სირ</td><td>you (plural)</td></tr>
                    <tr><td>სურ</td><td>they</td></tr>
                </table>
            </div>
            
            <div class="grammar-section">
                <h3>Verb Tenses</h3>
                <h4>Present Tense</h4>
                <p>Use the base form of the verb:</p>
                <div class="grammar-example">სა ზურ = "I love"</div>
                
                <h4>Past Tense</h4>
                <p>Add <strong>-უმ</strong> to the verb stem:</p>
                <div class="grammar-example">სა ზურუმ = "I loved"</div>
                
                <h4>Future Tense</h4>
                <p>Add <strong>-ალ</strong> to the verb stem:</p>
                <div class="grammar-example">სა ზურალ = "I will love"</div>
            </div>
            
            <div class="grammar-section">
                <h3>Noun Forms</h3>
                <h4>Plurals</h4>
                <p>Add <strong>-იმ</strong> to make nouns plural:</p>
                <div class="grammar-example">
                    შალ → შალიმ (person → people)<br>
                    აش → აשიმ (water → waters)
                </div>
                
                <h4>Possessive</h4>
                <p>Add <strong>-შ</strong> to show possession:</p>
                <div class="grammar-example">
                    შალ → შალშ (person → person's)<br>
                    სარ → სარშ (king → king's)
                </div>
            </div>
            
            <div class="grammar-section">
                <h3>Common Prepositions</h3>
                <table class="grammar-table">
                    <tr><th>Sasiran</th><th>English</th><th>Example</th></tr>
                    <tr><td>ან</td><td>in, within</td><td>უშუ ან (in the temple)</td></tr>
                    <tr><td>ურ</td><td>on, upon</td><td>შალიმ ურ (upon people)</td></tr>
                    <tr><td>ილ</td><td>with</td><td>ლის ილ (with friend)</td></tr>
                    <tr><td>აზ</td><td>from</td><td>შოს აზ (from river)</td></tr>
                    <tr><td>ის</td><td>to, toward</td><td>შალიმ ის (to people)</td></tr>
                </table>
            </div>
            
            <div class="grammar-section">
                <h3>Conjunctions</h3>
                <table class="grammar-table">
                    <tr><th>Sasiran</th><th>English</th></tr>
                    <tr><td>ორ</td><td>and</td></tr>
                    <tr><td>ულ</td><td>but, however</td></tr>
                    <tr><td>იფ</td><td>if, when</td></tr>
                </table>
            </div>
            
            <div class="grammar-section">
                <h3>Practice Tips</h3>
                <ul>
                    <li>Remember SOV word order: put verbs at the end</li>
                    <li>Sibilants (s, z, sh sounds) are common in Sasiran</li>
                    <li>Most plosives (hard consonants) are avoided</li>
                    <li>Context from archaeological discovery helps with translation</li>
                    <li>Religious vocabulary appears frequently in temple texts</li>
                </ul>
            </div>
        `;

        content.innerHTML = grammarGuide;
    }
}

// Initialize the reference system when the page loads
if (document.querySelector('.reference-main')) {
    new SasiranReference();
}
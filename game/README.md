# 🏛️ Sasiran Language Game

An interactive web-based translation game for learning the constructed ancient language **Sasiran**.

## Quick Start

1. **Navigate to the game directory:**
   ```bash
   cd game
   ```

2. **Run the game:**
   ```bash
   python3 play.py
   ```
   
   Or specify a custom port:
   ```bash
   python3 play.py 8080
   ```

3. **Open your browser:**
   - Go to `http://localhost:8000` (or your custom port)
   - Start translating ancient texts!

## Game Features

### 🎮 Interactive Translation Game
- **Progressive Difficulty:** Start with simple marketplace inscriptions, advance to complex prophetic texts
- **Archaeological Context:** Each text comes with discovery context to aid translation
- **Real-time Feedback:** Check your translations and get hints
- **Solution System:** Reveal solutions when stuck

### 📖 Comprehensive Reference Materials
- **Complete Dictionary:** 50+ Sasiran words with English translations
- **Grammar Guide:** SOV word order, tense formations, and grammatical rules
- **Example Sentences:** Practice sentences with translations at multiple difficulty levels
- **Interactive Features:** Search dictionary, filter examples, click-to-reveal translations

### 🗝️ Solution Access
- Complete translations for all source texts
- Detailed linguistic analysis
- Grammar explanations for each text

## Game Structure

```
📁 Difficulty Levels:
├── 01/ Beginner    - Simple daily life, marketplace, basic temple texts
├── 02/ Intermediate - Ceremonial practices, scholarly works  
└── 03/ Advanced    - Sacred archives, complex prophecies, tower inscriptions

📁 Archaeological Sites:
├── Marketplace     - Merchant records, trade documents
├── Temple Area     - Religious inscriptions, devotional texts
├── Ceremonial Areas - Ritual texts, altar inscriptions
├── Scholarly Complex - Academic documents, underground archives
├── Sacred Archives  - Prophetic texts, sacred decrees
└── Tower Complex   - Monumental inscriptions, dedications
```

## Language Overview

**Sasiran** (the "Whispered Tongue") is a constructed language inspired by Akkadian and Egyptian:

- **Writing System:** Uses Ethiopian (Ge'ez) and Georgian characters
- **Phonology:** Emphasizes sibilants (s, z, š, ž), minimal plosives
- **Grammar:** SOV word order, agglutinative morphology
- **Vocabulary:** ~50 core words covering daily life, religion, nature, and society

### Basic Grammar
- **Present:** Base verb form → `სა ზურ` (I love)
- **Past:** Verb + უმ → `სა ზურუმ` (I loved)  
- **Future:** Verb + ალ → `სა ზურალ` (I will love)
- **Plural:** Noun + იმ → `შალ → შალიმ` (person → people)
- **Possessive:** Noun + შ → `შალ → შალშ` (person → person's)

## Technical Requirements

- **Python 3.6+**
- **Web Browser** (Chrome, Firefox, Safari, Edge)
- **Automatic Installation:** Required packages (`markdown`) install automatically

## File Structure

```
game/
├── server.py          # Main web server with API endpoints
├── play.py           # Game launcher script  
├── style.css         # Game styling and layout
├── game.js           # Interactive game functionality
├── reference.js      # Reference material interface
└── README.md         # This file
```

## API Endpoints

The game server provides REST API endpoints:

- `GET /api/sources` - Archaeological source texts
- `GET /api/solutions` - Translation solutions  
- `GET /api/reference` - Dictionary and grammar materials

## Customization

### Adding New Texts
1. Add markdown files to appropriate `sources/` difficulty folder
2. Add corresponding solutions to `solutions/` folder
3. Restart the server - new content loads automatically

### Modifying Vocabulary
1. Edit `reference/dictionary.md` 
2. Update `reference/example_sentences.md`
3. Reload the reference page

## Educational Use

Perfect for:
- **Linguistics Students:** Practice with constructed language analysis
- **Game-Based Learning:** Engaging way to learn language structure  
- **Archaeological Role-Play:** Immersive historical linguistic discovery
- **Puzzle Enthusiasts:** Progressive difficulty translation challenges

## License

This is an educational project for learning constructed languages and archaeological linguistics.

---

**Happy translating! May you uncover the secrets of the Whispered Tongue! 🏺📜**
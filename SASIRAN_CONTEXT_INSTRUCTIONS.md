# Sasiran Language Game - Context Instructions for AI Assistants

## Project Overview

This directory contains materials for a language translation game featuring **Sasiran** - a constructed ancient language with fictional archaeological context. The project includes a Flask-based web viewer, comprehensive language documentation, and progressive difficulty learning materials.

### Current Project Status

- **Complete vocabulary**: 100+ words with systematic morpheme construction
- **JSON-structured dictionary**: Computational format for language analysis
- **20 example sentences**: Demonstrating SOV grammar patterns
- **Flask web applications**: Both legacy viewer and new webapp with foldable tables
- **Progressive content**: 10 archaeological sites with increasing difficulty
- **Unified format**: All sources now include translations alongside original texts
- **Difficulty organization**: Level-based content grouping with visual headers

## Language Characteristics - Sasiran

- **Inspiration**: Akkadian grammar with original vocabulary
- **Phonology**: Sibilant-heavy (s, z, š, ž, ṣ, ḫ) with minimal plosives (d, g only)
- **Word Order**: SOV (Subject-Object-Verb) - strict ordering
- **Morphology**: Agglutinative with systematic morpheme construction
- **Script**: Lycian characters for writing system (left-to-right reading direction)

### Core Morpheme Types

- **Pronouns**: sa (I), šu (you), lu (he/she/it), + plural/conjunctive forms
- **Verbs**: ašu (do/make), ešu (move), šu (create/make) - combine with other morphemes
- **Body Parts**: šen (eye), nas (ear), žaf (mouth), ṣir (hand), haš (foot), šer (heart)
- **Descriptors**: Size (zur/gah), temperature (zer/šif), texture (mal/ṣar), colors (žel/ḫar)
- **Nature**: šez (tree), šul (wind), mur (rain) + plant/weather elements

## Directory Structure

```shell
/home/james/repos/sasira/
├── SASIRAN_CONTEXT_INSTRUCTIONS.md    # This comprehensive guide
├── viewer/                           # Legacy Flask web application
│   ├── server.py                     # Original Flask server with hot reload
│   ├── index.html                    # UI template with file navigation
│   ├── styles.css                    # Sasiran-themed styling
│   ├── app.js                        # Frontend JavaScript
│   └── README.md                     # Viewer documentation
├── webapp/                           # New Flask web application
│   ├── app.py                        # Main Flask server with table view
│   ├── templates/
│   │   └── index.html                # Foldable table interface
│   ├── requirements.txt              # Python dependencies
│   └── README.md                     # Webapp documentation
├── reference/                        # Language documentation
│   ├── dictionary.json               # 100+ word structured vocabulary
│   └── example_sentences.json        # 20 sentences with translations
└── sources/                          # Game content with translations
    ├── 01/                           # Beginner: Daily life contexts
    │   ├── marketplace.json           # Trade and commerce
    │   ├── temple_area.json           # Basic religious practices
    │   ├── workshop.json              # Artisan crafts and tools
    │   ├── residential.json           # Family and household life
    │   └── guard_post.json            # Military outpost duties
    ├── 02/                           # Intermediate: Cultural contexts
    │   ├── ceremonial_areas.json     # Ritual and ceremonial texts
    │   ├── scholarly_complex.json    # Academic/scholarly discoveries
    │   ├── administrative_center.json # Government and bureaucracy
    │   ├── military_academy.json     # Advanced military training
    │   └── merchant_quarter_elite.json # Elite commercial activities
```

## Technical Infrastructure

- **Flask Applications**: 
  - Legacy viewer with markdown rendering and file navigation
  - New webapp with foldable table interface organized by difficulty level
- **Docker Support**: Full containerization with docker-compose.yml (configured for webapp)
- **JSON Vocabulary**: Computational format enabling systematic word construction
- **Difficulty Organization**: Level 01 (Beginner) and Level 02 (Intermediate) with visual headers
- **Foldable Interface**: Collapsible sections per archaeological site with context display

## Word Construction Patterns

**Verb Formation:**

- `{sense_organ} + ašu` = sense_verb (šen + ašu = šenašu "to see")
- `{body_part} + ašu` = action_verb (ṣir + ašu = ṣirašu "to carry")  
- `{body_part} + šu` = creation_verb (žaf + šu = žafšu "to speak")
- `{quality} + šu` = quality_change_verb (mal + šu = malšu "to smooth")

**Noun Formation:**

- `{quality} + šu` = substance/object (me + šu = mešu "water")
- `{quality} + ru` = energy/multiple (žih + ru = žihru "stars")
- `{plant} + ru` = collection (šez + ru = šezru "forest")

**Adjective Formation:**

- `{quality} + ru` = plural_adjective (zur + ru = zurru "small ones")

**Pronoun Formation:**

- `{pronoun} + ru` = plural (šu + ru = šuru "you-plural")
- `{pronoun} + nu` = inclusive (sa + nu = sanu "we")

## How to Use This Context

### For AI Assistant Onboarding

1. **Read vocabulary first**: `/reference/dictionary.json` contains 100+ words with construction patterns
2. **Study sentence patterns**: `/reference/example_sentences.json` has 20 SOV examples  
3. **Review specific content**: Check relevant `/sources/` files for archaeological context
4. **Choose interface**: Use `/viewer/` for development or `/webapp/` for organized table view

### For Translation Tasks

1. **Reference the dictionary** (`reference/dictionary.json`) for vocabulary and construction patterns
2. **Check example sentences** (`reference/example_sentences.json`) for grammar patterns  
3. **Consider archaeological context** from the relevant source file
4. **Apply SOV word order** consistently in all constructions

### For Content Creation

When adding new texts to source files:

- **Use markdown format** with `## Context` and `## Texts` sections
- **Provide archaeological context** explaining where/how text was discovered
- **Use appropriate difficulty level** for the folder (01=beginner, 02=intermediate)
- **Follow established vocabulary** and grammar patterns from dictionary.json

### For Language Development

- **Maintain consistency** with established phonology (emphasize sibilants)
- **Build on existing morphemes** before creating new words - use construction patterns
- **Follow SOV grammar patterns** established in examples
- **Keep morphology simple** and regular - agglutinative structure

### For Technical Development

- **Flask server** runs on `python viewer/server.py` with hot reload enabled
- **Docker setup** available via `docker-compose up` for full environment
- **JSON structure** enables computational linguistics analysis and word construction

## Key Grammar Reminders

- **Word Order:** Subject-Object-Verb (SOV) - strictly enforced
- **Morphology:** Agglutinative - complex words built from simple morphemes
- **Phonology:** Sibilant-heavy with minimal plosives (only d, g allowed)
- **Script:** Lycian/Phoenician characters for authentic appearance

## Character Usage Notes

- **Sibilants should dominate** phonetically: s, z, š, ž, ṣ, ḫ
- **Avoid heavy plosive clusters** (minimal b, p, t, k sounds)
- **Use vowels** a, i, u, e, o regularly
- **Include liquids** r, l, m, n for flow

## Archaeological Context Themes

- **01/ (Beginner):** Daily life, marketplace, basic temple areas - simple vocabulary  
- **02/ (Intermediate):** Ceremonial practices, scholarly activities - complex grammar

## Translation Game Mechanics

Players encounter texts with:

1. **Archaeological context** (where/how found)
2. **Sasiran text** to translate using established vocabulary
3. **Script representation** in Lycian characters
4. **English translations** provided for learning and verification
5. **Contextual clues** to aid translation understanding
6. **Progressive difficulty** requiring accumulated morpheme knowledge

## Content Creation Process

### Unified File Structure

The game content uses a streamlined single-file system where each JSON contains both the challenge and the answer:

**Current Format** (`sources/01/marketplace.json`):

```json
{
    "name": "Marketplace",
    "context": "Archaeological discovery context...",
    "texts": [
        {
            "name": "Merchant's Daily Record",
            "sasiran": "Sa mešu ṣirašu.",
            "script": "𐊖𐊀 𐤌𐤄𐤔𐤅 𐤑𐤉𐤓𐤀𐤔𐤅",
            "notes": "Found beneath collapsed stone counter. Hastily carved..."
        }
    ]
}
```

**Translation Integration**: All source files now include translations directly in the JSON structure, eliminating the need for separate solution files. Each text entry contains both the Sasiran content and its English translation:

```json
{
    "name": "Marketplace", 
    "context": "Archaeological context and cultural significance...",
    "texts": [
        {
            "name": "Merchant's Daily Record",
            "sasiran": "Sa mešu ṣirašu.",
            "script": "𐊖𐊀 𐤌𐤄𐤔𐤅 𐤑𐤉𐤓𐤀𐤔𐤅",
            "translation": "I carry water.",
            "notes": "Found beneath collapsed stone counter. Hastily carved..."
        }
    ]
}
```

### Content Creation Guidelines

**Archaeological Notes**: Focus on discovery context, script quality, and cultural significance rather than grammatical explanations:

- **Discovery location**: "Found beneath collapsed stone counter", "near central plaza entrance"
- **Script quality**: "hastily carved with casual script", "formal script suggests public proclamation"
- **Cultural context**: "likely a personal note", "possibly official documentation"

**Vocabulary Selection**: Use beginner-appropriate morphemes for level 01:

- Basic pronouns: sa, šu, lu, sanu, šuru, luru
- Simple verbs: ṣirašu (carry), žafašu (eat), šenašu (see)
- Common nouns: mešu (water), ašmu (stone), nehšu (fruit)
- Basic adjectives: nehru (sweet ones), ašmru (hard ones)

**SOV Structure**: All sentences follow Subject-Object-Verb pattern:

- "Sa mešu ṣirašu" = "I water carry" = "I carry water"
- "Luru nehšu žafšu" = "They fruit speak" = "They speak of fruit"

---

## Dictionary Optimization and Analysis Features

### Quick Lookup System

The dictionary now includes optimized lookup indexes for efficient analysis:

- **`quick_lookup.by_sasiran`**: Direct word lookup by Sasiran text with complete information
- **`quick_lookup.by_meaning`**: Reverse lookup by English meaning to find Sasiran words  
- **`quick_lookup.by_type`**: Grouped words by grammatical category (pronouns, verbs, nouns, etc.)
- **`morpheme_patterns`**: Analysis helpers for verb endings, construction formulas, and patterns

### Advanced Vocabulary

**Compound Words** (Level 02+):
- `mehuš` (rivers) = me + hu + š (water + flow + sound)
- `šamšeru` (dawn) = šam + še + ru (bright + early + plural)  
- `ašmgah` (mountains) = ašm + gah (hard + great)
- `šulsur` (trade winds) = šul + sur (wind + new)
- `šezru` (seasons) = šez + ru (time + plural)
- `gahmur` (storm) = gah + mur (big + rain)

**Advanced Verbs** (for sophisticated contexts):
- `ženašu` (to inspect/examine) - used in commercial and academic contexts
- `ženšu` (to tend/signal) - care or communication actions
- `žarašu` (to arbitrate/negotiate) - diplomatic and legal contexts

## Translation Validation Guidelines

### Contextual Appropriateness

When reviewing or creating translations, ensure they match archaeological contexts:

**Level 01 (Beginner) - Daily Life:**
- Simple, practical vocabulary (water, food, tools, basic activities)
- Personal and domestic contexts (family meals, household tasks)
- Basic commercial activities (simple trade, water collection)
- Elementary religious practices (daily prayers, basic offerings)

**Level 02 (Intermediate) - Cultural Sophistication:**
- Administrative language (legal disputes, diplomatic correspondence)
- Elite commerce (credit systems, quality assurance, international trade)
- Academic discourse (scholarly debates, scientific observations)
- Advanced military concepts (tactical formations, intelligence gathering)
- Complex ceremonial practices (ritual instructions, community blessings)

### Common Translation Improvements

Based on validation work, avoid these patterns:

**Generic Translations** → **Context-Specific Alternatives:**
- "I see hard ones" → "I count our tools" (household inventory)
- "You see stone" → "You inspect goods" (merchant quality check)
- "They speak of fire" → "They signal with fire" (military communications)
- "I love forest sweet ones" → "I study forest sweet ones" (scholarly research)

### Morphological Analysis Tools

Use the dictionary's `morpheme_patterns` for:
- **Verb classification**: Identify action_verbs (ašu), creation_verbs (šu), motion_verbs (ešu)
- **Construction validation**: Verify compounds follow established formulas
- **Type grouping**: Organize vocabulary by grammatical function

## Content Quality Standards

### Archaeological Note Guidelines

**Effective Notes Include:**
- **Physical discovery context**: exact location, associated artifacts
- **Script characteristics**: formality level, wear patterns, material quality
- **Cultural significance**: intended audience, social context, usage patterns
- **Preservation state**: damage patterns, environmental factors

**Example Quality Improvements:**
- ❌ "Formal military script?" → ✅ "Formal military script indicating supply requisition"
- ❌ "Found in temple" → ✅ "Found buried beneath prayer mat remnants with emotional urgency in carving depth"

### Translation Context Alignment

Ensure translations reflect their archaeological settings:

**Military Contexts**: Use directive, precise language (signal, requisition, formation)
**Commercial Contexts**: Use transactional language (inspect, trade, evaluate)
**Domestic Contexts**: Use personal, practical language (tend, count, collect)
**Academic Contexts**: Use analytical language (study, observe, analyze)
**Ceremonial Contexts**: Use formal, ritual language (invoke, bless, purify)

## Technical Development Notes

### Flask Application Features

**Legacy Viewer** (`/viewer/`):
- Hot reload development server
- Markdown rendering with file navigation
- Individual file display with context preservation

**New Webapp** (`/webapp/`):
- Foldable table interface organized by difficulty
- Bulk loading with load_all_texts() function
- Level-based organization with visual headers
- Comprehensive site information display

### Docker Configuration

Current setup optimized for webapp deployment:
- Production-ready environment with proper requirements
- Automated dependency management
- Scalable containerization for web serving

### JSON Structure Validation

When editing source files, maintain strict structure:
```json
{
    "name": "Site Name",
    "context": "Archaeological and cultural background...",
    "texts": [
        {
            "name": "Text Name",
            "sasiran": "Sasiran language text following SOV grammar",
            "script": "𐊖𐊀 corresponding Lycian script representation", 
            "translation": "Contextually appropriate English translation",
            "notes": "Discovery context and archaeological significance"
        }
    ]
}
```

---

## Quick Start Commands for AI Assistants

### Essential Files to Read First

```bash
# Core language data
cat reference/dictionary.json        # Complete vocabulary with morpheme construction
cat reference/example_sentences.json # 20 sentences showing SOV patterns

# Technical setup  
cat viewer/README.md                # Legacy web application documentation
cat webapp/README.md                # New table webapp documentation
ls sources/                         # Available content for translation work
```

### For Development Work

```bash
# Legacy markdown viewer
cd viewer && python server.py       # Start Flask development server

# New table webapp
cd webapp && source venv/bin/activate && python app.py  # Start webapp with foldable tables

# Docker deployment (uses webapp)
docker-compose up                   # Full containerized environment
```

This provides complete context for translation work, content creation, language development, or technical modifications to the Sasiran language game system.

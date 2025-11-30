# Sasiran Text Viewer Web App

A simple Flask application for viewing Sasiran archaeological texts in a table format.

## Features

- Displays all texts from JSON files in the `../sources/` directory
- Shows only the "name", "script", and "notes" fields in a clean table
- Responsive design with archaeological theming
- Proper Lycian script rendering

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser to http://localhost:5000

## File Structure

```
webapp/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main table view template
└── README.md          # This file
```

## Development

The app automatically discovers all JSON files in the `../sources/` directory and extracts the text entries for display. No manual configuration needed - just add new JSON files to the sources directory and they'll appear in the table.
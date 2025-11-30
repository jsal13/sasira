#!/usr/bin/env python3
"""
Flask web application for displaying Sasiran archaeological texts.
Serves a table view of JSON content from the sources directory.
"""

import json
import os
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

def load_all_texts():
    """Load all texts from JSON files in the sources directory, grouped by difficulty level."""
    difficulty_groups = {'01': [], '02': []}
    sources_dir = Path(__file__).parent.parent / 'sources'
    
    for json_file in sorted(sources_dir.glob('**/*.json')):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Extract texts from the JSON structure
            texts = []
            for text in data.get('texts', []):
                texts.append({
                    'name': text.get('name', ''),
                    'script': text.get('script', ''),
                    'notes': text.get('notes', '')
                })
            
            # Determine difficulty level from path
            difficulty = json_file.parent.name
            if difficulty in difficulty_groups:
                difficulty_groups[difficulty].append({
                    'filename': json_file.name,
                    'filepath': str(json_file.relative_to(sources_dir)),
                    'site_name': data.get('name', json_file.stem.replace('_', ' ').title()),
                    'context': data.get('context', ''),
                    'texts': texts,
                    'text_count': len(texts)
                })
            
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error loading {json_file}: {e}")
    
    return difficulty_groups

@app.route('/')
def index():
    """Main page displaying all texts grouped by difficulty level in foldable tables."""
    difficulty_groups = load_all_texts()
    total_texts = sum(sum(file_data['text_count'] for file_data in files) for files in difficulty_groups.values())
    return render_template('index.html', difficulty_groups=difficulty_groups, total_texts=total_texts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
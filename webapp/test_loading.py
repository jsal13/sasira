#!/usr/bin/env python3
"""
Quick test script to verify JSON loading functionality.
"""

import json
import sys
from pathlib import Path

def test_json_loading():
    """Test that all JSON files can be loaded and contain expected structure."""
    sources_dir = Path(__file__).parent.parent / 'sources'
    
    print(f"Looking for JSON files in: {sources_dir}")
    print(f"Directory exists: {sources_dir.exists()}")
    
    total_texts = 0
    
    for json_file in sources_dir.glob('**/*.json'):
        print(f"\nProcessing: {json_file}")
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            texts = data.get('texts', [])
            print(f"  Found {len(texts)} texts")
            
            for i, text in enumerate(texts):
                name = text.get('name', 'Unknown')
                has_script = bool(text.get('script', ''))
                has_notes = bool(text.get('notes', ''))
                print(f"    Text {i+1}: {name} (script: {has_script}, notes: {has_notes})")
                total_texts += 1
                
        except Exception as e:
            print(f"  ERROR: {e}")
    
    print(f"\nTotal texts found across all files: {total_texts}")

if __name__ == '__main__':
    test_json_loading()
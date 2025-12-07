from pdfminer.high_level import extract_text
import json

def extract_text_by_page(path):
    text = extract_text(path)
    pages = text.split('\f')
    return pages

def pages_to_json(pages):
    return json.dumps([{"page": i+1, "text": p} for i,p in enumerate(pages)])

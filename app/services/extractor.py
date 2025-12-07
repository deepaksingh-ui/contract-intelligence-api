import re
from dateutil import parser as dateparser

def extract_parties(text):
    m = re.search(r"(This (Agreement|Contract).*?between\s+(.*?)(?:,|\n).*?and\s+(.*?)(?:,|\n))", text, re.IGNORECASE|re.DOTALL)
    if m:
        left = m.group(3).strip()
        right = m.group(4).strip()
        return [left, right]
    parties = re.findall(r"Party\s*[AB]:\s*(.+)", text)
    return parties

def extract_effective_date(text):
    m = re.search(r"(Effective Date[:\s]*|effective as of\s*)([A-Za-z0-9,\s]+)", text, re.IGNORECASE)
    if m:
        try:
            d = dateparser.parse(m.group(2), fuzzy=True)
            return d.date().isoformat()
        except:
            return m.group(2).strip()
    return None

def extract_governing_law(text):
    m = re.search(r"governed by the laws of\s*([A-Za-z ,]+)\.", text, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

def extract_auto_renewal(text):
    m = re.search(r"(auto-?renew|automatically renew).*?(notice.*?(\d+)\s*days)?", text, re.IGNORECASE|re.DOTALL)
    if m:
        days = m.group(3)
        return {"found": True, "notice_days": int(days) if days else None}
    return {"found": False}

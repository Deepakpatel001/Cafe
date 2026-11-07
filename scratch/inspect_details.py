import urllib.request
import re, sys

sys.stdout.reconfigure(encoding='utf-8')

req = urllib.request.Request('https://nexuscafe.in/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# Extract prices
prices = re.findall(r'([₹Rs]\s*\d+|\d+\s*/\s*hr)', html, re.I)
print("Prices found:", set(prices))

# Headings and cards
headings = re.findall(r'<(?:h[1-4]|div)[^>]*class="[^"]*(?:font-display|text-[\d\w]+)[^"]*"[^>]*>(.*?)</(?:h[1-4]|div)>', html, re.I | re.S)
for h in headings[:25]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean and len(clean) < 100:
        print("Heading/Text:", clean)

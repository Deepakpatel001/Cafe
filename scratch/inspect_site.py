import urllib.request
import re

req = urllib.request.Request('https://nexuscafe.in/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print(f"Page length: {len(html)} bytes")
        
        # Title
        m = re.search(r'<title>(.*?)</title>', html, re.I)
        if m: print("Title:", m.group(1).strip())
        
        # Meta description
        m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.I)
        if m: print("Meta description:", m.group(1).strip())
        
        # Fonts
        fonts = re.findall(r'https://fonts\.[^"\'\s)]+', html)
        print("Google Fonts:", list(set(fonts)))
        
        # Stylesheets / CSS
        css_links = re.findall(r'<link[^>]*href=["\']([^"\']+\.css[^"\']*)["\']', html, re.I)
        print("CSS links:", css_links[:5])
        
        # Headings
        headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html, re.I | re.S)
        clean_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings if h.strip()]
        print("Headings:", clean_headings[:15])
        
        # Colors / inline styles or key classes
        classes = list(set(re.findall(r'class=["\']([^"\']+)["\']', html)))
        print("Sample classes:", classes[:10])
        
        # Colors found in text (hex)
        hex_colors = list(set(re.findall(r'#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b', html)))
        print("Sample hex colors:", hex_colors[:15])

        # Text sample
        clean_text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.I|re.S)
        clean_text = re.sub(r'<style[^>]*>.*?</style>', '', clean_text, flags=re.I|re.S)
        clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()
        print("\nClean Text Sample (1000 chars):")
        print(clean_text[:1000])

except Exception as e:
    print("Error fetching site:", e)

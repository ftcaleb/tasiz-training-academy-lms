import re

filepath = r'c:\Users\brend\Desktop\build\tasez-training-academy\TASEZ Student Portal.dc.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Comprehensive Green Hex Map -> Melsoft Neutral/Navy/Blue replacements
green_map = {
    '#3DC98A': 'var(--accent-blue)',
    '#178A5C': 'var(--accent-navy)',
    '#14532D': 'var(--accent-navy-dark)',
    '#147A50': 'var(--accent-navy)',
    '#8FE3BD': '#94A3B8',
    '#BFE5D2': '#E5E7EB',
    '#E7F5EE': '#F4F7FC',
    '#F3FBF7': '#FFFFFF',
    'rgba(23,138,92,.22)': 'transparent',
    'rgba(61,201,138,0.4)': 'var(--border-color)',
    'rgba(61,201,138,0.25)': 'none',
    'rgba(61,201,138,0.16)': 'var(--accent-navy)',
    'rgba(61,201,138,0.35)': 'var(--border-color)',
    'rgba(61,201,138,0.15)': 'none',
    'rgba(61,201,138,0.2)': 'var(--border-color)',
}

for k, v in green_map.items():
    html = html.replace(k, v)

# Purge any remaining box-shadow declarations
html = re.sub(r'box-shadow\s*:\s*[^;\"]+;?', 'box-shadow: none;', html)

# Purge glow occurrences
html = html.replace('glow', '')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print('Purged all remaining green and shadow declarations.')

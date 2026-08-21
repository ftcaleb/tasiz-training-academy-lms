import re

filepath = r'c:\Users\brend\Desktop\build\tasez-training-academy\TASEZ Student Portal.dc.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace hardcoded dark theme colors outside :root
replacements = [
    # Dark card bgs
    ('background:#051322;', 'background:var(--bg-base);'),
    ('background:#081F38;', 'background:var(--bg-card);'),
    ('background:#0B2C4D;', 'background:var(--bg-card);'),
    ('background:#0E7490;', 'background:var(--accent-blue);'),
    ('background:#123E6B;', 'background:var(--bg-base);'),
    ('background:#1B4F8A;', 'background:var(--accent-navy);'),
    ('background:#1E3A5F;', 'background:var(--border-color);'),
    ('background:#22D3EE;', 'background:var(--accent-blue);'),
    ('background:#38BDF8;', 'background:var(--accent-blue);'),
    ('background:#7DD3FC;', 'background:var(--bg-base);'),
    ('background:#9F1239;', 'background:var(--status-red);'),
    ('background:#B4232A;', 'background:var(--status-red);'),
    ('background:#B45309;', 'background:var(--status-amber);'),
    ('background:#F2C4CB;', 'background:var(--status-red-bg);'),
    ('background:#FDE68A;', 'background:var(--status-amber-bg);'),

    # Text colors
    ('color:#E2E8F0;', 'color:var(--text-primary);'),
    ('color:#E3E8EF;', 'color:var(--text-primary);'),
    ('color:#EEF1F5;', 'color:var(--text-primary);'),
    ('color:#F8FAFC;', 'color:var(--text-primary);'),
    ('color:#5B6B7C;', 'color:var(--text-secondary);'),
    ('color:#64748B;', 'color:var(--text-secondary);'),
    ('color:#7A8BA0;', 'color:var(--text-secondary);'),
    ('color:#94A3B8;', 'color:var(--text-tertiary);'),
    ('color:#A5B1BF;', 'color:var(--text-tertiary);'),
    ('color:#CBD5E1;', 'color:var(--text-tertiary);'),
]

for old, new in replacements:
    html = html.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print('Cleaned up hardcoded hex values outside :root.')

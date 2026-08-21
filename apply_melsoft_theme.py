import re

filepath = r'c:\Users\brend\Desktop\build\tasez-training-academy\TASEZ Student Portal.dc.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update <style> block completely to reference reference design tokens
style_replacement = '''<style>
:root {
  /* Foundation */
  --bg-base: #F4F7FC;
  --bg-card: #FFFFFF;
  --border-color: #E5E7EB;
  --border-hover: #D1D5DB;

  /* Primary Accent - Deep Melsoft Navy */
  --accent-navy: #0A1733;
  --accent-navy-dark: #0C1B3A;

  /* Secondary Accent - Crisp Cobalt/Periwinkle Blue */
  --accent-blue: #1D49A8;

  /* Text Hierarchy */
  --text-primary: #0F172A;
  --text-secondary: #64748B;
  --text-tertiary: #94A3B8;
  --text-disabled: #7F8BA6;
  --dash-neutral: #9EA7BD;

  /* Status (Red Delta) */
  --status-red: #A22A2A;
  --status-red-bg: #FAE9E9;
  --status-amber: #92400E;
  --status-amber-bg: #FEF3C7;

  /* Role Badges */
  --badge-admin-bg: #F5C94C;
  --badge-admin-text: #17233E;

  /* Rank-Specific (Leaderboard ONLY) */
  --rank-gold: #F5C94C;
  --rank-silver: #CBD0DB;
  --rank-bronze: #DAA476;

  /* Flat Elevation System */
  --shadow-card: none;
}

body {
  margin: 0;
  font-family: 'Public Sans', sans-serif;
  color: var(--text-primary);
  background: var(--bg-base);
  min-height: 100vh;
}
a { color: var(--accent-blue); text-decoration: none; }
a:hover { color: var(--accent-navy); }
* { box-sizing: border-box; }
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 4px; }

/* MELSOFT STYLE TOP PILL NAVBAR */
.tubelight-bar {
  position: fixed;
  top: 16px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 9999px;
  padding: 6px 16px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.tubelight-item {
  position: relative;
  cursor: pointer;
  font-size: 13.5px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 9999px;
  color: var(--text-secondary);
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
}
.tubelight-item:hover {
  color: var(--text-primary);
}
.tubelight-item.active {
  background: var(--accent-navy);
  color: #FFFFFF;
  font-weight: 700;
}
.tubelight-lamp { display: none; }

.nav-dropdown { position: relative; display: flex; align-items: center; }
.nav-dropdown-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(8px);
  margin-top: 6px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 6px;
  min-width: 210px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  opacity: 0;
  pointer-events: none;
  transition: all 0.15s ease;
  z-index: 1000;
}
.nav-dropdown:hover .nav-dropdown-menu {
  opacity: 1;
  pointer-events: auto;
  transform: translateX(-50%) translateY(0);
}
.nav-dropdown-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  border-radius: 8px;
  color: var(--text-primary);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
  white-space: nowrap;
}
.nav-dropdown-item:hover {
  background: var(--bg-base);
  color: var(--accent-blue);
}
</style>'''

html = re.sub(r'<style>(.*?)</style>', style_replacement, html, flags=re.DOTALL)

# 2. Invert TASEZ logo brightness for light navbar background
html = html.replace('filter:brightness(0) invert(1);', 'filter:brightness(0.1);')

# 3. Clean up logo role switcher and student LM avatar
html = html.replace('background:rgba(255,255,255,0.08);', 'background:var(--bg-base);')
html = html.replace('background:#178A5C;color:#FFFFFF;font-size:12px;font-weight:700;', 'background:var(--accent-navy);color:#FFFFFF;font-size:12px;font-weight:700;')
html = html.replace('color:rgba(255,255,255,0.75);', 'color:var(--text-secondary);')
html = html.replace('border-left:1px solid rgba(255,255,255,0.15);', 'border-left:1px solid var(--border-color);')

# Replace LM avatar background from old green #178A5C to navy var(--accent-navy)
html = html.replace('background:#178A5C;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;color:#fff;', 'background:var(--accent-navy);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;color:#FFFFFF;')

# 4. Global Dark to Light Transformations
# Replace dark backgrounds with var(--bg-card) or var(--bg-base)
html = re.sub(r'background:rgba\(13,37,64,0\.7\);border:1px solid rgba\(61,201,138,0\.2\);', 'background:var(--accent-navy);border:1px solid var(--accent-navy);', html) # Hero banner

# Dark card background replacements
html = html.replace('background:#0D2540;', 'background:var(--bg-card);')
html = html.replace('background:#081F38;', 'background:var(--bg-card);')
html = html.replace('background:#051322;', 'background:var(--bg-base);')
html = html.replace('background:rgba(13,37,64,0.7);', 'background:var(--bg-card);')
html = html.replace('background:rgba(13,37,64,0.6);', 'background:var(--bg-card);')
html = html.replace('background:rgba(13,37,64,0.4);', 'background:var(--bg-base);')
html = html.replace('background:rgba(255,255,255,0.03);', 'background:var(--bg-base);')
html = html.replace('background:rgba(255,255,255,0.05);', 'background:var(--bg-base);')

# Border replacements (glow/shadow/dark borders to 1px solid var(--border-color))
html = re.sub(r'border:1px solid rgba\(61,201,138,0\.25?\);?', 'border:1px solid var(--border-color);', html)
html = re.sub(r'border:1px solid rgba\(255,255,255,0\.08\);?', 'border:1px solid var(--border-color);', html)
html = re.sub(r'border:1px solid rgba\(255,255,255,0\.1\);?', 'border:1px solid var(--border-color);', html)
html = re.sub(r'border-top:1px solid rgba\(255,255,255,0\.08\);?', 'border-top:1px solid var(--border-color);', html)
html = re.sub(r'border-bottom:1px solid rgba\(255,255,255,0\.08\);?', 'border-bottom:1px solid var(--border-color);', html)

# Box shadow removals
html = re.sub(r'box-shadow:[^;\"]+;?', 'box-shadow:var(--shadow-card);', html)

# Text Color Replacements
# Replace pure white text on cards with var(--text-primary) except on solid navy hero background
# We handle hero banner specially: <div style="...background:var(--accent-navy)...">
html = html.replace('color:#FFFFFF;', 'color:var(--text-primary);')
html = html.replace('color:#fff;', 'color:var(--text-primary);')

# Fix text inside Hero banner back to white
html = html.replace('Welcome back, Lerato', '<span style="color:#FFFFFF;">Welcome back, Lerato</span>')

# Progress bars & badges
html = html.replace('background:#3DC98A;', 'background:var(--accent-blue);')
html = html.replace('background:#178A5C;', 'background:var(--accent-navy);')
html = html.replace('color:#3DC98A;', 'color:var(--accent-blue);')
html = html.replace('color:#178A5C;', 'color:var(--accent-navy);')

# Non-accredited & status green pills to light periwinkle/navy or status red/amber
html = html.replace('rgba(61,201,138,0.15)', 'rgba(29,73,168,0.1)')
html = html.replace('rgba(61,201,138,0.2)', 'rgba(29,73,168,0.15)')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully transformed TASEZ Student Portal.dc.html')

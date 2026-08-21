#!/usr/bin/env python3
"""
Comprehensive Dark Theme Polish for TASEZ Student Portal & Admin Console.
1. Add tasiz-nobg-logo.png to Navbar
2. Eliminate all remaining white/light callout backgrounds (#FBFCFE, #F3FBF7, #E8F0FB, #FFF8EB, #FDECEC, etc.)
3. Upgrade Transcript & Certificate cards to dark glass containers with high-contrast text.
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\Scope answers pending"

# ── LOGO INSERTION ────────────────────────────────────────────────────────────
NAVBAR_LOGO_HTML = '<div style="display:flex;align-items:center;gap:10px;flex-shrink:0;"><img src="./tasiz-nobg-logo.png" alt="TASEZ" style="height:28px;filter:brightness(0) invert(1);display:block;"><div style="font-family:Archivo;font-weight:700;font-size:17px;letter-spacing:.02em;">TASEZ <span style="color:#3DC98A;">TTA</span></div></div>'
OLD_NAVBAR_TEXT = '<div style="font-family:Archivo;font-weight:700;font-size:17px;letter-spacing:.02em;flex-shrink:0;">TASEZ <span style="color:#3DC98A;">TTA</span></div>'

for fname in ["TASEZ Student Portal.dc.html", "TASEZ Admin Console.dc.html"]:
    fpath = os.path.join(DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Add logo to Navbar if not present
    if "tasiz-nobg-logo.png" not in c:
        c = c.replace(OLD_NAVBAR_TEXT, NAVBAR_LOGO_HTML)

    # 2. Fix Transcript Paper background
    c = c.replace('background:#FBFCFE;', 'background:rgba(8,25,45,0.85);border:1px solid rgba(61,201,138,0.25);border-radius:12px;')
    c = c.replace('background: #FBFCFE;', 'background:rgba(8,25,45,0.85);border:1px solid rgba(61,201,138,0.25);border-radius:12px;')
    c = c.replace('border-bottom:2px solid #0B2C4D;', 'border-bottom:2px solid rgba(61,201,138,0.4);')
    c = c.replace('border-bottom:1.5px solid #0B2C4D;', 'border-bottom:1.5px solid rgba(61,201,138,0.4);')

    # 3. Fix Issued Certificate card light background
    c = c.replace('border:1px solid #BFE5D2;background:#F3FBF7;', 'border:1px solid rgba(61,201,138,0.35);background:rgba(23,138,92,0.14);')
    c = c.replace('color:#147A50;', 'color:#3DC98A;')
    c = c.replace('color: #147A50;', 'color: #3DC98A;')
    c = c.replace('background:#E7F5EE;color:#147A50;', 'background:rgba(61,201,138,0.16);color:#3DC98A;')

    # 4. Fix Warning / Lock Alert box light backgrounds (#FFF8EB, #F3D9A4)
    c = c.replace('background:#FFF8EB;border:1px solid #F3D9A4;', 'background:rgba(245,158,11,0.12);border:1px solid rgba(245,158,11,0.3);')
    c = c.replace('color:#92400E;', 'color:#FBBF24;')
    c = c.replace('color:#7C5A1E;', 'color:#FDE68A;')

    # 5. Fix Info callouts (#E8F0FB, #C9DCF2)
    c = c.replace('background:#E8F0FB;border:1px solid #C9DCF2;', 'background:rgba(56,189,248,0.12);border:1px solid rgba(56,189,248,0.3);')
    c = c.replace('color:#123E6B;', 'color:#7DD3FC;')

    # 6. Fix Error callouts (#FDECEC)
    c = c.replace('background:#FDECEC;', 'background:rgba(239,68,68,0.12);border:1px solid rgba(239,68,68,0.3);')
    c = c.replace('color:#9F1239;', 'color:#FCA5A5;')

    # 7. Fix progress bar tracks (#EEF1F5)
    c = c.replace('background:#EEF1F5;', 'background:rgba(255,255,255,0.08);')

    # 8. Fix task text color (#3D4E61)
    c = c.replace('color:#3D4E61;', 'color:#CBD5E1;')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)

print("Comprehensive Dark Theme Polish Complete.")

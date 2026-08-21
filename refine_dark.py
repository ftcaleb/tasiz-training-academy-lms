#!/usr/bin/env python3
"""
Refine links, borders, inputs, and text contrast in Dark Mode Glassmorphism.
"""
import os

DIR = r"c:\Users\brend\Desktop\build\Scope answers pending"

for fname in ["TASEZ Student Portal.dc.html", "TASEZ Admin Console.dc.html"]:
    fpath = os.path.join(DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # Link colors on dark background
    c = c.replace('color:#1B4F8A;', 'color:#3DC98A;')
    c = c.replace('color: #1B4F8A;', 'color: #3DC98A;')
    
    # Form input backgrounds and borders on dark background
    c = c.replace('background:#F8FAFC;', 'background:rgba(13,37,64,0.65);color:#FFFFFF;')
    c = c.replace('border:1px solid #C7D0DB;', 'border:1px solid rgba(61,201,138,0.25);')
    c = c.replace('border:1px solid #E5E7EB;', 'border:1px solid rgba(61,201,138,0.18);')
    c = c.replace('border:1px solid #E3E8EF;', 'border:1px solid rgba(61,201,138,0.18);')
    
    # Table headers and borders
    c = c.replace('background:#f9fafb;', 'background:rgba(13,37,64,0.8);')
    c = c.replace('background:#F9FAFB;', 'background:rgba(13,37,64,0.8);')
    c = c.replace('border-bottom:1px solid #E5E7EB;', 'border-bottom:1px solid rgba(255,255,255,0.08);')
    c = c.replace('border-bottom:1px solid #EEF1F5;', 'border-bottom:1px solid rgba(255,255,255,0.08);')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)

print("Refinements applied.")

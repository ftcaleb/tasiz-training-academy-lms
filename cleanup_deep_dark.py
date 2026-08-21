#!/usr/bin/env python3
"""
Deep Dark Theme Cleanup & High-Contrast Polish
Target: c:\\Users\\brend\\Desktop\\build\\Scope answers pending\\
"""
import os

DIR = r"c:\Users\brend\Desktop\build\Scope answers pending"

for fname in ["TASEZ Student Portal.dc.html", "TASEZ Admin Console.dc.html"]:
    fpath = os.path.join(DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Pipeline container light backgrounds
    c = c.replace('background:#EAEFF5;', 'background:rgba(13,37,64,0.6);border:1px solid rgba(61,201,138,0.2);')

    # 2. Pill tags with light blue/green backgrounds (#E8F0FB, #E7F5EE, #ECFAFD)
    c = c.replace('background:#E8F0FB;color:#3DC98A;', 'background:rgba(61,201,138,0.16);color:#3DC98A;border:1px solid rgba(61,201,138,0.3);')
    c = c.replace('background:#E8F0FB;', 'background:rgba(61,201,138,0.16);color:#3DC98A;')
    c = c.replace('background:#E7F5EE;', 'background:rgba(61,201,138,0.16);color:#3DC98A;')
    c = c.replace('background:#ECFAFD;color:#0E7490;', 'background:rgba(14,116,144,0.2);color:#38BDF8;')

    # 3. Dashed file drop zone border (#C7D0DB)
    c = c.replace('border:2px dashed #C7D0DB;', 'border:2px dashed rgba(61,201,138,0.35);background:rgba(13,37,64,0.5);')

    # 4. Map box light background (#EDF3F9, #DCE6F0)
    c = c.replace('background:#EDF3F9;', 'background:rgba(8,25,45,0.9);border:1px solid rgba(61,201,138,0.2);')
    c = c.replace('#DCE6F0', 'rgba(255,255,255,0.06)')

    # 5. Buttons: replace dark navy (#0B2C4D) buttons with emerald / translucent green
    c = c.replace('background:#0B2C4D;color:#fff;', 'background:#178A5C;color:#FFFFFF;')
    c = c.replace('background:#0B2C4D;color:#fff', 'background:#178A5C;color:#FFFFFF')

    # 6. Border cleanups
    c = c.replace('border:1px solid #E7EBF1;', '')
    c = c.replace('border-bottom:1px solid #F1F4F8;', 'border-bottom:1px solid rgba(255,255,255,0.08);')
    c = c.replace('border-top:1px solid #EEF1F5;', 'border-top:1px solid rgba(255,255,255,0.08);')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)

print("Deep dark theme cleanup complete.")

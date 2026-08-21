#!/usr/bin/env python3
"""
Redesign TASEZ Student Portal & Admin Console to Full Midnight Navy & Emerald Glassmorphism Dark Mode.
Source directory: c:\\Users\\brend\\Desktop\\build\\Scope answers pending\\
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\Scope answers pending"

# 1. Redesign Student Portal CSS & Theme
student_path = os.path.join(DIR, "TASEZ Student Portal.dc.html")
with open(student_path, "r", encoding="utf-8") as f:
    sp_content = f.read()

# Replace body background and base colors in helmet <style>
sp_content = re.sub(
    r"body\{margin:0;font-family:'Public Sans',sans-serif;color:#152435;background:radial-gradient\([^)]+\),radial-gradient\([^)]+\),#F4F6F9;\}",
    """body{margin:0;font-family:'Public Sans',sans-serif;color:#E2E8F0;background:#051322;background-image:radial-gradient(1200px 600px at 80% -10%,rgba(23,138,92,.18),transparent 60%),radial-gradient(1000px 500px at -10% 20%,rgba(14,58,92,.3),transparent 55%),radial-gradient(rgba(255,255,255,0.05) 1px,transparent 1px);background-size:100% 100%,100% 100%,24px 24px;}
a{color:#3DC98A;text-decoration:none;} a:hover{color:#8FE3BD;}
*{box-sizing:border-box;}
::-webkit-scrollbar{width:10px;height:10px;} ::-webkit-scrollbar-thumb{background:#1E3A5F;border-radius:6px;}
.tta-card{background:linear-gradient(180deg,rgba(13,37,64,.8),rgba(8,25,45,.9));backdrop-filter:blur(12px);border:1px solid rgba(61,201,138,.18);border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.36);color:#FFFFFF;transition:all .2s ease;}
.tta-card:hover{border-color:rgba(61,201,138,.45);box-shadow:0 0 24px rgba(61,201,138,.18);}""",
    sp_content
)

# Convert light cards to dark glass cards
sp_content = sp_content.replace(
    'background:linear-gradient(180deg,#FFFFFF,#FBFDFF);border:1px solid #E3E8EF;border-radius:16px;box-shadow:0 1px 2px rgba(11,44,77,.04),0 12px 28px -20px rgba(11,44,77,.18);',
    'background:linear-gradient(180deg,rgba(13,37,64,.8),rgba(8,25,45,.9));backdrop-filter:blur(12px);border:1px solid rgba(61,201,138,.18);border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.36);color:#FFFFFF;'
)

# Replace headings color from dark navy (#0B2C4D) to pure white (#FFFFFF)
sp_content = sp_content.replace('color:#0B2C4D;', 'color:#FFFFFF;')
sp_content = sp_content.replace('fill="#0B2C4D"', 'fill="#FFFFFF"')
sp_content = sp_content.replace('stroke="#EEF1F5"', 'stroke="rgba(255,255,255,0.08)"')

# Replace subtitle text color from #5B6B7C to #94A3B8
sp_content = sp_content.replace('color:#5B6B7C;', 'color:#94A3B8;')
sp_content = sp_content.replace('color:#152435;', 'color:#E2E8F0;')
sp_content = sp_content.replace('color:#7A8BA0;', 'color:#64748B;')
sp_content = sp_content.replace('border:1px solid #E3E8EF;', 'border:1px solid rgba(61,201,138,0.2);')
sp_content = sp_content.replace('background:#fff;', 'background:rgba(13,37,64,0.7);')
sp_content = sp_content.replace('background:#FFFFFF;', 'background:rgba(13,37,64,0.7);')

with open(student_path, "w", encoding="utf-8") as f:
    f.write(sp_content)

print("Student Portal updated to Dark Glassmorphism.")

# 2. Redesign Admin Console CSS & Theme
admin_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
with open(admin_path, "r", encoding="utf-8") as f:
    ac_content = f.read()

ac_content = re.sub(
    r"body\{margin:0;font-family:'Public Sans',sans-serif;color:#152435;background:radial-gradient\([^)]+\),radial-gradient\([^)]+\),#F4F6F9;\}",
    """body{margin:0;font-family:'Public Sans',sans-serif;color:#E2E8F0;background:#051322;background-image:radial-gradient(1200px 600px at 80% -10%,rgba(23,138,92,.18),transparent 60%),radial-gradient(1000px 500px at -10% 20%,rgba(14,58,92,.3),transparent 55%),radial-gradient(rgba(255,255,255,0.05) 1px,transparent 1px);background-size:100% 100%,100% 100%,24px 24px;}
a{color:#3DC98A;text-decoration:none;} a:hover{color:#8FE3BD;}
*{box-sizing:border-box;}
::-webkit-scrollbar{width:10px;height:10px;} ::-webkit-scrollbar-thumb{background:#1E3A5F;border-radius:6px;}
.tta-card{background:linear-gradient(180deg,rgba(13,37,64,.8),rgba(8,25,45,.9));backdrop-filter:blur(12px);border:1px solid rgba(61,201,138,.18);border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.36);color:#FFFFFF;transition:all .2s ease;}
.tta-card:hover{border-color:rgba(61,201,138,.45);box-shadow:0 0 24px rgba(61,201,138,.18);}""",
    ac_content
)

ac_content = ac_content.replace(
    'background:linear-gradient(180deg,#FFFFFF,#FBFDFF);border:1px solid #E3E8EF;border-radius:16px;box-shadow:0 1px 2px rgba(11,44,77,.04),0 12px 28px -20px rgba(11,44,77,.18);',
    'background:linear-gradient(180deg,rgba(13,37,64,.8),rgba(8,25,45,.9));backdrop-filter:blur(12px);border:1px solid rgba(61,201,138,.18);border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.36);color:#FFFFFF;'
)

ac_content = ac_content.replace('color:#0B2C4D;', 'color:#FFFFFF;')
ac_content = ac_content.replace('color:#5B6B7C;', 'color:#94A3B8;')
ac_content = ac_content.replace('color:#152435;', 'color:#E2E8F0;')
ac_content = ac_content.replace('color:#7A8BA0;', 'color:#64748B;')
ac_content = ac_content.replace('border:1px solid #E3E8EF;', 'border:1px solid rgba(61,201,138,0.2);')
ac_content = ac_content.replace('background:#fff;', 'background:rgba(13,37,64,0.7);')
ac_content = ac_content.replace('background:#FFFFFF;', 'background:rgba(13,37,64,0.7);')

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(ac_content)

print("Admin Console updated to Dark Glassmorphism.")

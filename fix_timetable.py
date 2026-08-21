#!/usr/bin/env python3
"""
Fix Timetable event cards and month grid colors in TASEZ Student Portal.
Target: c:\\Users\\brend\\Desktop\\build\\Scope answers pending\\TASEZ Student Portal.dc.html
"""
import os, re

fpath = r"c:\Users\brend\Desktop\build\Scope answers pending\TASEZ Student Portal.dc.html"

with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update JS tCol definition to dark glass backgrounds & vibrant accent colors
old_tCol = "const tCol = {Class:{bar:'#1B4F8A',bg:'#EFF5FC'},Practical:{bar:'#178A5C',bg:'#F0FAF4'},Workplace:{bar:'#0B2C4D',bg:'#EEF1F5'},Virtual:{bar:'#0E7490',bg:'#ECFAFD'},Assessment:{bar:'#B45309',bg:'#FFF8EB'},Moderation:{bar:'#9F1239',bg:'#FDF0F3'}};"
new_tCol = "const tCol = {Class:{bar:'#38BDF8',bg:'rgba(56,189,248,0.14)'},Practical:{bar:'#3DC98A',bg:'rgba(61,201,138,0.14)'},Workplace:{bar:'#C084FC',bg:'rgba(192,132,252,0.14)'},Virtual:{bar:'#22D3EE',bg:'rgba(34,211,238,0.14)'},Assessment:{bar:'#FBBF24',bg:'rgba(245,158,11,0.14)'},Moderation:{bar:'#FCA5A5',bg:'rgba(239,68,68,0.14)'}};"

c = c.replace(old_tCol, new_tCol)

# 2. Update ttCells month grid cells background and borders
old_ttCells = "const ttCells = [...Array(5).fill(null),...Array.from({length:31},(_,i)=>i+1)].map(d=>({d:d||'', dots:(d&&monthEv[d]||[]).map(c=>({c})), border:d===20?'#178A5C':'#EEF1F5', bg:d?'#fff':'#FBFCFE'}));"
new_ttCells = "const ttCells = [...Array(5).fill(null),...Array.from({length:31},(_,i)=>i+1)].map(d=>({d:d||'', dots:(d&&monthEv[d]||[]).map(c=>({c})), border:d===20?'#3DC98A':'rgba(255,255,255,0.08)', bg:d?'rgba(13,37,64,0.65)':'transparent'}));"

c = c.replace(old_ttCells, new_ttCells)

# 3. Update Timetable HTML event card styling for crisp white titles and light cyan meta text
old_event_card = """<div style="background:{{ s.bg }};border-left:3px solid {{ s.bar }};border-radius:8px;padding:9px 10px;">
                      <div style="font-size:10.5px;font-weight:700;color:{{ s.bar }};">{{ s.time }} · {{ s.type }}</div>
                      <div style="font-size:12px;font-weight:600;margin-top:3px;line-height:1.35;">{{ s.title }}</div>
                      <div style="font-size:10.5px;color:#64748B;margin-top:3px;">{{ s.meta }}</div>
                    </div>"""

new_event_card = """<div style="background:{{ s.bg }};border-left:3px solid {{ s.bar }};border-radius:8px;padding:9px 10px;border:1px solid rgba(255,255,255,0.06);">
                      <div style="font-size:10.5px;font-weight:700;color:{{ s.bar }};">{{ s.time }} · {{ s.type }}</div>
                      <div style="font-size:12px;font-weight:600;margin-top:3px;line-height:1.35;color:#FFFFFF;">{{ s.title }}</div>
                      <div style="font-size:10.5px;color:#94A3B8;margin-top:3px;">{{ s.meta }}</div>
                    </div>"""

c = c.replace(old_event_card, new_event_card)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

print("Timetable event cards and month grid updated to Dark Glassmorphism.")

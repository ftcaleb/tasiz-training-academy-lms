#!/usr/bin/env python3
"""
Sync TASEZ Admin Console (standalone).html with TASEZ Admin Console.dc.html
so that opening either file in any browser or IDE preview executes the live dark Tubelight navbar app.
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\
"""
import os

DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"
src_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
standalone_path = os.path.join(DIR, "TASEZ Admin Console (standalone).html")

with open(src_path, "r", encoding="utf-8") as f:
    src_content = f.read()

with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(src_content)

print("Standalone HTML file successfully updated and synced with TASEZ Admin Console.dc.html.")

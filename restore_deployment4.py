#!/usr/bin/env python3
"""
Restore local project files directly from Deployment 4 (https://tasez-training-academy.vercel.app)
Downloads exact byte-for-byte build outputs from Vercel and overwrites local files completely.
"""
import urllib.request
import os

BASE_URL = "https://tasez-training-academy.vercel.app/"
DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"

files_to_restore = [
    "TASEZ Student Portal.dc.html",
    "TASEZ Admin Console.dc.html",
    "support.js",
    "index.html",
    "tasiz-nobg-logo.png"
]

print("Restoring exact files from Deployment 4 (https://tasez-training-academy.vercel.app)...")

for filename in files_to_restore:
    url = BASE_URL + urllib.parse.quote(filename)
    dest = os.path.join(DIR, filename)
    print(f"Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(dest, "wb") as f:
                f.write(data)
            print(f"Successfully restored {filename} ({len(data)} bytes).")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# Also sync TASEZ Admin Console (standalone).html with exact restored TASEZ Admin Console.dc.html
admin_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
standalone_path = os.path.join(DIR, "TASEZ Admin Console (standalone).html")

if os.path.exists(admin_path):
    with open(admin_path, "rb") as sf, open(standalone_path, "wb") as df:
        df.write(sf.read())
    print("Successfully synced TASEZ Admin Console (standalone).html with restored Admin Console.")

print("Restoration from Deployment 4 complete.")

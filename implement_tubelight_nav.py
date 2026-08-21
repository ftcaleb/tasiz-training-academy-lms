#!/usr/bin/env python3
"""
Implement Tubelight Floating Navbar with Logically Grouped Dropdowns & Active Lamp Glow.
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"

# ── STUDENT PORTAL TUBELIGHT NAVBAR ───────────────────────────────────────────
student_path = os.path.join(DIR, "TASEZ Student Portal.dc.html")
with open(student_path, "r", encoding="utf-8") as f:
    sp = f.read()

# Add Tubelight CSS to <style>
tubelight_css = """
  /* TUBELIGHT FLOATING NAVBAR STYLES */
  .tubelight-bar { position:fixed; top:18px; left:50%; transform:translateX(-50%); z-index:999; background:rgba(8,25,45,0.85); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border:1px solid rgba(61,201,138,0.35); border-radius:9999px; padding:5px 12px; box-shadow:0 16px 40px rgba(0,0,0,0.6),0 0 24px rgba(61,201,138,0.2); display:flex; align-items:center; gap:8px; }
  .tubelight-item { position:relative; cursor:pointer; font-size:13px; font-weight:600; padding:8px 16px; border-radius:9999px; color:rgba(255,255,255,0.8); transition:all 0.2s ease; display:flex; align-items:center; gap:6px; white-space:nowrap; }
  .tubelight-item:hover { color:#3DC98A; }
  .tubelight-item.active { background:rgba(61,201,138,0.16); color:#3DC98A; font-weight:700; }
  .tubelight-lamp { position:absolute; top:-6px; left:50%; transform:translateX(-50%); width:30px; height:3.5px; background:#3DC98A; border-radius:9999px; box-shadow:0 -2px 10px #3DC98A,0 0 16px #3DC98A,0 0 24px rgba(61,201,138,0.8); }
  
  .nav-dropdown { position:relative; display:flex; align-items:center; }
  .nav-dropdown-menu { position:absolute; top:100%; left:50%; transform:translateX(-50%) translateY(12px); margin-top:8px; background:rgba(8,25,45,0.95); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border:1px solid rgba(61,201,138,0.35); border-radius:18px; padding:8px; box-shadow:0 20px 48px rgba(0,0,0,0.7),0 0 20px rgba(61,201,138,0.15); min-width:210px; display:flex; flex-direction:column; gap:4px; opacity:0; pointer-events:none; transition:all 0.2s cubic-bezier(0.16, 1, 0.3, 1); z-index:1000; }
  .nav-dropdown:hover .nav-dropdown-menu { opacity:1; pointer-events:auto; transform:translateX(-50%) translateY(0); }
  .nav-dropdown-item { display:flex; align-items:center; gap:10px; padding:9px 14px; border-radius:10px; color:#E2E8F0; font-size:13px; font-weight:600; cursor:pointer; transition:all 0.15s; white-space:nowrap; }
  .nav-dropdown-item:hover { background:rgba(61,201,138,0.16); color:#3DC98A; }
"""

sp = sp.replace("::-webkit-scrollbar{width:10px;height:10px;} ::-webkit-scrollbar-thumb{background:#C7D0DB;border-radius:6px;}", "::-webkit-scrollbar{width:10px;height:10px;} ::-webkit-scrollbar-thumb{background:#1E3A5F;border-radius:6px;}\n" + tubelight_css)

# Update padding-top on content container so fixed navbar doesn't cover top titles
sp = sp.replace('<div style="flex:1;padding:32px 28px 48px;">', '<div style="flex:1;padding:84px 28px 48px;">')

# Replace old Navbar HTML with Tubelight Navbar & Dropdowns
old_sp_navbar_pattern = re.compile(r'<!-- NAVBAR -->.*?<!-- CONTENT -->', re.DOTALL)

new_sp_navbar_html = """<!-- TUBELIGHT FLOATING NAVBAR -->
  <div class="tubelight-bar">
    <!-- Logo -->
    <a href="#" onClick="{{ () => this.go('dashboard') }}" style="display:flex;align-items:center;padding:0 6px;cursor:pointer;">
      <img src="./tasiz-nobg-logo.png" alt="TASEZ" style="height:28px;filter:brightness(0) invert(1);display:block;">
    </a>

    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ sDash ? 'active' : '' }}" onClick="{{ () => this.go('dashboard') }}">
      <sc-if value="{{ sDash }}"><div class="tubelight-lamp"></div></sc-if>
      Overview
    </div>

    <!-- Item 2: Academics Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (sCourse || sProg || sTime || sNon || sModule || sPractical || sLogbook || sQuiz || sQResults || sExam) ? 'active' : '' }}">
        <sc-if value="{{ sCourse || sProg || sTime || sNon || sModule || sPractical || sLogbook || sQuiz || sQResults || sExam }}"><div class="tubelight-lamp"></div></sc-if>
        Academics <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ () => this.go('course') }}">📚 My Coursework</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('prog') }}">📈 Progress &amp; Results</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('time') }}">📅 Timetable &amp; Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('non') }}">🎓 Non-Accredited Events</div>
      </div>
    </div>

    <!-- Item 3: Records & Finance Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (sTrans || sFin) ? 'active' : '' }}">
        <sc-if value="{{ sTrans || sFin }}"><div class="tubelight-lamp"></div></sc-if>
        Records &amp; Finance <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ () => this.go('trans') }}">📄 Academic Transcripts</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('fin') }}">💳 Statements &amp; Fees</div>
      </div>
    </div>

    <!-- Role Switcher & Avatar -->
    <div style="display:flex;align-items:center;gap:6px;margin-left:8px;padding-left:8px;border-left:1px solid rgba(255,255,255,0.12);">
      <div style="display:flex;background:rgba(255,255,255,0.08);border-radius:9999px;padding:2px;gap:2px;">
        <div style="padding:4px 12px;border-radius:9999px;background:#178A5C;color:#FFFFFF;font-size:11.5px;font-weight:700;">Student</div>
        <a href="TASEZ Admin Console.dc.html" style="padding:4px 12px;border-radius:9999px;color:rgba(255,255,255,0.7);font-size:11.5px;font-weight:600;text-decoration:none;">Admin</a>
      </div>
      <div title="Lerato Mokoena · TASEZ-2025-0342" style="width:32px;height:32px;border-radius:50%;background:#178A5C;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11.5px;color:#fff;cursor:default;">LM</div>
    </div>
  </div>
  <!-- CONTENT -->"""

sp = old_sp_navbar_pattern.sub(new_sp_navbar_html, sp)

with open(student_path, "w", encoding="utf-8") as f:
    f.write(sp)

print("Student Portal Tubelight Navbar implemented.")


# ── ADMIN CONSOLE TUBELIGHT NAVBAR ───────────────────────────────────────────
admin_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
with open(admin_path, "r", encoding="utf-8") as f:
    ac = f.read()

ac = ac.replace("*{box-sizing:border-box;}", "*{box-sizing:border-box;}\n" + tubelight_css)
ac = ac.replace('<div style="flex:1;padding:26px 28px 48px;">', '<div style="flex:1;padding:84px 28px 48px;">')

old_ac_navbar_pattern = re.compile(r'<div style="position:sticky;top:0;z-index:20;background:linear-gradient\(90deg,#081F38,#0B2C4D 55%,#0E3A5C\);.*?</div>\s*</div>\s*<div style="flex:1;', re.DOTALL)

new_ac_navbar_html = """<!-- TUBELIGHT FLOATING NAVBAR (ADMIN) -->
  <div class="tubelight-bar">
    <!-- Logo -->
    <a href="#" onClick="{{ () => this.go('dashboard') }}" style="display:flex;align-items:center;padding:0 6px;cursor:pointer;">
      <img src="./tasiz-nobg-logo.png" alt="TASEZ" style="height:28px;filter:brightness(0) invert(1);display:block;">
    </a>

    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ vDash ? 'active' : '' }}" onClick="{{ () => this.go('dashboard') }}">
      <sc-if value="{{ vDash }}"><div class="tubelight-lamp"></div></sc-if>
      Overview
    </div>

    <!-- Item 2: Students & Intake Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vStudPipeline || vStudReg || vStudRisk || vStudStats || vQueue) ? 'active' : '' }}">
        <sc-if value="{{ vStudPipeline || vStudReg || vStudRisk || vStudStats || vQueue }}"><div class="tubelight-lamp"></div></sc-if>
        Students &amp; Intake <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ () => this.go('pipeline') }}">📊 Recruitment Pipeline</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('reg') }}">📋 Learner Register</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('risk') }}">⚠️ At-Risk Learners</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('stats') }}">📈 Intake Statistics</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('queue') }}">✒️ Logbook Approvals</div>
      </div>
    </div>

    <!-- Item 3: Academics & Quality Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert) ? 'active' : '' }}">
        <sc-if value="{{ vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert }}"><div class="tubelight-lamp"></div></sc-if>
        Academics &amp; Quality <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-menu-item nav-dropdown-item" onClick="{{ () => this.go('sched') }}">📅 Assessment Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('builder') }}">🛠 Curriculum Builder</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('author') }}">❓ Question Bank</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('vle') }}">💻 VLE Tracking</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('centres') }}">🏢 EISA Assessment Centres</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('cert') }}">🏅 Certification Runs</div>
      </div>
    </div>

    <!-- Item 4: Partners & Operations Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents) ? 'active' : '' }}">
        <sc-if value="{{ vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents }}"><div class="tubelight-lamp"></div></sc-if>
        Partners &amp; Operations <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ () => this.go('sponsors') }}">💰 Sponsor Register</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('progs') }}">📖 Programme Catalogue</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('hosts') }}">🏭 Host Employers</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('providers') }}">🏫 Training Providers</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('accr') }}">📜 SETA Accreditation</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('staff') }}">👨‍🏫 Facilitators &amp; Assessors</div>
        <div class="nav-dropdown-item" onClick="{{ () => this.go('users') }}">🔑 User Provisioning</div>
      </div>
    </div>

    <!-- Role Switcher & Avatar -->
    <div style="display:flex;align-items:center;gap:6px;margin-left:8px;padding-left:8px;border-left:1px solid rgba(255,255,255,0.12);">
      <div style="display:flex;background:rgba(255,255,255,0.08);border-radius:9999px;padding:2px;gap:2px;">
        <a href="TASEZ Student Portal.dc.html" style="padding:4px 12px;border-radius:9999px;color:rgba(255,255,255,0.7);font-size:11.5px;font-weight:600;text-decoration:none;">Student</a>
        <div style="padding:4px 12px;border-radius:9999px;background:#178A5C;color:#FFFFFF;font-size:11.5px;font-weight:700;">Admin</div>
      </div>
      <div title="Nomsa Khumalo · Administrator" style="width:32px;height:32px;border-radius:50%;background:#1B4F8A;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11.5px;color:#fff;cursor:default;">NK</div>
    </div>
  </div>
  <div style="flex:1;'"""

ac = old_ac_navbar_pattern.sub(new_ac_navbar_html, ac)

with open(admin_path, "w", encoding="utf-8") as f:
    f.write(ac)

print("Admin Console Tubelight Navbar implemented.")

#!/usr/bin/env python3
"""
Fix Navbar Clickability, Increase Content Padding (Move Page Lower), and Enlarge Floating Tubelight Navbar.
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"

# ── STUDENT PORTAL FIXES ──────────────────────────────────────────────────────
sp_path = os.path.join(DIR, "TASEZ Student Portal.dc.html")
with open(sp_path, "r", encoding="utf-8") as f:
    sp = f.read()

# 1. Increase top padding of main content from 84px to 125px to move pages lower
sp = sp.replace('<div style="flex:1;padding:84px 28px 48px;">', '<div style="flex:1;padding:125px 28px 48px;">')

# 2. Update Tubelight Navbar CSS padding & size
old_sp_css = """.tubelight-bar { position:fixed; top:18px; left:50%; transform:translateX(-50%); z-index:999; background:rgba(8,25,45,0.85); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); border:1px solid rgba(61,201,138,0.35); border-radius:9999px; padding:5px 12px; box-shadow:0 16px 40px rgba(0,0,0,0.6),0 0 24px rgba(61,201,138,0.2); display:flex; align-items:center; gap:8px; }
  .tubelight-item { position:relative; cursor:pointer; font-size:13px; font-weight:600; padding:8px 16px; border-radius:9999px; color:rgba(255,255,255,0.8); transition:all 0.2s ease; display:flex; align-items:center; gap:6px; white-space:nowrap; }"""

new_sp_css = """.tubelight-bar { position:fixed; top:20px; left:50%; transform:translateX(-50%); z-index:9999; background:rgba(8,25,45,0.92); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border:1.5px solid rgba(61,201,138,0.4); border-radius:9999px; padding:8px 20px; box-shadow:0 20px 50px rgba(0,0,0,0.7),0 0 30px rgba(61,201,138,0.25); display:flex; align-items:center; gap:12px; }
  .tubelight-item { position:relative; cursor:pointer; font-size:13.5px; font-weight:600; padding:9px 18px; border-radius:9999px; color:rgba(255,255,255,0.85); transition:all 0.2s ease; display:flex; align-items:center; gap:6px; white-space:nowrap; }"""

sp = sp.replace(old_sp_css, new_sp_css)

# 3. Expose goDash, goCourse, goNon handlers in Student Portal data() return
sp = sp.replace(
    "goFin:()=>this.go('fin'), goProg:()=>this.go('prog'), goTime:()=>this.go('time'), goTrans:()=>this.go('trans'),",
    "goDash:()=>this.go('dashboard'), goCourse:()=>this.go('course'), goNon:()=>this.go('non'), goFin:()=>this.go('fin'), goProg:()=>this.go('prog'), goTime:()=>this.go('time'), goTrans:()=>this.go('trans'),"
)

# 4. Replace Tubelight Navbar HTML with valid Stitch prop-bound onClick handlers
old_sp_nav_html = re.search(r'<!-- TUBELIGHT FLOATING NAVBAR -->.*?<!-- CONTENT -->', sp, re.DOTALL).group(0)

new_sp_nav_html = """<!-- TUBELIGHT FLOATING NAVBAR -->
  <div class="tubelight-bar">
    <!-- Logo -->
    <div onClick="{{ goDash }}" style="display:flex;align-items:center;padding:0 6px;cursor:pointer;">
      <img src="./tasiz-nobg-logo.png" alt="TASEZ" style="height:32px;filter:brightness(0) invert(1);display:block;margin-right:4px;">
    </div>

    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ sDash ? 'active' : '' }}" onClick="{{ goDash }}">
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
        <div class="nav-dropdown-item" onClick="{{ goCourse }}">📚 My Coursework</div>
        <div class="nav-dropdown-item" onClick="{{ goProg }}">📈 Progress &amp; Results</div>
        <div class="nav-dropdown-item" onClick="{{ goTime }}">📅 Timetable &amp; Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ goNon }}">🎓 Non-Accredited Events</div>
      </div>
    </div>

    <!-- Item 3: Records & Finance Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (sTrans || sFin) ? 'active' : '' }}">
        <sc-if value="{{ sTrans || sFin }}"><div class="tubelight-lamp"></div></sc-if>
        Records &amp; Finance <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goTrans }}">📄 Academic Transcripts</div>
        <div class="nav-dropdown-item" onClick="{{ goFin }}">💳 Statements &amp; Fees</div>
      </div>
    </div>

    <!-- Role Switcher & Avatar -->
    <div style="display:flex;align-items:center;gap:8px;margin-left:8px;padding-left:12px;border-left:1px solid rgba(255,255,255,0.15);">
      <div style="display:flex;background:rgba(255,255,255,0.08);border-radius:9999px;padding:3px;gap:2px;">
        <div style="padding:5px 14px;border-radius:9999px;background:#178A5C;color:#FFFFFF;font-size:12px;font-weight:700;">Student</div>
        <a href="TASEZ Admin Console.dc.html" style="padding:5px 14px;border-radius:9999px;color:rgba(255,255,255,0.75);font-size:12px;font-weight:600;text-decoration:none;">Admin</a>
      </div>
      <div title="Lerato Mokoena · TASEZ-2025-0342" style="width:34px;height:34px;border-radius:50%;background:#178A5C;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;color:#fff;cursor:default;">LM</div>
    </div>
  </div>
  <!-- CONTENT -->"""

sp = sp.replace(old_sp_nav_html, new_sp_nav_html)

with open(sp_path, "w", encoding="utf-8") as f:
    f.write(sp)

print("Student Portal Tubelight Navbar clickability & padding fixed.")


# ── ADMIN CONSOLE FIXES ───────────────────────────────────────────────────────
ac_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
with open(ac_path, "r", encoding="utf-8") as f:
    ac = f.read()

# 1. Increase top padding of main content to 125px
ac = ac.replace('<div style="flex:1;padding:84px 28px 48px;">', '<div style="flex:1;padding:125px 28px 48px;">')

# 2. Update CSS
ac = ac.replace(old_sp_css, new_sp_css)

# 3. Expose admin navigation handlers in data() return
admin_handlers = """      goDash:()=>this.go('dashboard'), goPipeline:()=>this.go('pipeline'), goReg:()=>this.go('reg'), goRisk:()=>this.go('risk'), goStats:()=>this.go('stats'), goQueue:()=>this.go('queue'),
      goSched:()=>this.go('sched'), goBuilder:()=>this.go('builder'), goAuthor:()=>this.go('author'), goVle:()=>this.go('vle'), goCentres:()=>this.go('centres'), goCert:()=>this.go('cert'),
      goSponsors:()=>this.go('sponsors'), goProgs:()=>this.go('progs'), goHosts:()=>this.go('hosts'), goProviders:()=>this.go('providers'), goAccr:()=>this.go('accr'), goStaff:()=>this.go('staff'), goUsers:()=>this.go('users'),"""

ac = ac.replace("return {", "return {\n" + admin_handlers)

# 4. Replace Admin Navbar HTML with prop-bound onClick handlers
old_ac_nav_html = re.search(r'<!-- TUBELIGHT FLOATING NAVBAR \(ADMIN\) -->.*?<div style="flex:1;', ac, re.DOTALL).group(0)

new_ac_nav_html = """<!-- TUBELIGHT FLOATING NAVBAR (ADMIN) -->
  <div class="tubelight-bar">
    <!-- Logo -->
    <div onClick="{{ goDash }}" style="display:flex;align-items:center;padding:0 6px;cursor:pointer;">
      <img src="./tasiz-nobg-logo.png" alt="TASEZ" style="height:32px;filter:brightness(0) invert(1);display:block;margin-right:4px;">
    </div>

    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ vDash ? 'active' : '' }}" onClick="{{ goDash }}">
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
        <div class="nav-dropdown-item" onClick="{{ goPipeline }}">📊 Recruitment Pipeline</div>
        <div class="nav-dropdown-item" onClick="{{ goReg }}">📋 Learner Register</div>
        <div class="nav-dropdown-item" onClick="{{ goRisk }}">⚠️ At-Risk Learners</div>
        <div class="nav-dropdown-item" onClick="{{ goStats }}">📈 Intake Statistics</div>
        <div class="nav-dropdown-item" onClick="{{ goQueue }}">✒️ Logbook Approvals</div>
      </div>
    </div>

    <!-- Item 3: Academics & Quality Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert) ? 'active' : '' }}">
        <sc-if value="{{ vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert }}"><div class="tubelight-lamp"></div></sc-if>
        Academics &amp; Quality <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goSched }}">📅 Assessment Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ goBuilder }}">🛠 Curriculum Builder</div>
        <div class="nav-dropdown-item" onClick="{{ goAuthor }}">❓ Question Bank</div>
        <div class="nav-dropdown-item" onClick="{{ goVle }}">💻 VLE Tracking</div>
        <div class="nav-dropdown-item" onClick="{{ goCentres }}">🏢 EISA Assessment Centres</div>
        <div class="nav-dropdown-item" onClick="{{ goCert }}">🏅 Certification Runs</div>
      </div>
    </div>

    <!-- Item 4: Partners & Operations Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents) ? 'active' : '' }}">
        <sc-if value="{{ vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents }}"><div class="tubelight-lamp"></div></sc-if>
        Partners &amp; Operations <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goSponsors }}">💰 Sponsor Register</div>
        <div class="nav-dropdown-item" onClick="{{ goProgs }}">📖 Programme Catalogue</div>
        <div class="nav-dropdown-item" onClick="{{ goHosts }}">🏭 Host Employers</div>
        <div class="nav-dropdown-item" onClick="{{ goProviders }}">🏫 Training Providers</div>
        <div class="nav-dropdown-item" onClick="{{ goAccr }}">📜 SETA Accreditation</div>
        <div class="nav-dropdown-item" onClick="{{ goStaff }}">👨‍🏫 Facilitators &amp; Assessors</div>
        <div class="nav-dropdown-item" onClick="{{ goUsers }}">🔑 User Provisioning</div>
      </div>
    </div>

    <!-- Role Switcher & Avatar -->
    <div style="display:flex;align-items:center;gap:8px;margin-left:8px;padding-left:12px;border-left:1px solid rgba(255,255,255,0.15);">
      <div style="display:flex;background:rgba(255,255,255,0.08);border-radius:9999px;padding:3px;gap:2px;">
        <a href="TASEZ Student Portal.dc.html" style="padding:5px 14px;border-radius:9999px;color:rgba(255,255,255,0.75);font-size:12px;font-weight:600;text-decoration:none;">Student</a>
        <div style="padding:5px 14px;border-radius:9999px;background:#178A5C;color:#FFFFFF;font-size:12px;font-weight:700;">Admin</div>
      </div>
      <div title="Nomsa Khumalo · Administrator" style="width:34px;height:34px;border-radius:50%;background:#1B4F8A;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;color:#fff;cursor:default;">NK</div>
    </div>
  </div>
  <div style="flex:1;"""

ac = ac.replace(old_ac_nav_html, new_ac_nav_html)

with open(ac_path, "w", encoding="utf-8") as f:
    f.write(ac)

print("Admin Console Tubelight Navbar clickability & padding fixed.")

#!/usr/bin/env python3
"""
Bulletproof Admin Dropdown Navigation Fix:
1. Fix CSS hover gap bridge so dropdown menus never close prematurely on hover.
2. Bind window.dcGoAdmin & window.dcGoStudent global helpers to Component instances.
3. Add inline onclick fallback handlers to guarantee clicks work everywhere.
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"

# ── ADMIN CONSOLE ─────────────────────────────────────────────────────────────
ac_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
with open(ac_path, "r", encoding="utf-8") as f:
    ac = f.read()

# 1. Update CSS to include invisible hover bridge and adjust dropdown placement
css_fix = """  .nav-dropdown { position:relative; display:flex; align-items:center; }
  .nav-dropdown::after { content:""; position:absolute; top:100%; left:-10px; right:-10px; height:18px; }
  .nav-dropdown-menu { position:absolute; top:calc(100% + 4px); left:50%; transform:translateX(-50%) translateY(8px); background:rgba(8,25,45,0.96); backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px); border:1px solid rgba(61,201,138,0.35); border-radius:18px; padding:8px; box-shadow:0 20px 48px rgba(0,0,0,0.8),0 0 20px rgba(61,201,138,0.2); min-width:220px; display:flex; flex-direction:column; gap:4px; opacity:0; pointer-events:none; transition:all 0.18s cubic-bezier(0.16, 1, 0.3, 1); z-index:10000; }
  .nav-dropdown:hover .nav-dropdown-menu { opacity:1; pointer-events:auto; transform:translateX(-50%) translateY(0); }"""

ac = re.sub(r'\.nav-dropdown\s*\{.*?\n  \.nav-dropdown-item:hover\s*\{.*?\}', css_fix + '\n  .nav-dropdown-item { display:flex; align-items:center; gap:10px; padding:10px 14px; border-radius:10px; color:#E2E8F0; font-size:13px; font-weight:600; cursor:pointer; transition:all 0.15s; white-space:nowrap; }\n  .nav-dropdown-item:hover { background:rgba(61,201,138,0.2); color:#3DC98A; }', ac, flags=re.DOTALL)

# 2. Expose window.dcGoAdmin inside Component
window_bridge = """  componentDidMount() {
    window.dcGoAdmin = (sec) => {
      this.go(sec);
    };
  }
"""

ac = ac.replace("class Component extends DCLogic {", "class Component extends DCLogic {\n" + window_bridge)

# 3. Update Admin Navbar HTML to include fallback onclick calls
new_ac_nav_items = """    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ vDash ? 'active' : '' }}" onClick="{{ goDash }}" onclick="window.dcGoAdmin && window.dcGoAdmin('dashboard')">
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
        <div class="nav-dropdown-item" onClick="{{ goPipeline }}" onclick="window.dcGoAdmin && window.dcGoAdmin('pipeline')">📊 Recruitment Pipeline</div>
        <div class="nav-dropdown-item" onClick="{{ goReg }}" onclick="window.dcGoAdmin && window.dcGoAdmin('reg')">📋 Learner Register</div>
        <div class="nav-dropdown-item" onClick="{{ goRisk }}" onclick="window.dcGoAdmin && window.dcGoAdmin('risk')">⚠️ At-Risk Learners</div>
        <div class="nav-dropdown-item" onClick="{{ goStats }}" onclick="window.dcGoAdmin && window.dcGoAdmin('stats')">📈 Intake Statistics</div>
        <div class="nav-dropdown-item" onClick="{{ goQueue }}" onclick="window.dcGoAdmin && window.dcGoAdmin('queue')">✒️ Logbook Approvals</div>
      </div>
    </div>

    <!-- Item 3: Academics & Quality Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert) ? 'active' : '' }}">
        <sc-if value="{{ vAcadSched || vAcadBuilder || vAcadAuthor || vAcadVle || vAcadCentres || vCert }}"><div class="tubelight-lamp"></div></sc-if>
        Academics &amp; Quality <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goSched }}" onclick="window.dcGoAdmin && window.dcGoAdmin('sched')">📅 Assessment Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ goBuilder }}" onclick="window.dcGoAdmin && window.dcGoAdmin('builder')">🛠 Curriculum Builder</div>
        <div class="nav-dropdown-item" onClick="{{ goAuthor }}" onclick="window.dcGoAdmin && window.dcGoAdmin('author')">❓ Question Bank</div>
        <div class="nav-dropdown-item" onClick="{{ goVle }}" onclick="window.dcGoAdmin && window.dcGoAdmin('vle')">💻 VLE Tracking</div>
        <div class="nav-dropdown-item" onClick="{{ goCentres }}" onclick="window.dcGoAdmin && window.dcGoAdmin('centres')">🏢 EISA Assessment Centres</div>
        <div class="nav-dropdown-item" onClick="{{ goCert }}" onclick="window.dcGoAdmin && window.dcGoAdmin('cert')">🏅 Certification Runs</div>
      </div>
    </div>

    <!-- Item 4: Partners & Operations Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents) ? 'active' : '' }}">
        <sc-if value="{{ vPartSponsors || vPartProgs || vPartHosts || vPartProviders || vCompAccr || vCompSites || vCompQms || vPeopleStaff || vPeopleUsers || vNonEvents }}"><div class="tubelight-lamp"></div></sc-if>
        Partners &amp; Operations <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goSponsors }}" onclick="window.dcGoAdmin && window.dcGoAdmin('sponsors')">💰 Sponsor Register</div>
        <div class="nav-dropdown-item" onClick="{{ goProgs }}" onclick="window.dcGoAdmin && window.dcGoAdmin('progs')">📖 Programme Catalogue</div>
        <div class="nav-dropdown-item" onClick="{{ goHosts }}" onclick="window.dcGoAdmin && window.dcGoAdmin('hosts')">🏭 Host Employers</div>
        <div class="nav-dropdown-item" onClick="{{ goProviders }}" onclick="window.dcGoAdmin && window.dcGoAdmin('providers')">🏫 Training Providers</div>
        <div class="nav-dropdown-item" onClick="{{ goAccr }}" onclick="window.dcGoAdmin && window.dcGoAdmin('accr')">📜 SETA Accreditation</div>
        <div class="nav-dropdown-item" onClick="{{ goStaff }}" onclick="window.dcGoAdmin && window.dcGoAdmin('staff')">👨‍🏫 Facilitators &amp; Assessors</div>
        <div class="nav-dropdown-item" onClick="{{ goUsers }}" onclick="window.dcGoAdmin && window.dcGoAdmin('users')">🔑 User Provisioning</div>
      </div>
    </div>"""

# Replace navbar items in Admin Console
ac = re.sub(r'<!-- Item 1: Overview -->.*?<!-- Role Switcher & Avatar -->', new_ac_nav_items + '\n\n    <!-- Role Switcher & Avatar -->', ac, flags=re.DOTALL)

with open(ac_path, "w", encoding="utf-8") as f:
    f.write(ac)

print("Admin Console bulletproof dropdown fix applied.")


# ── STUDENT PORTAL ───────────────────────────────────────────────────────────
sp_path = os.path.join(DIR, "TASEZ Student Portal.dc.html")
with open(sp_path, "r", encoding="utf-8") as f:
    sp = f.read()

sp = re.sub(r'\.nav-dropdown\s*\{.*?\n  \.nav-dropdown-item:hover\s*\{.*?\}', css_fix + '\n  .nav-dropdown-item { display:flex; align-items:center; gap:10px; padding:10px 14px; border-radius:10px; color:#E2E8F0; font-size:13px; font-weight:600; cursor:pointer; transition:all 0.15s; white-space:nowrap; }\n  .nav-dropdown-item:hover { background:rgba(61,201,138,0.2); color:#3DC98A; }', sp, flags=re.DOTALL)

sp_window_bridge = """  componentDidMount() {
    window.dcGoStudent = (screen) => {
      this.go(screen);
    };
  }
"""

sp = sp.replace("class Component extends DCLogic {", "class Component extends DCLogic {\n" + sp_window_bridge)

new_sp_nav_items = """    <!-- Item 1: Overview -->
    <div class="tubelight-item {{ sDash ? 'active' : '' }}" onClick="{{ goDash }}" onclick="window.dcGoStudent && window.dcGoStudent('dashboard')">
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
        <div class="nav-dropdown-item" onClick="{{ goCourse }}" onclick="window.dcGoStudent && window.dcGoStudent('course')">📚 My Coursework</div>
        <div class="nav-dropdown-item" onClick="{{ goProg }}" onclick="window.dcGoStudent && window.dcGoStudent('prog')">📈 Progress &amp; Results</div>
        <div class="nav-dropdown-item" onClick="{{ goTime }}" onclick="window.dcGoStudent && window.dcGoStudent('time')">📅 Timetable &amp; Schedule</div>
        <div class="nav-dropdown-item" onClick="{{ goNon }}" onclick="window.dcGoStudent && window.dcGoStudent('non')">🎓 Non-Accredited Events</div>
      </div>
    </div>

    <!-- Item 3: Records & Finance Dropdown -->
    <div class="nav-dropdown">
      <div class="tubelight-item {{ (sTrans || sFin) ? 'active' : '' }}">
        <sc-if value="{{ sTrans || sFin }}"><div class="tubelight-lamp"></div></sc-if>
        Records &amp; Finance <span style="font-size:10px;opacity:0.7;">▼</span>
      </div>
      <div class="nav-dropdown-menu">
        <div class="nav-dropdown-item" onClick="{{ goTrans }}" onclick="window.dcGoStudent && window.dcGoStudent('trans')">📄 Academic Transcripts</div>
        <div class="nav-dropdown-item" onClick="{{ goFin }}" onclick="window.dcGoStudent && window.dcGoStudent('fin')">💳 Statements &amp; Fees</div>
      </div>
    </div>"""

sp = re.sub(r'<!-- Item 1: Overview -->.*?<!-- Role Switcher & Avatar -->', new_sp_nav_items + '\n\n    <!-- Role Switcher & Avatar -->', sp, flags=re.DOTALL)

with open(sp_path, "w", encoding="utf-8") as f:
    f.write(sp)

print("Student Portal bulletproof dropdown fix applied.")

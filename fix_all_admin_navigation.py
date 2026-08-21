#!/usr/bin/env python3
"""
Deep Fix for Admin Console Navigation & Dropdown Execution
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\
"""
import os, re

DIR = r"c:\Users\brend\Desktop\build\tasez-training-academy"

# ── ADMIN CONSOLE ─────────────────────────────────────────────────────────────
ac_path = os.path.join(DIR, "TASEZ Admin Console.dc.html")
with open(ac_path, "r", encoding="utf-8") as f:
    ac = f.read()

# 1. Fix broken style syntax error at line 110: <div style="flex:1;'padding:84px 28px 48px;">
ac = re.sub(r'<div style="flex:1;[\'"]?padding:[^">]+">', '<div style="flex:1;padding:130px 28px 48px;">', ac)

# 2. Update Component class methods in Admin Console JS
class_methods = """class Component extends DCLogic {

  go(sec) { this.setState({ sec, repDone: false }); }

  goDash = () => this.go('dashboard');
  goPipeline = () => this.go('pipeline');
  goReg = () => this.go('reg');
  goRisk = () => this.go('risk');
  goStats = () => this.go('stats');
  goQueue = () => this.go('queue');
  goSched = () => this.go('sched');
  goBuilder = () => this.go('builder');
  goAuthor = () => this.go('author');
  goVle = () => this.go('vle');
  goCentres = () => this.go('centres');
  goCert = () => this.go('cert');
  goSponsors = () => this.go('sponsors');
  goProgs = () => this.go('progs');
  goHosts = () => this.go('hosts');
  goProviders = () => this.go('providers');
  goAccr = () => this.go('accr');
  goStaff = () => this.go('staff');
  goUsers = () => this.go('users');

  getSecTitles(sec) {
    const map = {
      dashboard: ['Management Dashboard', 'Academy-wide statistics, intake pipeline and key performance metrics.'],
      dash: ['Management Dashboard', 'Academy-wide statistics, intake pipeline and key performance metrics.'],
      pipeline: ['Recruitment Pipeline', 'Applications, shortlisting and registration pipeline for 2026/27.'],
      reg: ['Learner Register', 'Enrolled learners across all qualifications, sponsors and projects.'],
      risk: ['At-Risk Learners', 'Learners flagged for attendance, assessment or logbook early intervention.'],
      stats: ['Intake Statistics', 'Geographic, demographic and cohort distribution analysis.'],
      queue: ['Logbook Approvals', 'Pending supervisor and mentor sign-offs awaiting administrative review.'],
      sched: ['Assessment Schedule', 'Formative, summative and moderation calendar.'],
      builder: ['Curriculum Builder', 'Structure and module layout for accredited qualifications.'],
      author: ['Question Bank', 'Item bank for online knowledge quizzes and Safe Exam Browser tests.'],
      vle: ['VLE Tracking', 'Real-time assessment tracking and blended learning analytics.'],
      centres: ['EISA Assessment Centres', 'Accredited assessment sites and invigilator allocation.'],
      cert: ['Certification Runs', 'Batch certificate printing, serial numbers and NAMB trade test numbers.'],
      sponsors: ['Sponsor Register', 'Grants, funding agreements and financial summaries per sponsor.'],
      progs: ['Programme Catalogue', 'Accredited and short-course learning programmes.'],
      hosts: ['Host Employers', 'Workplace learning host companies and SETA agreements.'],
      providers: ['Training Providers', 'Co-delivery partners, SDP accreditations and compliance.'],
      accr: ['SETA Accreditation', 'QCTO SDP accreditation status and audit records.'],
      staff: ['Facilitators & Assessors', 'Registered facilitators, assessors and internal moderators.'],
      users: ['User Provisioning', 'Role-based access control and named user licence usage.']
    };
    return map[sec] || map['dashboard'];
  }
"""

ac = re.sub(r'class Component extends DCLogic \{.*?\n  state = \{', class_methods + '\n  state = {', ac, flags=re.DOTALL)

# 3. Update renderVals() in Admin Console
render_vals_code = """  renderVals() {
    return {
      goDash: this.goDash,
      goPipeline: this.goPipeline,
      goReg: this.goReg,
      goRisk: this.goRisk,
      goStats: this.goStats,
      goQueue: this.goQueue,
      goSched: this.goSched,
      goBuilder: this.goBuilder,
      goAuthor: this.goAuthor,
      goVle: this.goVle,
      goCentres: this.goCentres,
      goCert: this.goCert,
      goSponsors: this.goSponsors,
      goProgs: this.goProgs,
      goHosts: this.goHosts,
      goProviders: this.goProviders,
      goAccr: this.goAccr,
      goStaff: this.goStaff,
      goUsers: this.goUsers,
      ...this.v1(), ...this.v2(), ...this.v3(), ...this.v4(), ...this.v5()
    };
  }"""

ac = re.sub(r'renderVals\(\)\s*\{.*?\}', render_vals_code, ac, flags=re.DOTALL)

with open(ac_path, "w", encoding="utf-8") as f:
    f.write(ac)

print("Admin Console navigation deep fix complete.")


# ── STUDENT PORTAL ───────────────────────────────────────────────────────────
sp_path = os.path.join(DIR, "TASEZ Student Portal.dc.html")
with open(sp_path, "r", encoding="utf-8") as f:
    sp = f.read()

# Make sure padding is 130px
sp = re.sub(r'<div style="flex:1;[\'"]?padding:[^">]+">', '<div style="flex:1;padding:130px 28px 48px;">', sp)

# Add Component bound methods in Student Portal
sp_class_methods = """class Component extends DCLogic {

  go(screen) { this.setState({ screen }); }

  goDash = () => this.go('dashboard');
  goCourse = () => this.go('course');
  goProg = () => this.go('prog');
  goTime = () => this.go('time');
  goNon = () => this.go('non');
  goTrans = () => this.go('trans');
  goFin = () => this.go('fin');
"""

sp = re.sub(r'class Component extends DCLogic \{.*?\n  state = \{', sp_class_methods + '\n  state = {', sp, flags=re.DOTALL)

with open(sp_path, "w", encoding="utf-8") as f:
    f.write(sp)

print("Student Portal navigation deep fix complete.")

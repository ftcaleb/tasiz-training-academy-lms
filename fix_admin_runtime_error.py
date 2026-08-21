#!/usr/bin/env python3
"""
Fix TASEZ Admin Console JavaScript Runtime Error:
1. Define v1() / vDash() method properly
2. Resolve secTitle & secDesc dynamically for all admin sub-views
"""
import os, re

fpath = r"c:\Users\brend\Desktop\build\tasez-training-academy\TASEZ Admin Console.dc.html"

with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Define section titles & descriptions map
sec_map_code = """
  getSecTitles(sec) {
    const map = {
      dashboard: ['Management Dashboard', 'Academy-wide statistics, intake pipeline and key performance metrics.'],
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

# Inject getSecTitles into Component class
c = c.replace("class Component extends DCLogic {", "class Component extends DCLogic {\n" + sec_map_code)

# 2. Fix v1() method and renderVals() in Admin Console JS
old_renderVals = "renderVals(){ return {\n      goDash:()=>this.go('dashboard'), goPipeline:()=>this.go('pipeline'), goReg:()=>this.go('reg'), goRisk:()=>this.go('risk'), goStats:()=>this.go('stats'), goQueue:()=>this.go('queue'),\n      goSched:()=>this.go('sched'), goBuilder:()=>this.go('builder'), goAuthor:()=>this.go('author'), goVle:()=>this.go('vle'), goCentres:()=>this.go('centres'), goCert:()=>this.go('cert'),\n      goSponsors:()=>this.go('sponsors'), goProgs:()=>this.go('progs'), goHosts:()=>this.go('hosts'), goProviders:()=>this.go('providers'), goAccr:()=>this.go('accr'), goStaff:()=>this.go('staff'), goUsers:()=>this.go('users'),...this.v1(), ...this.v2(), ...this.v3(), ...this.v4(), ...this.v5()}; }"

new_renderVals = """v1(){
    const st = this.state, S = this.S();
    const [secTitle, secDesc] = this.getSecTitles(st.sec);
    return {
      secTitle, secDesc,
      vDash: st.sec === 'dashboard' || st.sec === 'dash',
      vStudPipeline: st.sec === 'pipeline',
      vStudReg: st.sec === 'reg',
      vStudRisk: st.sec === 'risk',
      vStudStats: st.sec === 'stats',
      vQueue: st.sec === 'queue',
      vAcadSched: st.sec === 'sched',
      vAcadBuilder: st.sec === 'builder',
      vAcadAuthor: st.sec === 'author',
      vAcadVle: st.sec === 'vle',
      vAcadCentres: st.sec === 'centres',
      vCert: st.sec === 'cert',
      vPartSponsors: st.sec === 'sponsors',
      vPartProgs: st.sec === 'progs',
      vPartHosts: st.sec === 'hosts',
      vPartProviders: st.sec === 'providers',
      vCompAccr: st.sec === 'accr',
      vCompSites: st.sec === 'sites',
      vCompQms: st.sec === 'qms',
      vPeopleStaff: st.sec === 'staff',
      vPeopleUsers: st.sec === 'users',
      vNonEvents: st.sec === 'events',
      vNonFin: st.sec === 'nonfin',
      kpis: [
        {label:'Active learners',value:'386',delta:'+42 YoY',dBg:'rgba(61,201,138,0.16)',dFg:'#3DC98A',sub:'Across 6 accredited programmes',c:'#178A5C'},
        {label:'Completion rate',value:'87%',delta:'+3%',dBg:'rgba(61,201,138,0.16)',dFg:'#3DC98A',sub:'Rolling 12 months, all cohorts',c:'#1B4F8A'},
        {label:'Certificates issued',value:'96',delta:'Q3 2026',dBg:'rgba(56,189,248,0.16)',dFg:'#38BDF8',sub:'Next serial TTA-2026-01238',c:'#0E7490'},
        {label:'At-risk learners',value:'7',delta:'Action needed',dBg:'rgba(239,68,68,0.16)',dFg:'#FCA5A5',sub:'Flagged per QMS TTA-QMS-014',c:'#9F1239'}
      ],
      progBarsDash: [
        {label:'Automotive Production Technician · NQF 4',n:148,pct:100},
        {label:'Mechatronics Artisan (NAMB) · NQF 4',n:86,pct:58},
        {label:'Production Supervisor · NQF 5',n:64,pct:43},
        {label:'Welding Application & Practice · NQF 3',n:52,pct:35},
        {label:'Short courses & skills programmes',n:36,pct:24}
      ],
      licUsed: 412 + st.licAdded, licPct: Math.round(((412 + st.licAdded)/500)*100), licFree: 500 - (412 + st.licAdded),
      repText: st.repDone ? '✓ Report generated — downloaded' : 'Generate report',
      repBg: st.repDone ? 'rgba(61,201,138,0.16)' : '#178A5C',
      repFg: st.repDone ? '#3DC98A' : '#FFFFFF',
      genReport: () => this.setState({repDone: true}),
      repType: st.repType, setRepType: e => this.setState({repType: e.target.value}),
      repPeriod: st.repPeriod, setRepPeriod: e => this.setState({repPeriod: e.target.value}),
      activity: [
        {text:'T. Mahlangu signed off logbook entry WM-01/e2 for Lerato Mokoena (awaiting supervisor).',when:'Today 09:41',c:'#178A5C'},
        {text:'Certification batch CB-2026-014 (Welding NQF 3, 28 learners) queued for QCTO submission.',when:'Today 08:15',c:'#1B4F8A'},
        {text:'Incident report: SEB session terminated early — KM-06 exam, learner S. Mahlatsi (under review).',when:'Yesterday 16:02',c:'#9F1239'},
        {text:'merSETA grant tranche 2 (R 780,000) receipted against DG 2025/26 project.',when:'Yesterday 11:30',c:'#178A5C'},
        {text:'OHS audit completed at Workshop B — 2 minor findings, corrective actions logged.',when:'18 Aug',c:'#B45309'}
      ]
    };
  }

  renderVals(){
    return {
      goDash:()=>this.go('dashboard'), goPipeline:()=>this.go('pipeline'), goReg:()=>this.go('reg'), goRisk:()=>this.go('risk'), goStats:()=>this.go('stats'), goQueue:()=>this.go('queue'),
      goSched:()=>this.go('sched'), goBuilder:()=>this.go('builder'), goAuthor:()=>this.go('author'), goVle:()=>this.go('vle'), goCentres:()=>this.go('centres'), goCert:()=>this.go('cert'),
      goSponsors:()=>this.go('sponsors'), goProgs:()=>this.go('progs'), goHosts:()=>this.go('hosts'), goProviders:()=>this.go('providers'), goAccr:()=>this.go('accr'), goStaff:()=>this.go('staff'), goUsers:()=>this.go('users'),
      ...this.v1(), ...this.v2(), ...this.v3(), ...this.v4(), ...this.v5()
    };
  }"""

c = c.replace(old_renderVals, new_renderVals)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

print("Admin Console JavaScript v1() runtime error fixed.")

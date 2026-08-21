#!/usr/bin/env python3
"""
Implement Bento Card Calendar component in TASEZ Student Portal Month View.
Target: c:\\Users\\brend\\Desktop\\build\\tasez-training-academy\\TASEZ Student Portal.dc.html
"""
import os, re

fpath = r"c:\Users\brend\Desktop\build\tasez-training-academy\TASEZ Student Portal.dc.html"

with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update JS data model for ttCells to support Bento pill styles (active day highlights & glows)
old_cells_js = """    const monthEv = {3:['#38BDF8'],4:['#C084FC'],5:['#3DC98A'],6:['#38BDF8'],7:['#C084FC'],10:['#38BDF8','#22D3EE'],11:['#C084FC'],12:['#3DC98A'],13:['#38BDF8'],14:['#C084FC'],17:['#38BDF8','#38BDF8'],18:['#C084FC','#22D3EE'],19:['#3DC98A','#22D3EE'],20:['#38BDF8','#3DC98A'],21:['#C084FC'],24:['#38BDF8','#38BDF8'],25:['#C084FC'],26:['#3DC98A','#FBBF24'],27:['#FCA5A5','#38BDF8','#22D3EE'],28:['#C084FC','#FBBF24'],31:['#FBBF24']};
    const ttCells = [...Array(5).fill(null),...Array.from({length:31},(_,i)=>i+1)].map(d=>({
      d:d||'', dots:(d&&monthEv[d]||[]).map(c=>({c})), border:d===20?'#3DC98A':'rgba(255,255,255,0.08)', bg:d?'rgba(13,37,64,0.7)':'transparent'
    }));"""

new_cells_js = """    const monthEv = {3:['#38BDF8'],4:['#C084FC'],5:['#3DC98A'],6:['#38BDF8'],7:['#C084FC'],10:['#38BDF8','#22D3EE'],11:['#C084FC'],12:['#3DC98A'],13:['#38BDF8'],14:['#C084FC'],17:['#38BDF8','#38BDF8'],18:['#C084FC','#22D3EE'],19:['#3DC98A','#22D3EE'],20:['#38BDF8','#3DC98A'],21:['#C084FC'],24:['#38BDF8','#38BDF8'],25:['#C084FC'],26:['#3DC98A','#FBBF24'],27:['#FCA5A5','#38BDF8','#22D3EE'],28:['#C084FC','#FBBF24'],31:['#FBBF24']};
    const activeDays = [3, 5, 10, 12, 17, 18, 19, 20, 26, 27];
    const ttCells = [...Array(5).fill(null),...Array.from({length:31},(_,i)=>i+1)].map(d=>{
      const isActive = activeDays.includes(d);
      const isToday = d === 20;
      return {
        d: d || '',
        dots: (d && monthEv[d] || []).map(c => ({c})),
        border: isToday ? '#3DC98A' : (isActive ? 'rgba(61,201,138,0.4)' : 'rgba(255,255,255,0.07)'),
        bg: isToday ? 'linear-gradient(135deg, #178A5C, #3DC98A)' : (isActive ? 'linear-gradient(135deg, rgba(23,138,92,0.45), rgba(13,37,64,0.85))' : (d ? 'rgba(13,37,64,0.5)' : 'transparent')),
        fg: (isToday || isActive) ? '#FFFFFF' : '#94A3B8',
        glow: isToday ? '0 0 16px rgba(61,201,138,0.5)' : (isActive ? '0 4px 14px rgba(23,138,92,0.25)' : 'none')
      };
    });"""

c = c.replace(old_cells_js, new_cells_js)

# 2. Replace Month View HTML template with 2-Column Bento Card Calendar Layout
old_month_html = re.search(r'<sc-if value="\{\{ ttMonth \}\}".*?</sc-if>', c, re.DOTALL).group(0)

new_month_html = """<sc-if value="{{ ttMonth }}" hint-placeholder-val="{{ false }}">
          <div style="display:grid;grid-template-columns:1.8fr 1fr;gap:20px;align-items:start;">
            
            <!-- BENTO CARD CALENDAR CONTAINER -->
            <div style="background:linear-gradient(180deg,rgba(13,37,64,.85),rgba(8,25,45,.95));backdrop-filter:blur(16px);border:1px solid rgba(61,201,138,.25);border-radius:24px;box-shadow:0px 2px 1.5px 0px rgba(165,174,184,.1) inset,0 12px 36px rgba(0,0,0,.5);padding:24px;color:#FFFFFF;position:relative;overflow:hidden;">
              <div style="position:absolute;top:0;right:0;width:300px;height:300px;background:radial-gradient(circle at top right,rgba(61,201,138,0.15),transparent 70%);pointer-events:none;"></div>
              
              <!-- Bento Calendar Header -->
              <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px;padding:0 4px;">
                <div style="display:flex;align-items:center;gap:10px;">
                  <span style="font-family:Archivo;font-weight:700;font-size:18px;color:#FFFFFF;letter-spacing:-.01em;">August, 2026</span>
                  <span style="width:4px;height:4px;border-radius:50%;background:#3DC98A;"></span>
                  <span style="font-size:12px;color:#94A3B8;">30 min call · QCTO Accredited</span>
                </div>
                <div style="font-size:11.5px;font-weight:700;color:#3DC98A;background:rgba(61,201,138,0.14);border:1px solid rgba(61,201,138,0.3);padding:5px 14px;border-radius:20px;letter-spacing:.04em;text-transform:uppercase;">
                  Today: 20 Aug
                </div>
              </div>

              <!-- 7-Column Day Names Row -->
              <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px;text-align:center;margin-bottom:12px;">
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">SUN</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">MON</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">TUE</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">WED</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">THU</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">FRI</div>
                <div style="font-size:11px;font-weight:700;color:#64748B;letter-spacing:.08em;">SAT</div>
              </div>

              <!-- 7-Column Day Pills Grid -->
              <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px;">
                <sc-for list="{{ ttCells }}" as="c" hint-placeholder-count="35">
                  <div style="min-height:52px;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:14px;border:1px solid {{ c.border }};background:{{ c.bg }};color:{{ c.fg }};box-shadow:{{ c.glow }};cursor:pointer;position:relative;transition:all .2s ease;" style-hover="transform:translateY(-2px);border-color:#3DC98A;">
                    <span style="font-size:13px;font-weight:700;">{{ c.d }}</span>
                    <div style="display:flex;gap:3px;margin-top:3px;">
                      <sc-for list="{{ c.dots }}" as="dot" hint-placeholder-count="0">
                        <div style="width:5px;height:5px;border-radius:50%;background:{{ dot.c }};box-shadow:0 0 6px {{ dot.c }};"></div>
                      </sc-for>
                    </div>
                  </div>
                </sc-for>
              </div>

              <!-- Legend Footer -->
              <div style="display:flex;gap:16px;margin-top:20px;font-size:11.5px;color:#94A3B8;flex-wrap:wrap;border-top:1px solid rgba(255,255,255,0.08);padding-top:14px;">
                <span style="display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:#38BDF8;box-shadow:0 0 6px #38BDF8;"></span> Class</span>
                <span style="display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:#3DC98A;box-shadow:0 0 6px #3DC98A;"></span> Practical</span>
                <span style="display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:#C084FC;box-shadow:0 0 6px #C084FC;"></span> Workplace</span>
                <span style="display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:#FBBF24;box-shadow:0 0 6px #FBBF24;"></span> Assessment</span>
                <span style="display:flex;align-items:center;gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:#FCA5A5;box-shadow:0 0 6px #FCA5A5;"></span> EISA / Moderation</span>
              </div>
            </div>

            # SIDE PANEL BENTO DOSSIER
            <div style="display:flex;flex-direction:column;gap:16px;">
              <div style="background:linear-gradient(180deg,rgba(13,37,64,.85),rgba(8,25,45,.95));backdrop-filter:blur(16px);border:1px solid rgba(61,201,138,.25);border-radius:24px;padding:22px;color:#FFFFFF;box-shadow:0 12px 36px rgba(0,0,0,.5);">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
                  <div>
                    <div style="font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#3DC98A;">Selected Schedule</div>
                    <div style="font-family:Archivo;font-weight:700;font-size:18px;margin-top:4px;">20 August 2026</div>
                  </div>
                  <span style="font-size:11px;font-weight:700;background:rgba(61,201,138,0.16);color:#3DC98A;padding:4px 10px;border-radius:12px;border:1px solid rgba(61,201,138,0.3);">2 Sessions</span>
                </div>

                <div style="display:flex;flex-direction:column;gap:10px;margin-top:14px;">
                  <div style="background:rgba(56,189,248,0.12);border-left:4px solid #38BDF8;border-radius:12px;padding:12px 14px;">
                    <div style="font-size:11px;font-weight:700;color:#38BDF8;">08:30–10:30 · Class</div>
                    <div style="font-size:13.5px;font-weight:600;margin-top:4px;color:#FFFFFF;">OHS: PPE and safe work procedures</div>
                    <div style="font-size:11.5px;color:#94A3B8;margin-top:4px;">R. Botha · Room 2.1</div>
                  </div>

                  <div style="background:rgba(61,201,138,0.14);border-left:4px solid #3DC98A;border-radius:12px;padding:12px 14px;">
                    <div style="font-size:11px;font-weight:700;color:#3DC98A;">14:00–16:00 · Practical</div>
                    <div style="font-size:13.5px;font-weight:600;margin-top:4px;color:#FFFFFF;">Height gauge practice session</div>
                    <div style="font-size:11.5px;color:#94A3B8;margin-top:4px;">P. Ndlovu · Metrology Lab</div>
                  </div>
                </div>

                <div style="margin-top:18px;padding:12px 0;border-radius:12px;text-align:center;font-weight:700;font-size:13.5px;cursor:pointer;background:#178A5C;color:#FFFFFF;box-shadow:0 8px 20px rgba(23,138,92,0.4);" style-hover="background:#147A50;">
                  Book Consultation Call
                </div>
              </div>
            </div>

          </div>
        </sc-if>"""

c = c.replace(old_month_html, new_month_html)

with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

print("Bento Card Calendar component successfully implemented.")

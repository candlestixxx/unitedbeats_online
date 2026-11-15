import os
import re

print("===> [1/4] Reading homepage.html...")
home_path = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Host and Repos
content = content.replace('lumbros.me', 'unitedbeats.online')
content = content.replace('Lumbros.me', 'UnitedBeats.Online')
content = content.replace('candlestixxx/lumbros.me', 'candlestixxx/unitedbeats_online')
content = content.replace('candlestixxx@lumbros-node:', 'candlestixxx@unitedbeats-node:')
content = content.replace('id="lumbros-uplink-form"', 'id="ub-uplink-form"')

# 2. Add CRT Original Logo Deck Component
crt_logo_html = '''
    <!-- =========================================================================
         ORIGINAL UNITED BEATS .ONLINE CRT TELEMETRY & MASTER LOGO DECK
         ========================================================================= -->
    <div class="ub-crt-deck-container">
      <div class="ub-crt-monitor-chassis">
        <div class="ub-crt-bezel-rim">
          <div class="ub-crt-screws screw-tl"></div>
          <div class="ub-crt-screws screw-tr"></div>
          <div class="ub-crt-screws screw-bl"></div>
          <div class="ub-crt-screws screw-br"></div>
          
          <div class="ub-crt-hud-header">
            <div class="ub-crt-hud-left">
              <span class="crt-dot-pulse">●</span>
              <span class="crt-tag">ONLIN 1 // API INGESTION: ACTIVE</span>
            </div>
            <div class="ub-crt-hud-center">
              <span class="crt-callout">TENANT 01: UNITED BEATS</span>
            </div>
            <div class="ub-crt-hud-right">
              <span class="crt-tag-cyan">MODEL CONTEXT PROTOCOL (MCP)</span>
            </div>
          </div>

          <div class="ub-crt-screen-viewport">
            <div class="ub-crt-curvature"></div>
            <div class="ub-crt-scanlines"></div>
            <div class="ub-crt-phosphor-glow"></div>
            <img src="/wp-content/uploads/unitedbeats-logo.jpg" alt="United Beats .ONLINE Original Master Logo" class="ub-crt-master-img" />
          </div>

          <div class="ub-crt-hud-footer">
            <div class="ub-crt-foot-item"><span class="f-lbl">SECURITY:</span> <span class="f-val">VRL-1: OPERATIONAL / ZERO-TRUST ACTIVE</span></div>
            <div class="ub-crt-foot-item"><span class="f-lbl">CIPHER:</span> <span class="f-val">ENCRYPTION MATRICES: 4096-BIT</span></div>
            <div class="ub-crt-foot-item"><span class="f-lbl">PILLAR:</span> <span class="f-val">UNITEDBEATS.ONLINE POWERHOUSE</span></div>
          </div>
        </div>
      </div>

      <!-- Pillar Interconnection Mission Banner -->
      <div class="ub-pillar-mission-card">
        <div class="ub-mission-spark">⚡</div>
        <div class="ub-mission-body">
          <h3 class="ub-mission-headline">THE ADVANCED TECH POWERHOUSE WITH LOVE FOR OUR WORLD COMMUNITY &amp; NEIGHBOR</h3>
          <p class="ub-mission-copy">
            <strong>UnitedBeats.Online</strong> is engineered as a foundational core <strong>Pillar</strong> of the United Beats digital ecosystem. Architected with high-assurance mathematical rigor, zero-trust protocols, and neural Model Context Protocol (MCP) meshes—designed to seamlessly interconnect with existing and future pillars of United Beats (HyperNexus VRL-1, Audio Synapses, Community Dance Club, and Distributed Autonomous Agents) until we stand as a leading, globally recognized software company rooted in love for every neighbor.
          </p>
        </div>
        <div class="ub-mission-spark">⚡</div>
      </div>
    </div>
'''

# Insert CRT logo right before the ASCII hero header if not already present
if 'ub-crt-deck-container' not in content:
    content = content.replace(
        '<header class="ascii-hero">',
        crt_logo_html + '\n  <header class="ascii-hero">'
    )
    print("Inserted CRT Logo and Pillar Mission Deck.")
else:
    print("CRT logo deck already present.")

# 3. Add styling for the CRT deck and the brand elements
crt_css = '''
    /* =========================================================================
       AUTHENTIC CRT MONITOR LOGO & PILLAR BRANDING STYLES
       ========================================================================= */
    .ub-crt-deck-container {
      max-width: 1060px;
      margin: 24px auto 35px;
      padding: 0 14px;
      position: relative;
      z-index: 5;
    }

    .ub-crt-monitor-chassis {
      background: linear-gradient(145deg, #121915, #080c09);
      border: 3px solid #00ff6640;
      border-radius: 20px;
      padding: 16px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), 0 0 40px rgba(0, 255, 102, 0.22);
      position: relative;
    }

    .ub-crt-bezel-rim {
      border: 2px solid #00ff6660;
      border-radius: 14px;
      padding: 12px 14px;
      background: radial-gradient(ellipse at 50% 50%, #05140a 0%, #010603 100%);
      position: relative;
    }

    .ub-crt-screws {
      position: absolute;
      width: 8px;
      height: 8px;
      background: #2a3a30;
      border: 1px solid #00ff6680;
      border-radius: 50%;
    }
    .screw-tl { top: 6px; left: 6px; }
    .screw-tr { top: 6px; right: 6px; }
    .screw-bl { bottom: 6px; left: 6px; }
    .screw-br { bottom: 6px; right: 6px; }

    .ub-crt-hud-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 10px;
      margin-bottom: 10px;
      border-bottom: 1px solid rgba(0, 255, 102, 0.25);
      font-family: 'Courier New', monospace;
      font-size: 0.76rem;
      letter-spacing: 1.5px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .crt-dot-pulse {
      color: #00ff66;
      animation: crtPulse 1.4s infinite;
      margin-right: 6px;
    }

    @keyframes crtPulse {
      0%, 100% { opacity: 1; transform: scale(1); text-shadow: 0 0 10px #00ff66; }
      50% { opacity: 0.4; transform: scale(0.9); text-shadow: none; }
    }

    .crt-tag { color: #8ce4a7; font-weight: 700; }
    .crt-callout { color: #00ff66; font-weight: 900; letter-spacing: 2px; }
    .crt-tag-cyan { color: #00e5ff; font-weight: 700; }

    .ub-crt-screen-viewport {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid #00ff6650;
      box-shadow: inset 0 0 40px rgba(0, 255, 102, 0.35);
      background: #000000;
    }

    .ub-crt-master-img {
      width: 100%;
      height: auto;
      display: block;
      filter: contrast(1.08) brightness(1.04);
      transition: filter 0.3s ease;
    }

    .ub-crt-scanlines {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%);
      background-size: 100% 4px;
      pointer-events: none;
      z-index: 2;
      opacity: 0.7;
    }

    .ub-crt-phosphor-glow {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      box-shadow: inset 0 0 30px rgba(0, 255, 102, 0.4);
      pointer-events: none;
      z-index: 3;
    }

    .ub-crt-hud-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      margin-top: 10px;
      border-top: 1px solid rgba(0, 255, 102, 0.25);
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 1.2px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .ub-crt-foot-item .f-lbl { color: #8ce4a7; margin-right: 5px; }
    .ub-crt-foot-item .f-val { color: #00ff66; font-weight: 800; }

    /* Mission & Community Love Callout */
    .ub-pillar-mission-card {
      margin-top: 20px;
      background: linear-gradient(135deg, rgba(0, 40, 18, 0.82), rgba(3, 15, 8, 0.94));
      border: 2px solid #00ff66;
      border-radius: 12px;
      padding: 20px 24px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: 0 10px 30px rgba(0, 255, 102, 0.18);
    }

    .ub-mission-spark {
      font-size: 2rem;
      color: #00ff66;
      text-shadow: 0 0 15px #00ff66;
      animation: crtPulse 2s infinite;
    }

    .ub-mission-body {
      flex: 1;
    }

    .ub-mission-headline {
      margin: 0 0 8px;
      font-family: 'Courier New', monospace;
      font-size: 1.05rem;
      letter-spacing: 2px;
      color: #00ff66;
      text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
      font-weight: 900;
    }

    .ub-mission-copy {
      margin: 0;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #d1fae5;
    }
'''

if 'ub-crt-deck-container' in content and '.ub-crt-deck-container' not in content:
    content = content.replace('</style>', crt_css + '\n    </style>')
    print("Injected CRT Deck CSS.")

# 4. Enhance the Architectural Pillars Section text
content = re.sub(
    r'<strong>Lumbros\.me</strong> is engineered as a living architectural monument\.',
    '<strong>UnitedBeats.Online</strong> is engineered as the advanced tech powerhouse with love for our world community and neighbor. Built as a primary foundational <strong>Pillar</strong> of United Beats, this monument is structured to connect seamlessly with all present and future pillars of our software ecosystem.',
    content
)

# Save updated homepage.html
with open(home_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✔ homepage.html successfully updated and branded!")

# Regenerate subpages (public.html, private.html, posts.html)
print("===> [2/4] Regenerating subpages (public, private, posts)...")
import subprocess
gen_script = os.path.join(os.path.dirname(__file__), 'generate_subpages.py')

# Update generate_subpages.py to reference UNITEDBEATS.ONLINE
with open(gen_script, 'r', encoding='utf-8') as f:
    sub_code = f.read()

sub_code = sub_code.replace('NODE: LUMBROS.ME', 'NODE: UNITEDBEATS.ONLINE')
with open(gen_script, 'w', encoding='utf-8') as f:
    f.write(sub_code)

res = subprocess.run(['python', gen_script], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print(res.stderr)

print("===> [3/4] Checking deploy_page.py for updated database export and labels...")
deploy_script = os.path.join(os.path.dirname(__file__), 'deploy_page.py')
with open(deploy_script, 'r', encoding='utf-8') as f:
    d_code = f.read()

d_code = d_code.replace('lumbros.me', 'unitedbeats.online')
d_code = d_code.replace('Lumbros.me', 'UnitedBeats.Online')
with open(deploy_script, 'w', encoding='utf-8') as f:
    f.write(d_code)

print("✔ deploy_page.py updated.")

print("===> [4/4] Branding complete!")

import os
import re

print("===> [1/5] Reading deploy/homepage.html...")
home_path = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_path, 'r', encoding='utf-8') as f:
    content = f.read()

# -----------------------------------------------------------------------------
# 1. Update Host Name to UNITED BEATS & Ensure 100% UnitedBeats.online branding
# -----------------------------------------------------------------------------
content = re.sub(
    r'<span class="hud-label">HOST:</span>\s*<span class="hud-val glow-cyan">.*?</span>',
    '<span class="hud-label">HOST:</span> <span class="hud-val glow-cyan">UNITED BEATS</span>',
    content
)
content = content.replace('lumbros.me', 'unitedbeats.online')
content = content.replace('Lumbros.me', 'UnitedBeats.online')
content = content.replace('LUMBROS.ME', 'UNITEDBEATS.ONLINE')
print("✔ Host set to UNITED BEATS and brand set to UnitedBeats.online.")

# -----------------------------------------------------------------------------
# 2. Extract Sections 9 and 9.5, replace with Portal Banner, build games.html
# -----------------------------------------------------------------------------
s_9_marker = '<!-- =========================================================================\n       SECTION: PROCEDURAL SHADERTOY'
if s_9_marker not in content:
    s_9_marker = content.find('<section id="shadertoy-tribute"')
else:
    s_9_marker = content.find(s_9_marker)

s_pillars_marker = '<!-- =========================================================================\n       SECTION: THE ARCHITECTURAL PILLARS'
if s_pillars_marker not in content:
    s_pillars_marker = content.find('<section id="pillars-architecture"')
else:
    s_pillars_marker = content.find(s_pillars_marker)

if s_9_marker != -1 and s_pillars_marker != -1 and s_9_marker < s_pillars_marker:
    games_sections = content[s_9_marker:s_pillars_marker]
    print(f"✔ Extracted Sections 9 & 9.5 ({len(games_sections)} chars).")

    # Portal banner to leave on the main page where Sections 9 & 9.5 were
    portal_banner = '''<!-- =========================================================================
       SECTOR DISPATCH: COOL CONCEPT GAMES ARCADE
       Section 09 (Procedural Shadertoy Engine) & Section 09.5 (Spectrum Monopoly Simulator)
       ========================================================================= -->
  <section id="cool-concept-games-portal" class="terminal-section arcade-portal-section">
    <div class="portal-card-frame">
      <div class="portal-glow-bar"></div>
      <div class="portal-header">
        <div class="portal-badge">
          <span class="portal-badge-pip"></span>
          <span class="portal-badge-text">ARCADE SECTOR // ADVANCED GRAPHICAL SIMULATIONS</span>
        </div>
        <span class="portal-tag-cyan">SECTIONS 09 &amp; 09.5 DISPATCHED</span>
      </div>
      <div class="portal-body">
        <div class="portal-icon-block">🎮</div>
        <div class="portal-info-block">
          <div class="section-badge" style="margin-bottom: 8px;"><span>[ SECTIONS 0x09 &amp; 0x09.5 ]</span> // DEDICATED ARCADE SECTOR</div>
          <h3 class="portal-title">⚡ ⟦ COOL CONCEPT GAMES ⟧</h3>
          <p class="portal-desc">
            The interactive <strong>Procedural Shadertoy Engine</strong> (Wave Structure of Matter &amp; 3D Earth Orbit) and <strong>Spectrum Monopoly</strong> (Planetary Survival &amp; Economic Equilibrium Simulator) have moved from the main hub into their own dedicated, full-screen interactive arcade sector.
          </p>
          <div class="portal-features-row">
            <span class="portal-chip">★ PROCEDURAL SHADERTOY ENGINE</span>
            <span class="portal-chip">★ SPECTRUM MONOPOLY SIMULATOR</span>
            <span class="portal-chip">★ WEBGL REAL-TIME GPU SHADERS</span>
            <span class="portal-chip">★ 12-COLOR SPECTRUM RESONANCE</span>
          </div>
        </div>
        <div class="portal-action-block">
          <a href="/games/" class="portal-launch-btn">
            <span>LAUNCH COOL CONCEPT GAMES</span>
            <span class="btn-arrow">↗</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  '''

    # Replace Sections 9 and 9.5 on homepage with portal banner
    content = content[:s_9_marker] + portal_banner + content[s_pillars_marker:]
    print("✔ Replaced Sections 9 & 9.5 on homepage with Cool Concept Games portal banner.")
else:
    print("WARNING: Could not find markers for Section 9 and Section 9.5!")

# -----------------------------------------------------------------------------
# 3. Add Bob Pelloni Repository Ecosystem & Dynamic Spectrum Sliding Circle
# -----------------------------------------------------------------------------
candlestixxx_box_end = '<!-- Candlestixxx GitHub Ecosystem Showcase -->'
if candlestixxx_box_end in content:
    box_start = content.find(candlestixxx_box_end)
    # find closing tag of the github-ecosystem-box
    # It has <div class="github-ecosystem-box"> ... </div>
    box_div_start = content.find('<div class="github-ecosystem-box">', box_start)
    # Find the end of this div (it precedes <div class="uplink-form-col"> or </form>)
    form_col_start = content.find('<div class="uplink-form-col">', box_div_start)
    if form_col_start != -1:
        # The closing tag of github-ecosystem-box is right before the </div> that closes uplink-profile-col
        # Let's find the closing </div> of github-ecosystem-box
        target_insertion = form_col_start
        # Search backwards from form_col_start for </div>\n\n      </div>
        match_div = content[:form_col_start].rfind('</div>')
        # Let's insert Bob's ecosystem and the sliding separator right before uplink-profile-col closes
        # which is right before <div class="uplink-form-col">
        
        separator_and_bob_html = '''
        <!-- =========================================================================
             DYNAMIC SPECTRUM SLIDER SEPARATOR: LUM & BOB SYNERGISTIC REPOSITORY BRIDGE
             Line and circle that slides left to right reflecting the color spectrum
             ========================================================================= -->
        <div class="spectrum-synergy-divider" id="spectrum-synergy-divider" aria-label="Spectral Repository Divider">
          <div class="divider-label-row">
            <span class="div-tag lum-tag">◈ LUM (@CANDLESTIXXX)</span>
            <span class="div-center-msg">⚡ SPECTRAL SYNERGY BRIDGE // CONTINUOUS WAVELENGTH REFLECTION ⚡</span>
            <span class="div-tag bob-tag">BOB (@ROBERBELLONI) ◈</span>
          </div>

          <!-- The Continuous Sliding Rail with 12-Color Gradient -->
          <div class="spectrum-divider-rail">
            <div class="spectrum-rail-gradient"></div>
            <!-- Animated Circle that slides left to right reflecting the color spectrum -->
            <div class="spectrum-sliding-circle" id="spectrum-sliding-circle">
              <div class="sliding-circle-halo"></div>
              <div class="sliding-circle-core"></div>
              <div class="sliding-circle-pip"></div>
            </div>
          </div>
        </div>

        <!-- =========================================================================
             ROBERT PELLONI GITHUB REPOSITORY ECOSYSTEM SHOWCASE
             Directly synchronized with github.com/robertpelloni
             ========================================================================= -->
        <div class="github-ecosystem-box bob-ecosystem-box">
          <div class="gh-header">
            <div class="gh-title-wrap">
              <div class="gh-title">
                <span class="gh-icon" style="color: #00e5ff;">⬢</span>
                <span>GITHUB // ROBERT PELLONI REPOSITORY ECOSYSTEM</span>
              </div>
              <div class="gh-live-badge">
                <span class="gh-live-pip" style="background: #00e5ff; box-shadow: 0 0 8px #00e5ff;"></span>
                <span id="gh-bob-repo-count-text">LIVE REPOSITORIES: 30+ REPOS // SYNCED @ROBERBELLONI</span>
              </div>
            </div>
            <a href="https://github.com/robertpelloni" target="_blank" rel="noopener noreferrer" class="gh-profile-btn bob-profile-btn" title="View Full GitHub Profile @robertpelloni">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <span class="gh-btn-text">VIEW @ROBERBELLONI</span>
              <span>→</span>
            </a>
          </div>
          
          <!-- Primary Featured Repositories Grid -->
          <div class="repo-chips-grid">
            <a href="https://github.com/robertpelloni/libjruntime" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">libjruntime</span> <span class="repo-lang go">GO / C++</span></div>
                <span class="repo-tag">Native Transpiler &amp; Tiny C++ Runtime</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/vst_monster" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">vst_monster</span> <span class="repo-lang svelte">SVELTE / C++</span></div>
                <span class="repo-tag">Audio DSP Synthesis &amp; VST Plugin Host</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/fcdm" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">fcdm</span> <span class="repo-lang py">PYTHON</span></div>
                <span class="repo-tag">Fitness Center Dance Machine Engine</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/CodeWhale-Extensions" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">CodeWhale-Extensions</span> <span class="repo-lang rust">RUST</span></div>
                <span class="repo-tag">Autonomous Community Agent Harness</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/bobtrader" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">bobtrader</span> <span class="repo-lang go">GO</span></div>
                <span class="repo-tag">Autonomous Crypto Predictor &amp; Trader</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/marketing_agent" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">marketing_agent</span> <span class="repo-lang go">GO</span></div>
                <span class="repo-tag">Multi-Channel Growth Automation Agent</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/okgame" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">okgame</span> <span class="repo-lang c">C</span></div>
                <span class="repo-tag">Multiplayer Puzzle Engine &amp; Netcode</span>
              </div>
            </a>
            <a href="https://github.com/robertpelloni/projectm" target="_blank" rel="noopener noreferrer" class="repo-chip">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <div class="repo-chip-inner">
                <div class="repo-row-top"><span class="repo-name">projectm</span> <span class="repo-lang cpp">C++</span></div>
                <span class="repo-tag">Cross-Platform Music Visualizer</span>
              </div>
            </a>
          </div>

          <!-- Bob Expand / See More Bar -->
          <div class="gh-expand-bar">
            <button type="button" class="gh-see-more-btn bob-see-more-btn" id="gh-bob-see-more-btn" title="Click to View All Robert Pelloni Repositories">
              <span class="spectrum-bar bar-left" aria-hidden="true"></span>
              <span class="spectrum-bar bar-right" aria-hidden="true"></span>
              <span class="btn-icon">▼</span>
              <span class="btn-text">VIEW ALL ROBERT PELLONI REPOSITORIES (30+ REPOS)</span>
            </button>
          </div>

          <!-- Collapsible Extended Repositories Container -->
          <div class="gh-collapsible-content" id="gh-bob-collapsible-repos" style="display: none;">
            <div class="repo-chips-grid expanded-grid">
              <a href="https://github.com/robertpelloni/bobfilez" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bobfilez</span> <span class="repo-lang cpp">C++</span></div>
                  <span class="repo-tag">High-Performance File System Organizer</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/bcs" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bcs</span> <span class="repo-lang cpp">C++</span></div>
                  <span class="repo-tag">Cross-Platform Core, GUI, Net &amp; Media</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/geiss" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">geiss</span> <span class="repo-lang cpp">C++</span></div>
                  <span class="repo-tag">Legendary Winamp Music Visualizer</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/bg" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bg</span> <span class="repo-lang cpp">C++</span></div>
                  <span class="repo-tag">Bob's Game Proprietary Native Engine</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/bobmani" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bobmani</span> <span class="repo-lang rust">RUST</span></div>
                  <span class="repo-tag">High-Throughput Vector Graphics Core</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/bgtk" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bgtk</span> <span class="repo-lang c">C</span></div>
                  <span class="repo-tag">Custom Lightweight Graphical Toolkit</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/bob_and_lum_sitcom" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">bob_and_lum_sitcom</span> <span class="repo-lang html">HTML</span></div>
                  <span class="repo-tag">Original Screenplays &amp; Dialogue Scripts</span>
                </div>
              </a>
              <a href="https://github.com/robertpelloni/workspace" target="_blank" rel="noopener noreferrer" class="repo-chip">
                <span class="spectrum-bar bar-left" aria-hidden="true"></span>
                <span class="spectrum-bar bar-right" aria-hidden="true"></span>
                <div class="repo-chip-inner">
                  <div class="repo-row-top"><span class="repo-name">workspace</span> <span class="repo-lang html">HTML / C++</span></div>
                  <span class="repo-tag">Monorepo Developer Workspace</span>
                </div>
              </a>
            </div>
          </div>
        </div>
'''
        # Find where uplink-profile-col ends
        pos_insert = content[:form_col_start].rfind('</div>')
        content = content[:pos_insert] + separator_and_bob_html + content[pos_insert:]
        print("✔ Injected Spectrum Slider Separator and Bob Pelloni's GitHub Ecosystem!")

# -----------------------------------------------------------------------------
# 4. Add "Cool Concept Games" to Navigation Menus & Rails
# -----------------------------------------------------------------------------
# Top Pillars Rail button
games_pillar_btn = '''
      <!-- Pillar: Cool Concept Games -->
      <a href="/games/" class="pillar-shape-btn pillar-games" title="Cool Concept Games: Procedural Shadertoy Engine & Spectrum Monopoly">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">ARCADE</span>
            <span class="pillar-status cyan">GAMES</span>
            <span class="pillar-bricks-tag">[2 SECTORS]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            COOL CONCEPT GAMES
          </div>
          <div class="pillar-sub">SHADERTOY &amp; MONOPOLY ↗</div>
        </div>
      </a>
'''
if 'pillar-games' not in content:
    # Insert right before </nav> of top-pillars-rail
    rail_end = content.find('</nav>', content.find('id="top-pillars-rail"'))
    if rail_end != -1:
        content = content[:rail_end] + games_pillar_btn + '\n    ' + content[rail_end:]
        print("✔ Added Cool Concept Games to top-pillars-rail.")

# Quick Nav Chips
games_nav_chip = '''    <a href="/games/" class="nav-chip chip-games" title="Launch Cool Concept Games Sector">
      <span class="spectrum-bar bar-left"></span>
      <span class="spectrum-bar bar-right"></span>
      <span class="chip-content"><span class="chip-dot"></span>🎮 COOL CONCEPT GAMES ↗</span>
    </a>
'''
if 'chip-games' not in content:
    qnav_start = content.find('<nav class="quick-nav">')
    if qnav_start != -1:
        insert_pos = qnav_start + len('<nav class="quick-nav">\n')
        content = content[:insert_pos] + games_nav_chip + content[insert_pos:]
        print("✔ Added Cool Concept Games chip to quick-nav.")

# -----------------------------------------------------------------------------
# 5. Add CSS for Sliding Circle, Bob Ecosystem, and Arcade Portal Banner
# -----------------------------------------------------------------------------
css_additions = '''
    /* =========================================================================
       DYNAMIC SPECTRUM SLIDER SEPARATOR & BOB PELLONI REPOSITORY ECOSYSTEM
       ========================================================================= */
    .spectrum-synergy-divider {
      margin: 34px 0 24px;
      position: relative;
    }

    .divider-label-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'Courier New', monospace;
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 8px;
    }

    .div-tag.lum-tag { color: #00ff66; font-weight: 800; text-shadow: 0 0 8px rgba(0,255,102,0.6); }
    .div-tag.bob-tag { color: #00e5ff; font-weight: 800; text-shadow: 0 0 8px rgba(0,229,255,0.6); }
    .div-center-msg { color: #ffffff; font-size: 0.68rem; font-weight: 700; text-align: center; }

    .spectrum-divider-rail {
      position: relative;
      height: 8px;
      border-radius: 4px;
      background: #020804;
      border: 1px solid rgba(0, 255, 102, 0.35);
      box-shadow: 0 0 14px rgba(0, 255, 102, 0.2);
      overflow: visible;
    }

    .spectrum-rail-gradient {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 4px;
      background: linear-gradient(90deg, 
        #ff0055 0%, 
        #ff5500 9%, 
        #ffaa00 18%, 
        #ffd700 27%, 
        #ffff00 36%, 
        #aaff00 45%, 
        #00ff66 50%, 
        #00ffaa 55%, 
        #00e5ff 64%, 
        #0066ff 73%, 
        #7b00ff 82%, 
        #ff00aa 100%
      );
      opacity: 0.95;
    }

    .spectrum-sliding-circle {
      position: absolute;
      top: 50%;
      width: 22px;
      height: 22px;
      margin-top: -11px;
      margin-left: -11px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 5;
      animation: spectrumSlideOrbit 6s ease-in-out infinite alternate;
    }

    @keyframes spectrumSlideOrbit {
      0% {
        left: 2%;
        background: #ff0055;
        box-shadow: 0 0 16px #ff0055, 0 0 30px #ff0055;
      }
      20% {
        background: #ffaa00;
        box-shadow: 0 0 16px #ffaa00, 0 0 30px #ffaa00;
      }
      40% {
        background: #ffff00;
        box-shadow: 0 0 16px #ffff00, 0 0 30px #ffff00;
      }
      50% {
        left: 50%;
        background: #00ff66;
        box-shadow: 0 0 20px #00ff66, 0 0 35px #00ff66;
      }
      70% {
        background: #00e5ff;
        box-shadow: 0 0 16px #00e5ff, 0 0 30px #00e5ff;
      }
      90% {
        background: #7b00ff;
        box-shadow: 0 0 16px #7b00ff, 0 0 30px #7b00ff;
      }
      100% {
        left: 98%;
        background: #ff00aa;
        box-shadow: 0 0 16px #ff00aa, 0 0 30px #ff00aa;
      }
    }

    .sliding-circle-core {
      position: absolute;
      top: 4px; left: 4px; right: 4px; bottom: 4px;
      border-radius: 50%;
      background: #ffffff;
      box-shadow: inset 0 0 6px rgba(0,0,0,0.8);
    }

    .sliding-circle-halo {
      position: absolute;
      top: -4px; left: -4px; right: -4px; bottom: -4px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.85);
      animation: circlePulseGlow 1.5s infinite;
    }

    @keyframes circlePulseGlow {
      0%, 100% { transform: scale(1); opacity: 0.9; }
      50% { transform: scale(1.3); opacity: 0.4; }
    }

    /* Bob Ecosystem Box */
    .bob-ecosystem-box {
      border-color: rgba(0, 229, 255, 0.35) !important;
      background: linear-gradient(145deg, rgba(2, 12, 16, 0.88), rgba(1, 6, 8, 0.94)) !important;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), 0 0 24px rgba(0, 229, 255, 0.2) !important;
    }

    .bob-profile-btn {
      border-color: rgba(0, 229, 255, 0.4) !important;
      color: #00e5ff !important;
    }
    .bob-profile-btn:hover {
      border-color: #00e5ff !important;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.5) !important;
    }

    .bob-see-more-btn {
      border-color: rgba(0, 229, 255, 0.4) !important;
      color: #00e5ff !important;
    }
    .bob-see-more-btn:hover {
      background: rgba(0, 229, 255, 0.2) !important;
      border-color: #00e5ff !important;
      box-shadow: 0 0 15px rgba(0, 229, 255, 0.4) !important;
    }

    .repo-lang.go { background: rgba(0, 173, 216, 0.25); color: #00add8; border: 1px solid #00add8; }
    .repo-lang.svelte { background: rgba(255, 62, 0, 0.25); color: #ff3e00; border: 1px solid #ff3e00; }
    .repo-lang.rust { background: rgba(222, 165, 132, 0.25); color: #dea584; border: 1px solid #dea584; }
    .repo-lang.cpp { background: rgba(243, 75, 125, 0.25); color: #f34b7d; border: 1px solid #f34b7d; }
    .repo-lang.c { background: rgba(85, 85, 85, 0.25); color: #9be9a8; border: 1px solid #9be9a8; }

    /* Cool Concept Games Portal Banner */
    .arcade-portal-section {
      margin: 35px 0;
    }

    .portal-card-frame {
      background: linear-gradient(135deg, rgba(4, 20, 14, 0.95), rgba(2, 10, 16, 0.98));
      border: 2px solid #00ff66;
      border-radius: 20px;
      padding: 24px 28px;
      position: relative;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9), 0 0 35px rgba(0, 255, 102, 0.25);
    }

    .portal-glow-bar {
      position: absolute;
      top: 0; left: 10%; right: 10%; height: 2px;
      background: linear-gradient(90deg, transparent, #00ff66, #00e5ff, transparent);
    }

    .portal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(0, 255, 102, 0.25);
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 10px;
    }

    .portal-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      color: #8ce4a7;
      font-family: 'Courier New', monospace;
    }

    .portal-badge-pip {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: crtPulse 1.4s infinite;
    }

    .portal-tag-cyan {
      font-size: 0.68rem;
      color: #00e5ff;
      letter-spacing: 1.2px;
      font-family: 'Courier New', monospace;
      font-weight: 700;
    }

    .portal-body {
      display: flex;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
    }

    .portal-icon-block {
      font-size: 3.5rem;
      width: 72px;
      height: 72px;
      border-radius: 18px;
      background: rgba(0, 255, 102, 0.12);
      border: 1px solid #00ff66;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 25px rgba(0, 255, 102, 0.4);
      flex-shrink: 0;
    }

    .portal-info-block {
      flex: 1;
      min-width: 280px;
    }

    .portal-title {
      margin: 0 0 6px;
      font-size: 1.35rem;
      letter-spacing: 2px;
      color: #00ff66;
      text-shadow: 0 0 12px rgba(0, 255, 102, 0.6);
    }

    .portal-desc {
      margin: 0 0 12px;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #d1fae5;
    }

    .portal-features-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .portal-chip {
      font-size: 0.64rem;
      font-family: 'Courier New', monospace;
      color: #00e5ff;
      background: rgba(0, 229, 255, 0.1);
      border: 1px solid rgba(0, 229, 255, 0.3);
      padding: 4px 10px;
      border-radius: 12px;
    }

    .portal-action-block {
      flex-shrink: 0;
    }

    .portal-launch-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: #00ff66;
      color: #020403;
      font-size: 0.88rem;
      font-weight: 900;
      letter-spacing: 1.5px;
      padding: 14px 24px;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 0 25px rgba(0, 255, 102, 0.6);
      transition: all 0.25s ease;
      text-transform: uppercase;
    }

    .portal-launch-btn:hover {
      background: #ffffff;
      color: #000000;
      box-shadow: 0 0 35px rgba(0, 255, 102, 0.9);
      transform: translateY(-2px) scale(1.02);
    }

    .pillar-games .pillar-status.cyan {
      background: rgba(0, 229, 255, 0.2);
      color: #00e5ff;
      border: 1px solid rgba(0, 229, 255, 0.5);
    }
'''

if '.spectrum-synergy-divider' not in content:
    content = content.replace('</style>', css_additions + '\n    </style>')
    print("✔ Injected CSS for Spectrum Slider Separator and Arcade Portal.")

# -----------------------------------------------------------------------------
# 6. Add JavaScript for Bob's See More Repositories Button
# -----------------------------------------------------------------------------
js_bob_expand = '''
    // =========================================================================
    // BOB PELLONI REPOSITORIES EXPAND / COLLAPSE
    // =========================================================================
    (function() {
      var bobSeeMoreBtn = document.getElementById('gh-bob-see-more-btn');
      var bobCollapsible = document.getElementById('gh-bob-collapsible-repos');
      if (bobSeeMoreBtn && bobCollapsible) {
        bobSeeMoreBtn.addEventListener('click', function() {
          var isHidden = bobCollapsible.style.display === 'none';
          bobCollapsible.style.display = isHidden ? 'block' : 'none';
          var btnText = bobSeeMoreBtn.querySelector('.btn-text');
          var btnIcon = bobSeeMoreBtn.querySelector('.btn-icon');
          if (btnText) {
            btnText.textContent = isHidden ? 'COLLAPSE ROBERT PELLONI REPOSITORIES' : 'VIEW ALL ROBERT PELLONI REPOSITORIES (30+ REPOS)';
          }
          if (btnIcon) {
            btnIcon.textContent = isHidden ? '▲' : '▼';
          }
        });
      }
    })();
'''

if 'gh-bob-see-more-btn' not in content:
    content = content.replace('</script>', js_bob_expand + '\n    </script>')
    print("✔ Injected JS for Bob Pelloni's repository expander.")

# Save updated homepage.html
with open(home_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✔ deploy/homepage.html successfully updated!")

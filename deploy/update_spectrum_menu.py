import os
import re

print("===> [1/4] Loading deploy/homepage.html...")
home_path = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the old #vision-calibration-deck with the new #spectrum-experience-deck
s_deck = content.find('<div id="vision-calibration-deck"')
e_deck = content.find('<!-- Scanline & Ambient Overlay -->')

if s_deck == -1 or e_deck == -1:
    print("ERROR: Could not locate bounds for vision-calibration-deck!")
    exit(1)

new_hero_deck = '''<!-- =========================================================================
       EXPANDABLE SPECTRUM EXPERIENCE MENU (LIGHT / DARK OPTICAL POLARITY)
       Clean, simple, and intuitive expandable controller modeled after the MY LIFE SOUNDS pill
       ========================================================================= -->
  <section id="spectrum-experience-deck" class="spectrum-experience-deck" aria-label="Optical Spectrum Controller">
    <!-- Mini Dock Pill Bar (Visible by default) -->
    <div class="spectrum-hero-pill" id="spectrum-hero-toggle" title="Click to Expand/Collapse Spectrum Experience Menu">
      <div class="spectrum-pill-glyph">
        <span class="glyph-orb" id="hero-glyph-orb">☾</span>
      </div>
      <div class="spectrum-pill-headings">
        <span class="spectrum-kicker">CHOOSE YOUR SPECTRUM EXPERIENCE</span>
        <span class="spectrum-current" id="hero-current-readout">CURRENT: DARK SPECTRUM [OBSIDIAN CYBER]</span>
      </div>
      
      <!-- Direct 1-Click Quick Toggles on the pill -->
      <div class="spectrum-pill-quick-actions" onclick="event.stopPropagation()">
        <button type="button" class="spec-quick-btn mode-dark active" id="hero-btn-dark" data-theme="dark" title="Switch to Dark Spectrum">
          <span class="spec-btn-icon">☾</span> <span class="spec-btn-txt">DARK</span>
        </button>
        <button type="button" class="spec-quick-btn mode-light" id="hero-btn-light" data-theme="light" title="Switch to Light Spectrum">
          <span class="spec-btn-icon">☼</span> <span class="spec-btn-txt">LIGHT</span>
        </button>
      </div>

      <span class="spectrum-hero-arrow" id="hero-arrow-indicator" title="Toggle Expansion">▼</span>
    </div>

    <!-- Expanded Drawer (Smoothly expands down when clicked) -->
    <div class="spectrum-hero-expanded" id="spectrum-hero-expanded" style="display: none;">
      <div class="drawer-top-bar">
        <div class="drawer-status-badge">
          <span class="status-pulse-dot"></span>
          <span>OPTICAL HARMONICS // DUAL SPECTRUM CONTROLLER</span>
        </div>
        <button type="button" class="drawer-close-btn" id="hero-drawer-close" title="Collapse Menu">▲ COLLAPSE</button>
      </div>

      <div class="drawer-hero-text">
        <h3 class="drawer-title">⚡ ⟦ CHOOSE YOUR SPECTRUM EXPERIENCE ⟧</h3>
        <p class="drawer-subtitle">
          Toggle between <strong>Dark Spectrum</strong> and <strong>Light Spectrum</strong> with instant adaptation across all visual layers, contrast ratios, and typography.
        </p>
      </div>

      <div class="spectrum-choice-cards">
        <!-- Dark Spectrum Choice Card -->
        <div class="spec-card card-dark active" id="spec-card-dark" data-theme="dark">
          <div class="spec-card-glow"></div>
          <div class="spec-card-head">
            <span class="spec-card-icon">☾</span>
            <div class="spec-card-meta">
              <h4 class="spec-card-name">DARK SPECTRUM</h4>
              <span class="spec-card-sub">Cyber Obsidian &amp; Phosphor Green</span>
            </div>
            <span class="spec-active-badge" id="badge-dark-active">ACTIVE</span>
          </div>
          <p class="spec-card-copy">
            Deep obsidian background with glowing neon green laser accents. Designed for deep engineering focus, reducing retinal strain, and full cyberpunk ambiance in low-light environments.
          </p>
          <div class="spec-card-stats">
            <span class="stat-pill">WEBER CONTRAST: 9.2:1</span>
            <span class="stat-pill">BACKGROUND: #020403</span>
            <span class="stat-pill">GLOW: #00FF66</span>
          </div>
          <button type="button" class="spec-card-btn" id="card-btn-dark" data-theme="dark">
            ✓ SELECTED (DARK)
          </button>
        </div>

        <!-- Light Spectrum Choice Card -->
        <div class="spec-card card-light" id="spec-card-light" data-theme="light">
          <div class="spec-card-glow"></div>
          <div class="spec-card-head">
            <span class="spec-card-icon">☼</span>
            <div class="spec-card-meta">
              <h4 class="spec-card-name">LIGHT SPECTRUM</h4>
              <span class="spec-card-sub">Reverse Optical Alabaster &amp; Emerald</span>
            </div>
            <span class="spec-active-badge" id="badge-light-active" style="display: none;">ACTIVE</span>
          </div>
          <p class="spec-card-copy">
            Crisp optical alabaster canvas with deep emerald typography. Designed for bright rooms, daylight work sessions, long-form document readability, and glare-free comfort.
          </p>
          <div class="spec-card-stats">
            <span class="stat-pill">WEBER CONTRAST: 12.4:1</span>
            <span class="stat-pill">BACKGROUND: #EDF3EF</span>
            <span class="stat-pill">ACCENT: #007A30</span>
          </div>
          <button type="button" class="spec-card-btn" id="card-btn-light" data-theme="light">
            ACTIVATE LIGHT SPECTRUM
          </button>
        </div>
      </div>

      <!-- Quick Accessibility Preset Row -->
      <div class="spec-drawer-footer">
        <span class="ft-label">ACCESSIBILITY SCALE:</span>
        <div class="ft-button-group">
          <button type="button" class="acuity-node-btn" data-acuity="20-200" title="Enlarged text and maximum contrast for low vision">HIGH CONTRAST (20/200)</button>
          <button type="button" class="acuity-node-btn active" data-acuity="20-20" title="Standard balanced view">BALANCED (20/20)</button>
          <button type="button" class="acuity-node-btn" data-acuity="20-10" title="Fine micro-focus">RAZOR FOCUS (20/10)</button>
        </div>
      </div>
    </div>
  </section>

  '''

content = content[:s_deck] + new_hero_deck + content[e_deck:]
print("✔ Replaced #vision-calibration-deck with new #spectrum-experience-deck.")

# 2. Update the floating HUD to include the companion expandable Spectrum pill alongside MY LIFE SOUNDS
old_audio_aside_start = content.find('<aside id="harmonic-audio-hud"')
if old_audio_aside_start != -1:
    audio_aside_end = content.find('</aside>', old_audio_aside_start) + len('</aside>')
    old_audio_aside = content[old_audio_aside_start:audio_aside_end]

    # Wrap both into a dual-unit cluster
    new_floating_cluster = '''<!-- Floating Unified HUD Console (Spectrum Controller + Harmonic Audio Engine) -->
  <aside id="harmonic-audio-hud" class="harmonic-audio-hud unified-hud-cluster" aria-label="System Quick Controls">
    
    <!-- DOCK PILL 1: SPECTRUM EXPERIENCE (LIGHT / DARK) -->
    <div class="floating-dock-unit" id="dock-spectrum-unit">
      <div class="audio-mini-pill spectrum-float-pill" id="float-spectrum-toggle" title="Click to Expand/Collapse Spectrum Experience">
        <div class="float-spectrum-icon" id="float-spectrum-orb">☾</div>
        <div class="pill-info">
          <span class="pill-title">◐ SPECTRUM</span>
          <span class="pill-meta" id="float-spectrum-status">DARK ☾</span>
        </div>
        <button type="button" class="float-quick-switch" id="float-quick-switch-btn" title="Quick Toggle Light/Dark">☼</button>
        <span class="pill-expand-arrow" id="float-spectrum-arrow">▲</span>
      </div>

      <!-- Floating Spectrum Expanded Drawer -->
      <div class="audio-expanded-panel spectrum-float-expanded" id="float-spectrum-panel" style="display: none;">
        <div class="audio-panel-header">
          <div class="audio-badge">
            <span class="audio-live-dot"></span>
            <span>SPECTRUM // LIGHT &amp; DARK POLARITY</span>
          </div>
          <button type="button" class="audio-collapse-btn" id="float-spectrum-close" title="Collapse Panel">▼</button>
        </div>

        <div class="audio-title-block">
          <h4 class="audio-h4">⚡ ⟦ CHOOSE YOUR SPECTRUM ⟧</h4>
          <div class="audio-creator-tag">UNITEDBEATS.ONLINE // OPTICAL SYSTEM</div>
        </div>

        <div class="float-spectrum-buttons">
          <button type="button" class="float-theme-card theme-dark-card active" id="f-btn-dark" data-theme="dark">
            <div class="ft-card-top"><span class="ft-icon">☾</span> <strong>DARK SPECTRUM</strong></div>
            <div class="ft-card-desc">Obsidian Phosphor • High Focus</div>
          </button>
          <button type="button" class="float-theme-card theme-light-card" id="f-btn-light" data-theme="light">
            <div class="ft-card-top"><span class="ft-icon">☼</span> <strong>LIGHT SPECTRUM</strong></div>
            <div class="ft-card-desc">Alabaster Daylight • Maximum Clarity</div>
          </button>
        </div>
      </div>
    </div>

    <!-- DOCK PILL 2: MY LIFE SOUNDS (AUDIO CONTROLLER) -->
    <div class="floating-dock-unit" id="dock-audio-unit">
''' + old_audio_aside.replace('<aside id="harmonic-audio-hud" class="harmonic-audio-hud" aria-label="Harmonic Audio Controller">', '').replace('</aside>', '') + '''
    </div>
  </aside>'''

    content = content[:old_audio_aside_start] + new_floating_cluster + content[audio_aside_end:]
    print("✔ Updated floating HUD with expandable Spectrum pill and unified cluster.")
else:
    print("WARNING: Could not find old_audio_aside_start")

# 3. Inject CSS for both Expandable Spectrum Menus
new_styles = '''
    /* =========================================================================
       EXPANDABLE SPECTRUM EXPERIENCE CONTROLLER (LIGHT / DARK) STYLES
       ========================================================================= */
    .spectrum-experience-deck {
      max-width: 1060px;
      margin: 18px auto 25px;
      padding: 0 14px;
      position: relative;
      z-index: 10;
      font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Courier New', monospace;
    }

    /* 1. Top Hero Mini Pill */
    .spectrum-hero-pill {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      background: rgba(3, 15, 8, 0.88);
      border: 1px solid rgba(0, 255, 102, 0.4);
      border-radius: 40px;
      padding: 10px 22px 10px 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.85), 0 0 18px rgba(0, 255, 102, 0.22);
      backdrop-filter: blur(14px);
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      user-select: none;
    }

    .spectrum-hero-pill:hover {
      border-color: #00ff66;
      box-shadow: 0 10px 36px rgba(0, 0, 0, 0.9), 0 0 28px rgba(0, 255, 102, 0.45);
      transform: translateY(-2px);
    }

    .spectrum-pill-glyph {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(0, 255, 102, 0.12);
      border: 1px solid #00ff66;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      color: #00ff66;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.4);
    }

    .spectrum-pill-headings {
      display: flex;
      flex-direction: column;
      flex: 1;
      line-height: 1.2;
    }

    .spectrum-kicker {
      font-size: 0.84rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      text-shadow: 0 0 8px rgba(0, 255, 102, 0.5);
    }

    .spectrum-current {
      font-size: 0.72rem;
      color: #a3ffd0;
      letter-spacing: 0.8px;
      font-family: 'Courier New', monospace;
    }

    /* Quick Action Pill Buttons */
    .spectrum-pill-quick-actions {
      display: flex;
      gap: 8px;
      align-items: center;
    }

    .spec-quick-btn {
      background: rgba(0, 255, 102, 0.1);
      border: 1px solid rgba(0, 255, 102, 0.35);
      color: #a3ffd0;
      font-size: 0.74rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      letter-spacing: 1px;
    }

    .spec-quick-btn:hover {
      background: rgba(0, 255, 102, 0.25);
      color: #ffffff;
      border-color: #00ff66;
      box-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
    }

    .spec-quick-btn.active {
      background: #00ff66;
      color: #020403;
      border-color: #00ff66;
      font-weight: 900;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.7);
    }

    .spectrum-hero-arrow {
      color: #00ff66;
      font-size: 0.85rem;
      transition: transform 0.25s ease;
      margin-left: 4px;
    }

    /* 2. Top Hero Expanded Drawer */
    .spectrum-hero-expanded {
      background: linear-gradient(145deg, rgba(3, 16, 9, 0.96), rgba(1, 8, 4, 0.98));
      border: 1px solid rgba(0, 255, 102, 0.5);
      border-radius: 24px;
      padding: 24px 28px;
      margin-top: 14px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.95), 0 0 35px rgba(0, 255, 102, 0.25);
      backdrop-filter: blur(18px);
      animation: panel-slide-down 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes panel-slide-down {
      from { opacity: 0; transform: translateY(-12px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .drawer-top-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(0, 255, 102, 0.2);
      margin-bottom: 16px;
    }

    .drawer-status-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.68rem;
      letter-spacing: 1.5px;
      color: #8ce4a7;
      font-family: 'Courier New', monospace;
    }

    .status-pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: crtPulse 1.4s infinite;
    }

    .drawer-close-btn {
      background: transparent;
      border: 1px solid rgba(0, 255, 102, 0.4);
      color: #00ff66;
      font-size: 0.68rem;
      letter-spacing: 1.2px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 14px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .drawer-close-btn:hover {
      background: rgba(0, 255, 102, 0.2);
      border-color: #00ff66;
      box-shadow: 0 0 10px rgba(0, 255, 102, 0.4);
    }

    .drawer-hero-text {
      text-align: center;
      margin-bottom: 22px;
    }

    .drawer-title {
      margin: 0 0 6px;
      font-size: 1.15rem;
      color: #00ff66;
      letter-spacing: 2px;
      text-shadow: 0 0 12px rgba(0, 255, 102, 0.6);
    }

    .drawer-subtitle {
      margin: 0;
      font-size: 0.86rem;
      color: #d1fae5;
      line-height: 1.5;
    }

    /* 3. The Two High-Impact Spectrum Cards (Easy to Comprehend) */
    .spectrum-choice-cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
      margin-bottom: 20px;
    }

    .spec-card {
      background: rgba(2, 10, 5, 0.85);
      border: 2px solid rgba(0, 255, 102, 0.25);
      border-radius: 16px;
      padding: 20px;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .spec-card:hover {
      border-color: #00ff66;
      box-shadow: 0 10px 30px rgba(0, 255, 102, 0.25);
      transform: translateY(-2px);
    }

    .spec-card.active {
      border-color: #00ff66;
      background: linear-gradient(145deg, rgba(0, 35, 15, 0.9), rgba(1, 14, 6, 0.95));
      box-shadow: 0 12px 35px rgba(0, 255, 102, 0.35), inset 0 0 25px rgba(0, 255, 102, 0.15);
    }

    .spec-card.card-light.active {
      border-color: #00e5ff;
      box-shadow: 0 12px 35px rgba(0, 229, 255, 0.35), inset 0 0 25px rgba(0, 229, 255, 0.15);
    }

    .spec-card-head {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 12px;
    }

    .spec-card-icon {
      font-size: 2rem;
      color: #00ff66;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: rgba(0, 255, 102, 0.15);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(0, 255, 102, 0.5);
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
    }

    .spec-card.card-light .spec-card-icon {
      color: #ffdd55;
      background: rgba(255, 221, 85, 0.15);
      border-color: rgba(255, 221, 85, 0.5);
      box-shadow: 0 0 15px rgba(255, 221, 85, 0.4);
    }

    .spec-card-meta {
      flex: 1;
    }

    .spec-card-name {
      margin: 0 0 2px;
      font-size: 1.05rem;
      letter-spacing: 1.5px;
      color: #ffffff;
      font-weight: 800;
    }

    .spec-card-sub {
      font-size: 0.72rem;
      color: #8ce4a7;
      letter-spacing: 0.8px;
    }

    .spec-active-badge {
      font-size: 0.64rem;
      font-weight: 900;
      letter-spacing: 1.2px;
      padding: 3px 10px;
      border-radius: 12px;
      background: #00ff66;
      color: #020403;
      box-shadow: 0 0 10px #00ff66;
    }

    .spec-card-copy {
      font-size: 0.84rem;
      line-height: 1.55;
      color: #d1fae5;
      margin: 0 0 14px;
    }

    .spec-card-stats {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 16px;
    }

    .stat-pill {
      font-size: 0.62rem;
      font-family: 'Courier New', monospace;
      padding: 3px 8px;
      border-radius: 6px;
      background: rgba(0, 255, 102, 0.08);
      border: 1px solid rgba(0, 255, 102, 0.2);
      color: #a3ffd0;
    }

    .spec-card-btn {
      width: 100%;
      background: rgba(0, 255, 102, 0.15);
      border: 1px solid #00ff66;
      color: #00ff66;
      padding: 10px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      cursor: pointer;
      transition: all 0.2s ease;
      text-transform: uppercase;
    }

    .spec-card:hover .spec-card-btn {
      background: #00ff66;
      color: #020403;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.6);
    }

    .spec-card.active .spec-card-btn {
      background: #00ff66;
      color: #020403;
      box-shadow: 0 0 18px rgba(0, 255, 102, 0.7);
    }

    .spec-card.card-light.active .spec-card-btn {
      background: #00e5ff;
      color: #020403;
      border-color: #00e5ff;
      box-shadow: 0 0 18px rgba(0, 229, 255, 0.7);
    }

    /* Fine Tune Footer */
    .spec-drawer-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      padding-top: 14px;
      border-top: 1px solid rgba(0, 255, 102, 0.2);
    }

    .ft-label {
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      color: #8ce4a7;
      font-family: 'Courier New', monospace;
    }

    .ft-button-group {
      display: flex;
      gap: 6px;
    }

    .ft-button-group .acuity-node-btn {
      font-size: 0.68rem;
      padding: 5px 12px;
      border-radius: 12px;
      border: 1px solid rgba(0, 255, 102, 0.3);
      background: rgba(0, 255, 102, 0.08);
      color: #a3ffd0;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .ft-button-group .acuity-node-btn:hover,
    .ft-button-group .acuity-node-btn.active {
      background: #00ff66;
      color: #020403;
      border-color: #00ff66;
      font-weight: 800;
    }

    /* 4. Unified Floating Dock Cluster Styles */
    .unified-hud-cluster {
      display: flex;
      gap: 12px;
      align-items: flex-end;
    }

    .floating-dock-unit {
      position: relative;
    }

    .float-spectrum-icon {
      font-size: 1.1rem;
      color: #00ff66;
      text-shadow: 0 0 8px #00ff66;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .float-quick-switch {
      background: rgba(0, 255, 102, 0.15);
      border: 1px solid #00ff66;
      color: #00ff66;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 0.88rem;
      transition: all 0.2s ease;
    }

    .float-quick-switch:hover {
      background: #00ff66;
      color: #020403;
      box-shadow: 0 0 10px #00ff66;
      transform: scale(1.08);
    }

    .spectrum-float-expanded {
      width: 320px;
    }

    .float-spectrum-buttons {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 10px;
    }

    .float-theme-card {
      background: rgba(3, 16, 9, 0.85);
      border: 1px solid rgba(0, 255, 102, 0.3);
      border-radius: 10px;
      padding: 10px 14px;
      text-align: left;
      cursor: pointer;
      color: #ffffff;
      transition: all 0.2s ease;
    }

    .float-theme-card:hover {
      border-color: #00ff66;
      background: rgba(0, 255, 102, 0.15);
      transform: translateX(3px);
    }

    .float-theme-card.active {
      border-color: #00ff66;
      background: linear-gradient(135deg, rgba(0, 45, 18, 0.9), rgba(1, 20, 8, 0.95));
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.35);
    }

    .ft-card-top {
      font-size: 0.82rem;
      letter-spacing: 1px;
      color: #00ff66;
      margin-bottom: 2px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .theme-light-card .ft-card-top {
      color: #00e5ff;
    }

    .ft-card-desc {
      font-size: 0.68rem;
      color: #a3ffd0;
    }

    /* =========================================================================
       LIGHT MODE ADAPTATION FOR SPECTRUM EXPANDABLE MENUS
       ========================================================================= */
    body[data-theme="light"] .spectrum-hero-pill {
      background: rgba(255, 255, 255, 0.95);
      border-color: rgba(0, 122, 48, 0.4);
      box-shadow: 0 8px 30px rgba(0, 60, 20, 0.12);
    }

    body[data-theme="light"] .spectrum-kicker {
      color: #007a30;
      text-shadow: none;
    }

    body[data-theme="light"] .spectrum-current {
      color: #2e5a3c;
    }

    body[data-theme="light"] .spec-quick-btn {
      background: rgba(0, 122, 48, 0.08);
      border-color: rgba(0, 122, 48, 0.3);
      color: #007a30;
    }

    body[data-theme="light"] .spec-quick-btn.active {
      background: #007a30;
      color: #ffffff;
      border-color: #007a30;
      box-shadow: 0 4px 14px rgba(0, 122, 48, 0.3);
    }

    body[data-theme="light"] .spectrum-hero-expanded {
      background: #ffffff;
      border-color: rgba(0, 122, 48, 0.3);
      box-shadow: 0 20px 50px rgba(0, 60, 20, 0.15);
    }

    body[data-theme="light"] .drawer-title {
      color: #007a30;
      text-shadow: none;
    }

    body[data-theme="light"] .drawer-subtitle {
      color: #2b3a30;
    }

    body[data-theme="light"] .spec-card {
      background: #f8faf9;
      border-color: rgba(0, 122, 48, 0.25);
    }

    body[data-theme="light"] .spec-card-name {
      color: #0a1f12;
    }

    body[data-theme="light"] .spec-card-copy {
      color: #2b3a30;
    }

    body[data-theme="light"] .spec-card.active {
      background: #f0f7f2;
      border-color: #007a30;
      box-shadow: 0 10px 25px rgba(0, 122, 48, 0.18);
    }

    body[data-theme="light"] .spec-card.active .spec-card-btn {
      background: #007a30;
      color: #ffffff;
    }
'''

if '.spectrum-experience-deck' not in content:
    content = content.replace('</style>', new_styles + '\n    </style>')
    print("✔ Injected CSS for Expandable Spectrum Menu.")

# 4. Inject JavaScript event listeners and sync handler for both Expandable Spectrum Menus
new_js = '''
    // =========================================================================
    // EXPANDABLE SPECTRUM EXPERIENCE CONTROLLER LOGIC (LIGHT / DARK POLARITY)
    // Synchronized between Top Hero Expandable Menu and Floating Dock Pill
    // =========================================================================
    (function initSpectrumExpander() {
      // Top Hero Menu Elements
      var heroToggle = document.getElementById('spectrum-hero-toggle');
      var heroDrawer = document.getElementById('spectrum-hero-expanded');
      var heroClose = document.getElementById('hero-drawer-close');
      var heroArrow = document.getElementById('hero-arrow-indicator');
      var heroBtnDark = document.getElementById('hero-btn-dark');
      var heroBtnLight = document.getElementById('hero-btn-light');
      var heroCurrentReadout = document.getElementById('hero-current-readout');
      var heroGlyph = document.getElementById('hero-glyph-orb');
      var cardDark = document.getElementById('spec-card-dark');
      var cardLight = document.getElementById('spec-card-light');
      var cardBtnDark = document.getElementById('card-btn-dark');
      var cardBtnLight = document.getElementById('card-btn-light');
      var badgeDark = document.getElementById('badge-dark-active');
      var badgeLight = document.getElementById('badge-light-active');

      // Floating Dock Elements
      var floatToggle = document.getElementById('float-spectrum-toggle');
      var floatDrawer = document.getElementById('float-spectrum-panel');
      var floatClose = document.getElementById('float-spectrum-close');
      var floatArrow = document.getElementById('float-spectrum-arrow');
      var floatQuickSwitch = document.getElementById('float-quick-switch-btn');
      var floatStatus = document.getElementById('float-spectrum-status');
      var floatOrb = document.getElementById('float-spectrum-orb');
      var fBtnDark = document.getElementById('f-btn-dark');
      var fBtnLight = document.getElementById('f-btn-light');

      // Expand / Collapse Top Hero Drawer
      if (heroToggle && heroDrawer) {
        heroToggle.addEventListener('click', function(e) {
          var isExpanded = heroDrawer.style.display !== 'none';
          heroDrawer.style.display = isExpanded ? 'none' : 'block';
          if (heroArrow) heroArrow.textContent = isExpanded ? '▼' : '▲';
        });
      }

      if (heroClose && heroDrawer) {
        heroClose.addEventListener('click', function() {
          heroDrawer.style.display = 'none';
          if (heroArrow) heroArrow.textContent = '▼';
        });
      }

      // Expand / Collapse Floating Drawer
      if (floatToggle && floatDrawer) {
        floatToggle.addEventListener('click', function(e) {
          if (e.target === floatQuickSwitch) return;
          var isExpanded = floatDrawer.style.display !== 'none';
          floatDrawer.style.display = isExpanded ? 'none' : 'block';
          if (floatArrow) floatArrow.textContent = isExpanded ? '▲' : '▼';
        });
      }

      if (floatClose && floatDrawer) {
        floatClose.addEventListener('click', function() {
          floatDrawer.style.display = 'none';
          if (floatArrow) floatArrow.textContent = '▲';
        });
      }

      // Master Synchronized Switcher
      function switchSpectrumTheme(theme) {
        if (typeof applyTheme === 'function') {
          applyTheme(theme);
        } else {
          document.documentElement.setAttribute('data-theme', theme);
          document.body.setAttribute('data-theme', theme);
        }

        var isDark = (theme === 'dark');

        // Update Top Hero UI
        if (heroGlyph) heroGlyph.textContent = isDark ? '☾' : '☼';
        if (heroCurrentReadout) {
          heroCurrentReadout.textContent = isDark ? 'CURRENT: DARK SPECTRUM [OBSIDIAN CYBER]' : 'CURRENT: LIGHT SPECTRUM [OPTICAL ALABASTER]';
        }
        if (heroBtnDark) {
          if (isDark) heroBtnDark.classList.add('active'); else heroBtnDark.classList.remove('active');
        }
        if (heroBtnLight) {
          if (!isDark) heroBtnLight.classList.add('active'); else heroBtnLight.classList.remove('active');
        }
        if (cardDark) {
          if (isDark) cardDark.classList.add('active'); else cardDark.classList.remove('active');
        }
        if (cardLight) {
          if (!isDark) cardLight.classList.add('active'); else cardLight.classList.remove('active');
        }
        if (badgeDark) badgeDark.style.display = isDark ? 'inline-block' : 'none';
        if (badgeLight) badgeLight.style.display = !isDark ? 'inline-block' : 'none';
        if (cardBtnDark) cardBtnDark.textContent = isDark ? '✓ SELECTED (DARK)' : 'ACTIVATE DARK SPECTRUM';
        if (cardBtnLight) cardBtnLight.textContent = !isDark ? '✓ SELECTED (LIGHT)' : 'ACTIVATE LIGHT SPECTRUM';

        // Update Floating Dock UI
        if (floatOrb) floatOrb.textContent = isDark ? '☾' : '☼';
        if (floatStatus) floatStatus.textContent = isDark ? 'DARK ☾' : 'LIGHT ☼';
        if (floatQuickSwitch) floatQuickSwitch.textContent = isDark ? '☼' : '☾';
        if (fBtnDark) {
          if (isDark) fBtnDark.classList.add('active'); else fBtnDark.classList.remove('active');
        }
        if (fBtnLight) {
          if (!isDark) fBtnLight.classList.add('active'); else fBtnLight.classList.remove('active');
        }
      }

      // Attach Click Handlers to All Polarity Triggers
      if (heroBtnDark) heroBtnDark.addEventListener('click', function() { switchSpectrumTheme('dark'); });
      if (heroBtnLight) heroBtnLight.addEventListener('click', function() { switchSpectrumTheme('light'); });
      if (cardDark) cardDark.addEventListener('click', function() { switchSpectrumTheme('dark'); });
      if (cardLight) cardLight.addEventListener('click', function() { switchSpectrumTheme('light'); });
      if (cardBtnDark) cardBtnDark.addEventListener('click', function(e) { e.stopPropagation(); switchSpectrumTheme('dark'); });
      if (cardBtnLight) cardBtnLight.addEventListener('click', function(e) { e.stopPropagation(); switchSpectrumTheme('light'); });

      if (floatQuickSwitch) {
        floatQuickSwitch.addEventListener('click', function(e) {
          e.stopPropagation();
          var current = document.documentElement.getAttribute('data-theme') || 'dark';
          switchSpectrumTheme(current === 'dark' ? 'light' : 'dark');
        });
      }

      if (fBtnDark) fBtnDark.addEventListener('click', function() { switchSpectrumTheme('dark'); });
      if (fBtnLight) fBtnLight.addEventListener('click', function() { switchSpectrumTheme('light'); });

      // Initialize with active theme
      var activeTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      switchSpectrumTheme(activeTheme);
    })();
'''

if 'initSpectrumExpander' not in content:
    content = content.replace('</script>', new_js + '\n    </script>')
    print("✔ Injected JS for Expandable Spectrum Menu.")

# Save updated homepage.html
with open(home_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✔ deploy/homepage.html successfully updated!")

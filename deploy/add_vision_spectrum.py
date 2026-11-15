import os
import re

vision_deck_html = '''
  <!-- =========================================================================
       OPTICAL VISION SPECTRUM & ACUITY CALIBRATION DECK (20/200 -> 20/20 -> 20/10)
       ========================================================================= -->
  <div id="vision-calibration-deck" class="vision-calibration-deck">
    <div class="vision-deck-frame">
      <div class="vision-deck-scanlines"></div>

      <!-- Top Status & Directive Bar -->
      <div class="vision-deck-topbar">
        <div class="vision-badge">
          <span class="vision-pulse-dot"></span>
          <span class="vision-badge-code">OPTICAL_HUD v3.4 // SPECTRUM ENGINE</span>
        </div>
        <div class="vision-headline">
          CHOOSE YOUR SPECTRUM EXPERIENCE // VISION ACUITY &amp; CONTRAST CALIBRATION
        </div>
        <div class="vision-telemetry" id="vision-live-telemetry">
          ACUITY: <span class="val-acuity">20/20</span> | POLARITY: <span class="val-polarity">DARK_SPECTRUM</span> | WEBER: <span class="val-contrast">9.2:1</span>
        </div>
      </div>

      <!-- Controls Grid: Acuity Gauge + Polarity Toggle -->
      <div class="vision-deck-controls">
        
        <!-- Module 1: 3-Stage Mathematical Acuity Gauge (20/200 -> 20/20 -> 20/10) -->
        <div class="vision-module vision-acuity-module">
          <div class="module-label">
            <span class="mod-icon">👁</span>
            <span>VISUAL ACUITY &amp; PRESCRIPTION FOCUS:</span>
          </div>

          <div class="acuity-gauge-track">
            <!-- Calibrated Acuity Selector Buttons -->
            <button type="button" class="acuity-node-btn" data-acuity="20-200" title="High-Contrast Macro Mode for Low Vision / Eye Fatigue (20/200 to 20/70)">
              <span class="node-grade">20/200</span>
              <span class="node-name">MACRO CONTRAST</span>
              <span class="node-spec">High Stroke // Anti-Strain</span>
            </button>

            <button type="button" class="acuity-node-btn active" data-acuity="20-20" title="Standard Harmonic Spectrum for 20/20 Corrected Vision">
              <span class="node-grade">20/20</span>
              <span class="node-name">BALANCED EQUILIBRIUM</span>
              <span class="node-spec">Nominal Dispersion</span>
            </button>

            <button type="button" class="acuity-node-btn" data-acuity="20-10" title="Hyper-Acuity Laser Focus for 20/10 Vision &amp; High-DPI Displays">
              <span class="node-grade">20/10</span>
              <span class="node-name">HYPER-ACUITY</span>
              <span class="node-spec">Razor Micro-Vector</span>
            </button>
          </div>

          <div class="acuity-gauge-meter">
            <div class="acuity-gauge-slider" id="acuity-gauge-slider">
              <div class="slider-pip"></div>
            </div>
            <div class="gauge-scale-ticks">
              <span>20/200 (MAR 10.0\')</span>
              <span>20/70</span>
              <span>20/40</span>
              <span>20/20 (MAR 1.0\')</span>
              <span>20/15</span>
              <span>20/10 (MAR 0.5\')</span>
            </div>
          </div>
        </div>

        <!-- Module 2: Luminance Spectrum Polarity (Dark Obsidian vs Reverse Light Alabaster) -->
        <div class="vision-module vision-polarity-module">
          <div class="module-label">
            <span class="mod-icon">◐</span>
            <span>SPECTRUM LUMINANCE POLARITY:</span>
          </div>

          <div class="polarity-toggle-group">
            <button type="button" class="polarity-btn active" data-theme="dark" title="Dark Spectrum: Deep obsidian background with phosphor neon laser illumination">
              <span class="pol-icon">☾</span>
              <div class="pol-info">
                <span class="pol-title">DARK SPECTRUM</span>
                <span class="pol-desc">Obsidian Phosphor // Cyber Terminal</span>
              </div>
            </button>

            <button type="button" class="polarity-btn" data-theme="light" title="Light Spectrum: Eye-soothing reverse optical alabaster contrast with jewel-tone spectrum">
              <span class="pol-icon">☼</span>
              <div class="pol-info">
                <span class="pol-title">LIGHT SPECTRUM</span>
                <span class="pol-desc">Reverse Optical Alabaster // Zero-Glare</span>
              </div>
            </button>
          </div>

          <div class="polarity-spectrum-preview">
            <span class="spectrum-dot dot-1"></span>
            <span class="spectrum-dot dot-2"></span>
            <span class="spectrum-dot dot-3"></span>
            <span class="spectrum-dot dot-4"></span>
            <span class="spectrum-dot dot-5"></span>
            <span class="spectrum-dot dot-6" title="Green Center Anchor 50%"></span>
            <span class="spectrum-dot dot-7"></span>
            <span class="spectrum-dot dot-8"></span>
            <span class="spectrum-dot dot-9"></span>
            <span class="spectrum-dot dot-10"></span>
            <span class="spectrum-dot dot-11"></span>
            <span class="spectrum-dot dot-12"></span>
          </div>
        </div>

      </div>
    </div>
  </div>
'''

vision_css = '''
    /* =========================================================================
       OPTICAL VISION SPECTRUM & ACUITY ENGINE STYLING
       ========================================================================= */
    .vision-calibration-deck {
      margin-bottom: 20px;
      position: relative;
      z-index: 10;
    }

    .vision-deck-frame {
      position: relative;
      background: radial-gradient(circle at 50% 0%, rgba(0, 229, 255, 0.08) 0%, rgba(2, 6, 4, 0.98) 80%);
      border: 2px solid #00ff66;
      border-radius: 8px;
      padding: 16px 20px;
      box-shadow: 0 0 25px rgba(0, 255, 102, 0.2), inset 0 0 20px rgba(0, 0, 0, 0.9);
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .vision-deck-scanlines {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(rgba(0, 255, 102, 0.03) 50%, rgba(0, 0, 0, 0.3) 50%);
      background-size: 100% 4px;
      pointer-events: none;
    }

    .vision-deck-topbar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid #14442a;
    }

    .vision-badge {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .vision-pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
      animation: pulse-dot 1.4s infinite;
    }

    .vision-badge-code {
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #00ff66;
      text-shadow: 0 0 8px rgba(0, 255, 102, 0.6);
    }

    .vision-headline {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #ffffff;
      text-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
    }

    .vision-telemetry {
      font-size: 0.72rem;
      letter-spacing: 1px;
      color: #00e5ff;
      font-weight: 700;
      font-family: inherit;
    }

    .vision-telemetry span {
      color: #e5ff80;
    }

    .vision-deck-controls {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 20px;
      position: relative;
      z-index: 2;
    }

    @media (max-width: 900px) {
      .vision-deck-controls {
        grid-template-columns: 1fr;
      }
    }

    .vision-module {
      background: rgba(3, 10, 6, 0.75);
      border: 1px solid #174e2d;
      border-radius: 6px;
      padding: 12px 14px;
    }

    .module-label {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #4ef38d;
      margin-bottom: 10px;
    }

    .mod-icon {
      font-size: 0.9rem;
    }

    /* Acuity Selector Track */
    .acuity-gauge-track {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin-bottom: 10px;
    }

    .acuity-node-btn {
      background: rgba(0, 20, 10, 0.85);
      border: 1px solid #1c5e37;
      border-radius: 4px;
      padding: 8px 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .acuity-node-btn:hover {
      border-color: #00ff66;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.3);
      transform: translateY(-1px);
    }

    .acuity-node-btn.active {
      background: rgba(0, 255, 102, 0.18);
      border-color: #00ff66;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.4), inset 0 0 10px rgba(0, 255, 102, 0.2);
    }

    .node-grade {
      font-size: 1.05rem;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 1px;
    }

    .acuity-node-btn.active .node-grade {
      color: #00ff66;
      text-shadow: 0 0 8px #00ff66;
    }

    .node-name {
      font-size: 0.65rem;
      font-weight: 800;
      color: #00e5ff;
      letter-spacing: 1px;
      margin: 2px 0;
    }

    .node-spec {
      font-size: 0.58rem;
      color: #8ce4a7;
    }

    /* Acuity Meter & Slider Track */
    .acuity-gauge-meter {
      position: relative;
      margin-top: 6px;
    }

    .acuity-gauge-slider {
      height: 8px;
      background: linear-gradient(90deg, #ffaa00 0%, #00ff66 50%, #00e5ff 100%);
      border-radius: 4px;
      position: relative;
      box-shadow: inset 0 0 6px rgba(0,0,0,0.8);
    }

    .slider-pip {
      position: absolute;
      top: -4px;
      left: 50%;
      transform: translateX(-50%);
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: #ffffff;
      border: 2px solid #00ff66;
      box-shadow: 0 0 10px #00ff66;
      transition: left 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .gauge-scale-ticks {
      display: flex;
      justify-content: space-between;
      margin-top: 6px;
      font-size: 0.58rem;
      color: #8ce4a7;
      font-weight: 700;
    }

    /* Polarity Toggle Group (Dark vs Light Reverse) */
    .polarity-toggle-group {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 12px;
    }

    .polarity-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      border-radius: 6px;
      background: rgba(0, 20, 10, 0.85);
      border: 1px solid #1c5e37;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: inherit;
      text-align: left;
    }

    .polarity-btn:hover {
      border-color: #00ff66;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.3);
      transform: translateY(-1px);
    }

    .polarity-btn.active {
      border-color: #00ff66;
      background: rgba(0, 255, 102, 0.18);
      box-shadow: 0 0 16px rgba(0, 255, 102, 0.4), inset 0 0 10px rgba(0, 255, 102, 0.2);
    }

    .pol-icon {
      font-size: 1.3rem;
      color: #00ff66;
      text-shadow: 0 0 8px #00ff66;
    }

    .polarity-btn.active .pol-icon {
      color: #ffffff;
      text-shadow: 0 0 12px #00ff66;
    }

    .pol-info {
      display: flex;
      flex-direction: column;
    }

    .pol-title {
      font-size: 0.78rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1px;
    }

    .polarity-btn.active .pol-title {
      color: #00ff66;
    }

    .pol-desc {
      font-size: 0.62rem;
      color: #8ce4a7;
      line-height: 1.3;
    }

    .polarity-spectrum-preview {
      display: flex;
      height: 6px;
      border-radius: 3px;
      overflow: hidden;
      gap: 2px;
    }

    .spectrum-dot {
      flex: 1;
      height: 100%;
    }
    .dot-1 { background: #ff0033; }
    .dot-2 { background: #ff3d00; }
    .dot-3 { background: #ff7700; }
    .dot-4 { background: #ffaa00; }
    .dot-5 { background: #ffe600; }
    .dot-6 { background: #b4e600; } /* Pear */
    .dot-7 { background: #00ff66; } /* Green 50% */
    .dot-8 { background: #00f0aa; }
    .dot-9 { background: #00e5ff; }
    .dot-10 { background: #0077ff; }
    .dot-11 { background: #5800ff; }
    .dot-12 { background: #e00099; }

    /* =========================================================================
       LIGHT MODE // REVERSE OPTICAL ALABASTER CONTRAST SPECTRUM
       ========================================================================= */
    body.theme-light,
    .theme-light html,
    html[data-theme="light"],
    body[data-theme="light"],
    [data-theme="light"] {
      background-color: #f1f5f2 !important;
      color: #0a2615 !important;
    }

    body[data-theme="light"] .nexus-terminal,
    body.theme-light .nexus-terminal {
      background: #f1f5f2 !important;
      color: #082112 !important;
    }

    /* Light Mode Overrides for Global Theme Elements */
    body[data-theme="light"] html,
    body[data-theme="light"] body,
    body[data-theme="light"] .wp-site-blocks,
    body[data-theme="light"] main,
    body[data-theme="light"] .entry-content,
    body[data-theme="light"] .wp-block-group {
      background-color: #f1f5f2 !important;
      color: #082112 !important;
    }

    body[data-theme="light"] .terminal-scanlines {
      opacity: 0.05 !important;
      background: linear-gradient(rgba(0, 100, 40, 0.04) 50%, rgba(240, 245, 242, 0.4) 50%) !important;
    }

    body[data-theme="light"] .vision-deck-frame {
      background: radial-gradient(circle at 50% 0%, rgba(0, 140, 60, 0.08) 0%, #ffffff 85%) !important;
      border-color: #008a38 !important;
      box-shadow: 0 4px 20px rgba(0, 100, 40, 0.12), inset 0 0 15px rgba(240, 245, 242, 0.8) !important;
    }

    body[data-theme="light"] .vision-deck-topbar {
      border-bottom-color: #a3d9b8 !important;
    }

    body[data-theme="light"] .vision-headline {
      color: #041a0d !important;
      text-shadow: none !important;
    }

    body[data-theme="light"] .vision-badge-code {
      color: #007a30 !important;
      text-shadow: none !important;
    }

    body[data-theme="light"] .vision-telemetry {
      color: #005577 !important;
    }

    body[data-theme="light"] .vision-telemetry span {
      color: #007a30 !important;
    }

    body[data-theme="light"] .vision-module {
      background: #f5f9f6 !important;
      border-color: #9cd3b2 !important;
    }

    body[data-theme="light"] .module-label {
      color: #006b2b !important;
    }

    body[data-theme="light"] .acuity-node-btn {
      background: #ffffff !important;
      border-color: #a8d6bc !important;
    }

    body[data-theme="light"] .acuity-node-btn .node-grade {
      color: #061d11 !important;
    }

    body[data-theme="light"] .acuity-node-btn .node-name {
      color: #006688 !important;
    }

    body[data-theme="light"] .acuity-node-btn .node-spec {
      color: #0f4f2c !important;
    }

    body[data-theme="light"] .acuity-node-btn.active {
      background: #d8f3e2 !important;
      border-color: #008a38 !important;
      box-shadow: 0 0 12px rgba(0, 138, 56, 0.25) !important;
    }

    body[data-theme="light"] .acuity-node-btn.active .node-grade {
      color: #007a30 !important;
      text-shadow: none !important;
    }

    body[data-theme="light"] .polarity-btn {
      background: #ffffff !important;
      border-color: #a8d6bc !important;
    }

    body[data-theme="light"] .polarity-btn .pol-title {
      color: #061d11 !important;
    }

    body[data-theme="light"] .polarity-btn .pol-icon {
      color: #007a30 !important;
      text-shadow: none !important;
    }

    body[data-theme="light"] .polarity-btn .pol-desc {
      color: #124d29 !important;
    }

    body[data-theme="light"] .polarity-btn.active {
      background: #d8f3e2 !important;
      border-color: #008a38 !important;
      box-shadow: 0 0 12px rgba(0, 138, 56, 0.25) !important;
    }

    body[data-theme="light"] .hud-bar {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
      box-shadow: 0 2px 10px rgba(0, 80, 30, 0.08) !important;
    }

    body[data-theme="light"] .hud-label {
      color: #006b2b !important;
    }

    body[data-theme="light"] .hud-val {
      color: #03140a !important;
    }

    body[data-theme="light"] .ascii-hero {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
      box-shadow: 0 4px 20px rgba(0, 80, 30, 0.08) !important;
    }

    body[data-theme="light"] .ascii-art {
      color: #007a30 !important;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1) !important;
    }

    body[data-theme="light"] .hero-tagline {
      color: #061d11 !important;
    }

    body[data-theme="light"] .terminal-section {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
      box-shadow: 0 4px 18px rgba(0, 80, 30, 0.08) !important;
    }

    body[data-theme="light"] .section-badge {
      color: #006b2b !important;
    }

    body[data-theme="light"] .section-title {
      color: #020d07 !important;
    }

    body[data-theme="light"] .terminal-callout {
      background: #f4f9f6 !important;
      border-color: #008a38 !important;
      color: #082112 !important;
    }

    body[data-theme="light"] .lead-text {
      color: #041209 !important;
    }

    body[data-theme="light"] p {
      color: #082112 !important;
    }

    body[data-theme="light"] .cyber-card {
      background: #f9fcf9 !important;
      border-color: #9cd3b2 !important;
      box-shadow: 0 2px 12px rgba(0, 60, 20, 0.06) !important;
    }

    body[data-theme="light"] .card-meta {
      border-bottom-color: #d1eadb !important;
    }

    body[data-theme="light"] .founder-role {
      color: #006688 !important;
    }

    body[data-theme="light"] .founder-bio p {
      color: #061a0f !important;
    }

    body[data-theme="light"] .skills-list li {
      color: #082415 !important;
    }

    body[data-theme="light"] .skills-list .bullet {
      color: #007a30 !important;
    }

    body[data-theme="light"] .nav-chip {
      background: #ffffff !important;
      color: #061d11 !important;
      border-color: #a8d6bc !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
    }

    body[data-theme="light"] .nav-chip:hover {
      background: #e2f5e9 !important;
      border-color: #008a38 !important;
      color: #005a20 !important;
    }

    body[data-theme="light"] .cyber-input,
    body[data-theme="light"] .cyber-textarea,
    body[data-theme="light"] .term-input,
    body[data-theme="light"] .term-textarea,
    body[data-theme="light"] .vault-text-input {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
      color: #031207 !important;
    }

    body[data-theme="light"] .cyber-btn {
      background: #007a30 !important;
      color: #ffffff !important;
      border-color: #005a20 !important;
      box-shadow: 0 2px 10px rgba(0, 122, 48, 0.3) !important;
    }

    body[data-theme="light"] .cyber-btn:hover {
      background: #00993c !important;
      color: #ffffff !important;
    }

    body[data-theme="light"] .cyber-table th {
      background: #e2f5e9 !important;
      color: #006b2b !important;
      border-bottom-color: #008a38 !important;
    }

    body[data-theme="light"] .cyber-table td {
      border-bottom-color: #d1eadb !important;
      color: #082112 !important;
    }

    body[data-theme="light"] .terminal-footer {
      background: #e6efe9 !important;
      border-color: #8ecea8 !important;
      color: #0f4f2c !important;
    }

    body[data-theme="light"] .sub-dock-matrix {
      background: #ffffff !important;
      border-color: #008a38 !important;
      box-shadow: 0 6px 25px rgba(0, 80, 30, 0.1) !important;
    }

    body[data-theme="light"] .sub-dock-ticker-bar {
      background: #e5f6eb !important;
      border-color: #008a38 !important;
    }

    body[data-theme="light"] .sub-dock-card {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
    }

    body[data-theme="light"] .sub-card-desc {
      color: #082112 !important;
    }

    body[data-theme="light"] .continuum-manifesto-box {
      background: radial-gradient(circle at 50% 0%, #e1f7fc 0%, #ffffff 85%) !important;
      border-color: #0088aa !important;
      box-shadow: 0 4px 20px rgba(0, 136, 170, 0.15) !important;
    }

    body[data-theme="light"] .manifesto-headline {
      color: #021a22 !important;
      text-shadow: none !important;
    }

    body[data-theme="light"] .manifesto-body,
    body[data-theme="light"] .manifesto-sub {
      color: #052618 !important;
    }

    body[data-theme="light"] .diary-entry-card {
      background: #ffffff !important;
      border-color: #8ecea8 !important;
    }

    body[data-theme="light"] .entry-title {
      color: #020d07 !important;
    }

    body[data-theme="light"] .entry-text p {
      color: #082112 !important;
    }

    body[data-theme="light"] .diary-broadcast-terminal {
      background: #ffffff !important;
      border-color: #0088aa !important;
    }

    body[data-theme="light"] .terminal-intro {
      color: #082112 !important;
    }

    /* =========================================================================
       MATHEMATICAL ACUITY PROFILES: 20/200, 20/20, 20/10
       ========================================================================= */

    /* 1. 20/200 Acuity Profile (High Contrast Macro Readability) */
    body[data-acuity="20-200"],
    [data-acuity="20-200"] {
      font-size: 110% !important;
      font-weight: 600 !important;
      letter-spacing: 0.5px !important;
      line-height: 1.8 !important;
    }

    body[data-acuity="20-200"] p,
    body[data-acuity="20-200"] .lead-text,
    body[data-acuity="20-200"] .entry-text p,
    body[data-acuity="20-200"] .sub-card-desc,
    body[data-acuity="20-200"] .proj-desc {
      font-size: 1.05rem !important;
      line-height: 1.85 !important;
      font-weight: 600 !important;
    }

    body[data-acuity="20-200"] .terminal-section,
    body[data-acuity="20-200"] .cyber-card,
    body[data-acuity="20-200"] .sub-dock-card,
    body[data-acuity="20-200"] .diary-entry-card {
      border-width: 2.5px !important;
    }

    /* 2. 20/20 Acuity Profile (Nominal Harmonic Baseline) */
    body[data-acuity="20-20"],
    [data-acuity="20-20"] {
      font-size: 100% !important;
      font-weight: normal !important;
      letter-spacing: normal !important;
      line-height: normal !important;
    }

    /* 3. 20/10 Acuity Profile (Hyper-Acuity Razor Neon Field) */
    body[data-acuity="20-10"],
    [data-acuity="20-10"] {
      font-size: 96% !important;
      letter-spacing: 0.25px !important;
    }

    body[data-acuity="20-10"] .terminal-section,
    body[data-acuity="20-10"] .cyber-card,
    body[data-acuity="20-10"] .sub-dock-card,
    body[data-acuity="20-10"] .diary-entry-card {
      border-width: 1px !important;
    }
'''

vision_js = '''
    // =========================================================================
    // Optical Vision Spectrum Engine Controller (20/200, 20/20, 20/10 & Light/Dark)
    // =========================================================================
    (function initVisionSpectrum() {
      var savedTheme = localStorage.getItem('lumbros_vision_theme') || 'dark';
      var savedAcuity = localStorage.getItem('lumbros_vision_acuity') || '20-20';

      function applyVisionSettings(theme, acuity) {
        // Set attributes on html and body
        document.documentElement.setAttribute('data-theme', theme);
        document.documentElement.setAttribute('data-acuity', acuity);
        document.body.setAttribute('data-theme', theme);
        document.body.setAttribute('data-acuity', acuity);

        if (theme === 'light') {
          document.body.classList.add('theme-light');
          document.body.classList.remove('theme-dark');
        } else {
          document.body.classList.add('theme-dark');
          document.body.classList.remove('theme-light');
        }

        // Update Buttons UI
        var themeBtns = document.querySelectorAll('.polarity-btn');
        themeBtns.forEach(function(btn) {
          if (btn.getAttribute('data-theme') === theme) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        });

        var acuityBtns = document.querySelectorAll('.acuity-node-btn');
        acuityBtns.forEach(function(btn) {
          if (btn.getAttribute('data-acuity') === acuity) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        });

        // Update Slider Position
        var sliderPip = document.querySelector('.slider-pip');
        if (sliderPip) {
          if (acuity === '20-200') {
            sliderPip.style.left = '10%';
          } else if (acuity === '20-10') {
            sliderPip.style.left = '90%';
          } else {
            sliderPip.style.left = '50%';
          }
        }

        // Update Live Telemetry
        var telem = document.getElementById('vision-live-telemetry');
        if (telem) {
          var weber = theme === 'light' ? '14.8:1' : (acuity === '20-200' ? '12.4:1' : (acuity === '20-10' ? '16.0:1' : '9.2:1'));
          var polarityName = theme === 'light' ? 'LIGHT_ALABASTER_REVERSE' : 'DARK_OBSIDIAN_PHOSPHOR';
          telem.innerHTML = 'ACUITY: <span class="val-acuity">' + acuity.replace('-', '/') + '</span> | POLARITY: <span class="val-polarity">' + polarityName + '</span> | WEBER: <span class="val-contrast">' + weber + '</span>';
        }

        localStorage.setItem('lumbros_vision_theme', theme);
        localStorage.setItem('lumbros_vision_acuity', acuity);
      }

      document.addEventListener('DOMContentLoaded', function() {
        applyVisionSettings(savedTheme, savedAcuity);

        // Click handlers for theme polarity
        var themeBtns = document.querySelectorAll('.polarity-btn');
        themeBtns.forEach(function(btn) {
          btn.addEventListener('click', function() {
            var selectedTheme = this.getAttribute('data-theme');
            var currentAcuity = document.body.getAttribute('data-acuity') || '20-20';
            applyVisionSettings(selectedTheme, currentAcuity);
          });
        });

        // Click handlers for acuity nodes
        var acuityBtns = document.querySelectorAll('.acuity-node-btn');
        acuityBtns.forEach(function(btn) {
          btn.addEventListener('click', function() {
            var selectedAcuity = this.getAttribute('data-acuity');
            var currentTheme = document.body.getAttribute('data-theme') || 'dark';
            applyVisionSettings(currentTheme, selectedAcuity);
          });
        });
      });

      // Apply immediately before DOM render to prevent flash
      applyVisionSettings(savedTheme, savedAcuity);
    })();
'''

# Update deploy/homepage.html
with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert vision_deck_html right before <!-- Scanline & Ambient Overlay -->
if '<!-- Scanline & Ambient Overlay -->' in content:
    content = content.replace('<!-- Scanline & Ambient Overlay -->', vision_deck_html + '\n  <!-- Scanline & Ambient Overlay -->')
    print("Inserted vision deck HTML.")
else:
    print("Warning: anchor not found for vision deck HTML.")

# Append vision_css inside <style>
content = content.replace('</style>', vision_css + '\n  </style>')
print("Appended vision CSS.")

# Append vision_js inside <script>
content = content.replace('</script>', vision_js + '\n  </script>')
print("Appended vision JS.")

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: deploy/homepage.html updated with Vision Spectrum Engine!")

import os
import re

with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. New Video-Game Arcade Vision Deck HTML
new_deck_html = '''
  <!-- =========================================================================
       OPTICAL VISION SPECTRUM & ACUITY CALIBRATION DECK (20/200 -> 20/20 -> 20/10)
       ARTISTIC DESIGN, IDEAS & CREATIVITY — ALL REPRESENTED THROUGH MATHEMATICS & GOD
       ========================================================================= -->
  <div id="vision-calibration-deck" class="vision-calibration-deck arcade-hud-active">
    <div class="vision-deck-frame">
      <div class="vision-deck-scanlines"></div>
      <div class="arcade-glow-halo"></div>

      <!-- Top Status & Directive Bar with Cycling Spectrum & Divine Creative Intent -->
      <div class="vision-deck-topbar">
        <div class="vision-badge-row">
          <div class="vision-badge">
            <span class="vision-pulse-dot"></span>
            <span class="vision-badge-code">OPTICAL_HUD v4.2 // SPECTRUM ENGINE</span>
          </div>
          <div class="arcade-status-capsule">
            <span class="capsule-pip"></span>
            <span class="capsule-text">NEURAL_OPTICS: ONLINE</span>
          </div>
        </div>

        <!-- Large Catchy Headline with 7-Pattern Circulating Spectrum -->
        <div class="vision-headline-wrap">
          <h2 class="vision-headline-hero">
            <span class="founder-name-chroma vision-hero-chroma">⟦ CHOOSE YOUR SPECTRUM EXPERIENCE ⟧</span>
          </h2>
          <div class="vision-divine-callout">
            <span class="manifesto-zap">⚡</span>
            <span class="manifesto-core">CONTROL THE OPTICAL SPECTRUM OF SIGHT // ARTISTIC DESIGN, IDEAS &amp; CREATIVITY — ALL REPRESENTED THROUGH MATHEMATICS &amp; GOD</span>
            <span class="manifesto-zap">⚡</span>
          </div>
        </div>

        <!-- Real-time Mathematical Telemetry -->
        <div class="vision-telemetry-hud" id="vision-live-telemetry">
          <div class="telem-item"><span class="telem-k">OPTICAL_PRESCRIPTION:</span> <span class="val-acuity glow-val">20/20</span></div>
          <div class="telem-item"><span class="telem-k">SPECTRUM_POLARITY:</span> <span class="val-polarity glow-val">DARK_OBSIDIAN</span></div>
          <div class="telem-item"><span class="telem-k">WEBER_CONTRAST:</span> <span class="val-contrast glow-val">9.2:1</span></div>
          <div class="telem-item"><span class="telem-k">RETINAL_POWER:</span> <span class="val-power glow-val">NOMINAL</span></div>
        </div>
      </div>

      <!-- Controls Grid: Acuity Gauge + Polarity Toggle -->
      <div class="vision-deck-controls">
        
        <!-- Module 1: 3-Stage Mathematical Acuity Gauge with Interactive Drag Circle -->
        <div class="vision-module vision-acuity-module">
          <div class="module-header-game">
            <span class="mod-icon-laser">◈</span>
            <span class="mod-title">VISUAL ACUITY GAUGE &amp; SIGHT PRESCRIPTION CALIBRATOR</span>
            <span class="mod-arcade-tag">TACTILE DIAL</span>
          </div>

          <!-- 3 Quick Focus Preset Buttons -->
          <div class="acuity-gauge-track">
            <button type="button" class="acuity-node-btn" data-acuity="20-200" data-gauge="0" title="High-Contrast Macro Mode for Low Vision / Eye Fatigue (20/200 to 20/70)">
              <span class="node-grade">20/200</span>
              <span class="node-name">MACRO CONTRAST</span>
              <span class="node-spec">High Stroke // Anti-Strain</span>
            </button>

            <button type="button" class="acuity-node-btn active" data-acuity="20-20" data-gauge="75" title="Standard Harmonic Spectrum for 20/20 Corrected Vision">
              <span class="node-grade">20/20</span>
              <span class="node-name">BALANCED EQUILIBRIUM</span>
              <span class="node-spec">Nominal Dispersion</span>
            </button>

            <button type="button" class="acuity-node-btn" data-acuity="20-10" data-gauge="100" title="Hyper-Acuity Laser Focus for 20/10 Vision &amp; High-DPI Displays">
              <span class="node-grade">20/10</span>
              <span class="node-name">HYPER-ACUITY</span>
              <span class="node-spec">Razor Micro-Vector</span>
            </button>
          </div>

          <!-- The Continuous Mathematical Gauge Bar with Interactive Drag Circle -->
          <div class="acuity-interactive-container" id="acuity-interactive-container">
            <div class="gauge-instruction-bar">
              <span>◄ SLIDE CIRCLE TO CALIBRATE EXACT VISUAL ACUITY &amp; CONTRAST ►</span>
              <span id="gauge-live-fraction" class="gauge-live-badge">20/20 (MAR 1.0\')</span>
            </div>

            <div class="acuity-rail-track" id="acuity-rail-track">
              <!-- 12-Color Optical Spectrum Background on Rail -->
              <div class="acuity-rail-spectrum"></div>
              
              <!-- Reticle Target Lines -->
              <div class="rail-grid-ticks">
                <span class="r-tick" style="left:0%;"></span>
                <span class="r-tick" style="left:15%;"></span>
                <span class="r-tick" style="left:35%;"></span>
                <span class="r-tick" style="left:55%;"></span>
                <span class="r-tick mid" style="left:75%;"></span>
                <span class="r-tick" style="left:90%;"></span>
                <span class="r-tick end" style="left:100%;"></span>
              </div>

              <!-- Interactive Drag Thumb (Circle on the Bar) -->
              <div class="slider-circle-thumb" id="slider-circle-thumb" style="left: 75%;">
                <div class="circle-laser-halo"></div>
                <div class="circle-core"></div>
                <div class="circle-crosshair"></div>
                <div class="circle-floating-badge" id="circle-floating-badge">20/20</div>
              </div>

              <!-- Accessible native range input overlay for seamless drag/touch/keys -->
              <input type="range" id="acuity-analog-slider" class="acuity-analog-slider" min="0" max="100" value="75" step="1" aria-label="Visual Acuity Range Calibrator">
            </div>

            <!-- Gauge Scale Ticks -->
            <div class="gauge-scale-ticks">
              <span class="tick-link" data-val="0">20/200</span>
              <span class="tick-link" data-val="25">20/70</span>
              <span class="tick-link" data-val="50">20/40</span>
              <span class="tick-link active" data-val="75">20/20 (STANDARD)</span>
              <span class="tick-link" data-val="90">20/15</span>
              <span class="tick-link" data-val="100">20/10 (RAZOR)</span>
            </div>
          </div>
        </div>

        <!-- Module 2: Luminance Spectrum Polarity (Dark Obsidian vs Reverse Light Alabaster) -->
        <div class="vision-module vision-polarity-module">
          <div class="module-header-game">
            <span class="mod-icon-laser">◐</span>
            <span class="mod-title">SPECTRUM LUMINANCE POLARITY</span>
            <span class="mod-arcade-tag">DUAL-LUX</span>
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

          <!-- 12-Color Preview Indicator Ribbon -->
          <div class="polarity-spectrum-preview">
            <span class="spectrum-dot dot-1" title="Red 0%"></span>
            <span class="spectrum-dot dot-2" title="Coral 9%"></span>
            <span class="spectrum-dot dot-3" title="Amber 18%"></span>
            <span class="spectrum-dot dot-4" title="Gold 27%"></span>
            <span class="spectrum-dot dot-5" title="Yellow 36%"></span>
            <span class="spectrum-dot dot-6" title="Pear 45%"></span>
            <span class="spectrum-dot dot-7" title="Emerald Green 50% [Center Midpoint]"></span>
            <span class="spectrum-dot dot-8" title="Teal 55%"></span>
            <span class="spectrum-dot dot-9" title="Cyan 64%"></span>
            <span class="spectrum-dot dot-10" title="Blue 73%"></span>
            <span class="spectrum-dot dot-11" title="Indigo 82%"></span>
            <span class="spectrum-dot dot-12" title="Magenta 100%"></span>
          </div>
          <div class="spectrum-center-label">
            <span>◄ 12-COLOR SPECTRUM // HARMONIC CENTER: 550nm GREEN ►</span>
          </div>
        </div>

      </div>
    </div>
  </div>
'''

# 2. Comprehensive CSS for Game-like Video Game Arcade HUD & Draggable Circle
new_css = '''
    /* =========================================================================
       ARCADE HUD // OPTICAL VISION SPECTRUM & INTERACTIVE DRAG CIRCLE GAUGE
       ========================================================================= */
    .arcade-hud-active .vision-deck-frame {
      background: radial-gradient(circle at 50% 0%, rgba(0, 255, 102, 0.12) 0%, rgba(2, 6, 4, 0.98) 75%) !important;
      border: 2px solid #00ff66 !important;
      box-shadow: 0 0 30px rgba(0, 255, 102, 0.3), inset 0 0 25px rgba(0, 0, 0, 0.9) !important;
      position: relative;
    }

    .arcade-glow-halo {
      position: absolute;
      top: -20px; left: 20%; right: 20%; height: 40px;
      background: radial-gradient(ellipse at center, rgba(0, 255, 102, 0.25) 0%, transparent 70%);
      pointer-events: none;
      filter: blur(10px);
    }

    .vision-badge-row {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }

    .arcade-status-capsule {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 2px 8px;
      background: rgba(0, 229, 255, 0.12);
      border: 1px solid #00e5ff;
      border-radius: 12px;
      font-size: 0.65rem;
      font-weight: 800;
      color: #00e5ff;
      letter-spacing: 1px;
    }

    .capsule-pip {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00e5ff;
      box-shadow: 0 0 6px #00e5ff;
      animation: pulse-dot 1.2s infinite;
    }

    /* Hero Headline with 7-Pattern Circulating Gradient Text */
    .vision-headline-wrap {
      text-align: center;
      margin: 8px 0 14px 0;
      padding: 0 10px;
    }

    .vision-headline-hero {
      margin: 0 0 6px 0;
      font-size: 1.65rem;
      letter-spacing: 2px;
      font-weight: 900;
    }

    @media (min-width: 900px) {
      .vision-headline-hero {
        font-size: 2.15rem;
        letter-spacing: 3px;
      }
    }

    .vision-hero-chroma {
      display: inline-block;
      text-shadow: 0 0 20px rgba(0, 255, 102, 0.4);
    }

    .vision-divine-callout {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
      text-shadow: 0 0 10px rgba(0, 255, 102, 0.7);
      flex-wrap: wrap;
    }

    .manifesto-zap {
      color: #ffe600;
      text-shadow: 0 0 8px #ffe600;
      font-size: 0.9rem;
    }

    .manifesto-core {
      background: linear-gradient(90deg, #8ce4a7, #ffffff, #00e5ff, #ffffff, #8ce4a7);
      background-size: 200% auto;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: pat1-spectrum-drift 6s linear infinite;
    }

    .vision-telemetry-hud {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 12px;
      background: rgba(0, 15, 8, 0.7);
      border: 1px solid #14442a;
      border-radius: 4px;
      padding: 8px 14px;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 1px;
    }

    .telem-k {
      color: #8ce4a7;
    }

    .glow-val {
      color: #00ff66;
      font-weight: 800;
      text-shadow: 0 0 8px rgba(0, 255, 102, 0.6);
    }

    .module-header-game {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      font-size: 0.72rem;
      font-weight: 800;
      color: #4ef38d;
      letter-spacing: 1.5px;
    }

    .mod-icon-laser {
      color: #00ff66;
      font-size: 0.85rem;
      margin-right: 6px;
    }

    .mod-arcade-tag {
      background: rgba(0, 255, 102, 0.15);
      border: 1px solid #00ff66;
      color: #00ff66;
      font-size: 0.62rem;
      padding: 1px 6px;
      border-radius: 3px;
    }

    /* The Interactive Rail Track & Circle on the Bar */
    .acuity-interactive-container {
      margin-top: 14px;
      background: rgba(0, 10, 5, 0.8);
      border: 1px solid #1c5e37;
      border-radius: 6px;
      padding: 14px 16px;
      position: relative;
    }

    .gauge-instruction-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.68rem;
      font-weight: 800;
      color: #00e5ff;
      letter-spacing: 1.5px;
      margin-bottom: 12px;
    }

    .gauge-live-badge {
      background: #00ff66;
      color: #030605;
      font-size: 0.72rem;
      font-weight: 900;
      padding: 2px 8px;
      border-radius: 4px;
      box-shadow: 0 0 10px #00ff66;
      letter-spacing: 1px;
    }

    .acuity-rail-track {
      position: relative;
      height: 16px;
      background: #010402;
      border: 1px solid #00ff66;
      border-radius: 8px;
      box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.9), 0 0 8px rgba(0, 255, 102, 0.2);
      margin: 18px 0 14px 0;
      cursor: pointer;
    }

    .acuity-rail-spectrum {
      position: absolute;
      top: 3px; bottom: 3px; left: 4px; right: 4px;
      border-radius: 5px;
      background: linear-gradient(
        90deg,
        #ff0033 0%,
        #ff7700 20%,
        #ffe600 40%,
        #b4e600 55%,
        #00ff66 75%,
        #00e5ff 90%,
        #e00099 100%
      );
      opacity: 0.85;
    }

    .rail-grid-ticks {
      position: absolute;
      top: 0; bottom: 0; left: 0; right: 0;
      pointer-events: none;
    }

    .r-tick {
      position: absolute;
      top: 0; bottom: 0;
      width: 2px;
      background: rgba(0, 0, 0, 0.6);
    }

    .r-tick.mid {
      background: #ffffff;
      box-shadow: 0 0 6px #ffffff;
      width: 3px;
    }

    /* The Interactive Circle on the Bar (Tactile Game Pip) */
    .slider-circle-thumb {
      position: absolute;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: radial-gradient(circle, #ffffff 30%, #00ff66 70%, #030605 100%);
      border: 2px solid #ffffff;
      box-shadow: 0 0 20px #00ff66, 0 0 40px rgba(0, 255, 102, 0.8), inset 0 0 8px rgba(0, 255, 102, 0.9);
      cursor: grab;
      z-index: 10;
      transition: box-shadow 0.2s ease, transform 0.15s ease;
      touch-action: none;
    }

    .slider-circle-thumb:active {
      cursor: grabbing;
      transform: translate(-50%, -50%) scale(1.15);
      box-shadow: 0 0 30px #00ff66, 0 0 60px rgba(0, 255, 102, 1);
    }

    .circle-laser-halo {
      position: absolute;
      top: -8px; left: -8px; right: -8px; bottom: -8px;
      border-radius: 50%;
      border: 1px dashed #00ff66;
      animation: spin-laser 8s linear infinite;
      pointer-events: none;
    }

    @keyframes spin-laser {
      100% { transform: rotate(360deg); }
    }

    .circle-core {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      width: 10px; height: 10px;
      border-radius: 50%;
      background: #030605;
      border: 2px solid #00ff66;
    }

    .circle-floating-badge {
      position: absolute;
      bottom: 38px;
      left: 50%;
      transform: translateX(-50%);
      background: #020604;
      border: 1px solid #00ff66;
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 0.65rem;
      font-weight: 900;
      color: #00ff66;
      white-space: nowrap;
      box-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
      pointer-events: none;
    }

    /* Native Range Input (Transparent Overlay for Seamless Touch & Keyboard Control) */
    .acuity-analog-slider {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      opacity: 0;
      cursor: pointer;
      margin: 0;
      z-index: 12;
    }

    /* Scale Ticks Below the Rail */
    .gauge-scale-ticks {
      display: flex;
      justify-content: space-between;
      margin-top: 10px;
      font-size: 0.64rem;
      color: #8ce4a7;
      font-weight: 800;
    }

    .tick-link {
      cursor: pointer;
      transition: color 0.2s ease, text-shadow 0.2s ease;
    }

    .tick-link:hover, .tick-link.active {
      color: #00ff66;
      text-shadow: 0 0 8px #00ff66;
    }

    .spectrum-center-label {
      text-align: center;
      margin-top: 6px;
      font-size: 0.62rem;
      font-weight: 800;
      color: #4ef38d;
      letter-spacing: 1px;
    }
'''

# 3. Dynamic Interactive JS Engine for Continuous Dragging & Math Scaling
new_js = '''
    // =========================================================================
    // Video Game Arcade Vision Engine & Continuous Acuity Drag Dial
    // =========================================================================
    (function initArcadeVisionDial() {
      var savedTheme = localStorage.getItem('lumbros_vision_theme') || 'dark';
      var savedAcuityVal = parseInt(localStorage.getItem('lumbros_vision_gauge') || '75', 10);

      var slider = document.getElementById('acuity-analog-slider');
      var circleThumb = document.getElementById('slider-circle-thumb');
      var floatingBadge = document.getElementById('circle-floating-badge');
      var liveFraction = document.getElementById('gauge-live-fraction');
      var telemAcuity = document.querySelector('.val-acuity');
      var telemPolarity = document.querySelector('.val-polarity');
      var telemContrast = document.querySelector('.val-contrast');
      var telemPower = document.querySelector('.val-power');

      // Mathematical Mapping of Slider Position [0..100] to Snellen Acuity, Stroke & Contrast
      function computeAcuityParameters(val) {
        var t = val / 100.0;
        var snellen = '20/20';
        var mar = '1.0\\'';
        var weber = '9.2:1';
        var power = 'NOMINAL';
        var fontScale = 1.0;
        var weightBoost = 0;
        var letterSpacing = 0;
        var lineHeight = 1.6;
        var borderWidth = 1.5;

        if (val <= 12) {
          snellen = '20/200';
          mar = '10.0\\'';
          weber = '18.5:1';
          power = 'ULTRA-HIGH CONTRAST';
          fontScale = 1.15;
          weightBoost = 250;
          letterSpacing = 0.8;
          lineHeight = 1.9;
          borderWidth = 3.0;
        } else if (val <= 28) {
          snellen = '20/100';
          mar = '5.0\\'';
          weber = '15.2:1';
          power = 'HIGH MACRO';
          fontScale = 1.10;
          weightBoost = 200;
          letterSpacing = 0.6;
          lineHeight = 1.8;
          borderWidth = 2.6;
        } else if (val <= 45) {
          snellen = '20/70';
          mar = '3.5\\'';
          weber = '13.0:1';
          power = 'EXPANDED';
          fontScale = 1.06;
          weightBoost = 150;
          letterSpacing = 0.4;
          lineHeight = 1.75;
          borderWidth = 2.2;
        } else if (val <= 60) {
          snellen = '20/40';
          mar = '2.0\\'';
          weber = '11.5:1';
          power = 'STANDARD-PLUS';
          fontScale = 1.03;
          weightBoost = 100;
          letterSpacing = 0.2;
          lineHeight = 1.7;
          borderWidth = 1.8;
        } else if (val <= 85) {
          snellen = '20/20';
          mar = '1.0\\'';
          weber = '9.2:1';
          power = 'HARMONIC EQUILIBRIUM';
          fontScale = 1.0;
          weightBoost = 0;
          letterSpacing = 0;
          lineHeight = 1.6;
          borderWidth = 1.5;
        } else if (val <= 95) {
          snellen = '20/15';
          mar = '0.75\\'';
          weber = '8.0:1';
          power = 'HIGH DENSITY';
          fontScale = 0.98;
          weightBoost = 0;
          letterSpacing = -0.1;
          lineHeight = 1.55;
          borderWidth = 1.2;
        } else {
          snellen = '20/10';
          mar = '0.5\\'';
          weber = '7.1:1';
          power = 'HYPER-ACUITY RAZOR';
          fontScale = 0.95;
          weightBoost = 0;
          letterSpacing = -0.2;
          lineHeight = 1.5;
          borderWidth = 0.85;
        }

        return {
          snellen: snellen,
          mar: mar,
          weber: weber,
          power: power,
          fontScale: fontScale,
          weightBoost: weightBoost,
          letterSpacing: letterSpacing,
          lineHeight: lineHeight,
          borderWidth: borderWidth
        };
      }

      function applyAcuityContinuous(val) {
        var params = computeAcuityParameters(val);

        // Position Circle Thumb
        if (circleThumb) {
          circleThumb.style.left = val + '%';
        }
        if (floatingBadge) {
          floatingBadge.textContent = params.snellen;
        }
        if (liveFraction) {
          liveFraction.textContent = params.snellen + ' (MAR ' + params.mar + ')';
        }
        if (slider) {
          slider.value = val;
        }

        // Update Telemetry
        if (telemAcuity) telemAcuity.textContent = params.snellen;
        if (telemContrast) telemContrast.textContent = params.weber;
        if (telemPower) telemPower.textContent = params.power;

        // Apply CSS custom properties dynamically across DOM
        var root = document.documentElement;
        root.style.setProperty('--font-scale', params.fontScale);
        root.style.setProperty('--line-height-scale', params.lineHeight);
        root.style.setProperty('--letter-spacing-boost', params.letterSpacing + 'px');
        root.style.setProperty('--border-width-scale', params.borderWidth + 'px');

        // Apply font scale and line height to body
        document.body.style.fontSize = (params.fontScale * 100) + '%';

        // Highlight preset buttons if near
        var presetBtns = document.querySelectorAll('.acuity-node-btn');
        presetBtns.forEach(function(btn) {
          var btnGauge = parseInt(btn.getAttribute('data-gauge') || '75', 10);
          if (Math.abs(btnGauge - val) <= 15) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        });

        // Highlight ticks
        var ticks = document.querySelectorAll('.tick-link');
        ticks.forEach(function(tick) {
          var tickVal = parseInt(tick.getAttribute('data-val') || '0', 10);
          if (Math.abs(tickVal - val) <= 12) {
            tick.classList.add('active');
          } else {
            tick.classList.remove('active');
          }
        });

        localStorage.setItem('lumbros_vision_gauge', val);
      }

      function applyThemePolarity(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        document.body.setAttribute('data-theme', theme);
        if (theme === 'light') {
          document.body.classList.add('theme-light');
          document.body.classList.remove('theme-dark');
          if (telemPolarity) telemPolarity.textContent = 'LIGHT_REVERSE_ALABASTER';
        } else {
          document.body.classList.add('theme-dark');
          document.body.classList.remove('theme-light');
          if (telemPolarity) telemPolarity.textContent = 'DARK_OBSIDIAN';
        }

        var themeBtns = document.querySelectorAll('.polarity-btn');
        themeBtns.forEach(function(btn) {
          if (btn.getAttribute('data-theme') === theme) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        });

        localStorage.setItem('lumbros_vision_theme', theme);
      }

      document.addEventListener('DOMContentLoaded', function() {
        applyThemePolarity(savedTheme);
        applyAcuityContinuous(savedAcuityVal);

        // Native range input slider event
        if (slider) {
          slider.addEventListener('input', function() {
            applyAcuityContinuous(parseInt(this.value, 10));
          });
        }

        // Preset Button clicks
        var presetBtns = document.querySelectorAll('.acuity-node-btn');
        presetBtns.forEach(function(btn) {
          btn.addEventListener('click', function() {
            var targetGauge = parseInt(this.getAttribute('data-gauge') || '75', 10);
            applyAcuityContinuous(targetGauge);
          });
        });

        // Tick link clicks
        var tickLinks = document.querySelectorAll('.tick-link');
        tickLinks.forEach(function(tick) {
          tick.addEventListener('click', function() {
            var targetGauge = parseInt(this.getAttribute('data-val') || '75', 10);
            applyAcuityContinuous(targetGauge);
          });
        });

        // Theme Polarity buttons
        var themeBtns = document.querySelectorAll('.polarity-btn');
        themeBtns.forEach(function(btn) {
          btn.addEventListener('click', function() {
            var selectedTheme = this.getAttribute('data-theme');
            applyThemePolarity(selectedTheme);
          });
        });
      });

      // Apply initial theme immediately
      applyThemePolarity(savedTheme);
    })();
'''

# 1. Replace existing <div id="vision-calibration-deck"...></div> in content
deck_pattern = re.compile(r'(<div id="vision-calibration-deck"[\s\S]*?</div>\s*</div>\s*</div>)', re.IGNORECASE)
if deck_pattern.search(content):
    content = deck_pattern.sub(new_deck_html.strip(), content, count=1)
    print("Replaced vision deck HTML with arcade HUD.")
else:
    print("Warning: could not match vision deck HTML, searching alternative pattern.")

# 2. Append new arcade CSS before </style>
content = content.replace('</style>', new_css + '\n  </style>')
print("Appended arcade HUD CSS.")

# 3. Append new continuous arcade JS before </script>
content = content.replace('</script>', new_js + '\n  </script>')
print("Appended arcade HUD JS.")

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: deploy/homepage.html updated with arcade vision gauge!")

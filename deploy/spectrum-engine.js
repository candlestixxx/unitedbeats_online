// =========================================================================
// OPTICAL SPECTRUM PRESCRIPTION CALIBRATOR AND THEME ENGINE (v4.2)
// Game/Calculator Engine for Lumbros.me and UnitedBeats.online
// Representing all 12 colors of the optical spectrum through mathematics and God
// =========================================================================
(function initSpectrumGameEngine() {
  function getStored(key, fallback) {
    try {
      var val = localStorage.getItem(key);
      if (val !== null) return val;
      return fallback;
    } catch(e) {
      return fallback;
    }
  }

  function setStored(key, val) {
    try {
      localStorage.setItem(key, val);
    } catch(e) {}
  }

  var currentTheme = getStored('lumbros_vision_theme', 'dark');
  var currentGauge = parseInt(getStored('lumbros_vision_gauge', '75'), 10);
  var currentArchetype = getStored('lumbros_active_archetype', 'heart');

  function computePrescription(val) {
    var clamped = Math.max(0, Math.min(100, val));
    var t = clamped / 100.0;
    
    // Mathematical Transparency and Geometry Formulas based on prescription strength:
    // Low Vision (20/200, t=0): High Opacity (0.65 fill, 0.95 border, 3.5px stroke, 0.85 shapes)
    // Standard (20/20, t=0.75): Balanced Opacity (0.16 fill, 0.40 border, 1.5px stroke, 0.35 shapes)
    // Hyper-Acuity (20/10, t=1.0): High Transparency (0.05 fill, 0.20 border, 0.85px stroke, 0.15 shapes)
    var fillOpacity = (0.65 - (t * 0.58)).toFixed(3);        // 0.65 down to 0.07
    var borderOpacity = (0.95 - (t * 0.72)).toFixed(3);      // 0.95 down to 0.23
    var shapeOpacity = (0.85 - (t * 0.68)).toFixed(3);       // 0.85 down to 0.17
    var strokeWidth = (3.5 - (t * 2.65)).toFixed(2) + 'px';  // 3.50px down to 0.85px
    var scanlineOpacity = (0.98 - (t * 0.55)).toFixed(3);    // 0.98 down to 0.43
    var fontScale = (1.18 - (t * 0.23)).toFixed(3);          // 1.18 down to 0.95
    var contrastMult = (1.65 - (t * 0.70)).toFixed(3);       // 1.65 down to 0.95
    var brightnessMult = (1.14 - (t * 0.18)).toFixed(3);     // 1.14 down to 0.96

    var snellen = '20/20';
    var diopters = '0.00D (PLANO)';
    var dioptersBrief = '0.00D';
    var grade = '20-20';
    var weber = '9.2:1';
    var calib = '100% NOMINAL';
    var power = 'HARMONIC EQUILIBRIUM';

    if (val <= 15) {
      snellen = '20/200';
      grade = '20-200';
      diopters = '-8.50D (HIGH SIGHT ASSIST)';
      dioptersBrief = '-8.50D';
      weber = '21.0:1';
      calib = '165% MAX CONTRAST';
      power = 'DENSE SIGHT SHIELD // MAX OPACITY';
    } else if (val <= 32) {
      snellen = '20/100';
      grade = '20-100';
      diopters = '-5.50D (HEAVY GLASSES)';
      dioptersBrief = '-5.50D';
      weber = '16.5:1';
      calib = '145% BOOSTED';
      power = 'HIGH MACRO // LOW TRANSPARENCY';
    } else if (val <= 50) {
      snellen = '20/70';
      grade = '20-70';
      diopters = '-4.00D (MEDIUM GLASSES)';
      dioptersBrief = '-4.00D';
      weber = '13.5:1';
      calib = '130% EXPANDED';
      power = 'EXPANDED SPECTRUM FIELD';
    } else if (val <= 68) {
      snellen = '20/40';
      grade = '20-40';
      diopters = '-2.00D (DRIVING SPEC)';
      dioptersBrief = '-2.00D';
      weber = '11.2:1';
      calib = '115% STANDARD-PLUS';
      power = 'BALANCED SPECTRUM HARMONIC';
    } else if (val <= 85) {
      snellen = '20/20';
      grade = '20-20';
      diopters = '0.00D (PLANO NORMAL)';
      dioptersBrief = '0.00D';
      weber = '9.2:1';
      calib = '100% NOMINAL';
      power = 'NOMINAL GOLDEN RATIO';
    } else if (val <= 95) {
      snellen = '20/15';
      grade = '20-15';
      diopters = '+0.50D (SHARP FOCUS)';
      dioptersBrief = '+0.50D';
      weber = '8.0:1';
      calib = '95% HIGH DENSITY';
      power = 'HIGH TRANSPARENCY // MICRO-VECTOR';
    } else {
      snellen = '20/10';
      grade = '20-10';
      diopters = '+1.00D (EAGLE HYPER)';
      dioptersBrief = '+1.00D';
      weber = '7.1:1';
      calib = '92% SUB-PIXEL';
      power = 'HYPER-ACUITY // ULTRA-TRANSPARENT';
    }

    return {
      val: val,
      grade: grade,
      snellen: snellen,
      diopters: diopters,
      dioptersBrief: dioptersBrief,
      weber: weber,
      calib: calib,
      power: power,
      fillOpacity: fillOpacity,
      borderOpacity: borderOpacity,
      shapeOpacity: shapeOpacity,
      strokeWidth: strokeWidth,
      scanlineOpacity: scanlineOpacity,
      fontScale: fontScale,
      contrastMult: contrastMult,
      brightnessMult: brightnessMult
    };
  }

  function applyPrescription(val) {
    currentGauge = val;
    setStored('lumbros_vision_gauge', val);
    var p = computePrescription(val);

    var root = document.documentElement;
    var body = document.body;
    var term = document.getElementById('united-beats-terminal');

    var targets = [root, body];
    if (term) targets.push(term);

    for (var i = 0; i < targets.length; i++) {
      var el = targets[i];
      el.style.setProperty('--spectrum-fill-opacity', p.fillOpacity);
      el.style.setProperty('--spectrum-border-opacity', p.borderOpacity);
      el.style.setProperty('--spectrum-shape-opacity', p.shapeOpacity);
      el.style.setProperty('--spectrum-stroke', p.strokeWidth);
      el.style.setProperty('--spectrum-scan-opacity', p.scanlineOpacity);
      el.style.setProperty('--border-width-scale', p.strokeWidth);
      el.style.setProperty('--font-scale', p.fontScale);
      el.style.setProperty('--site-contrast', p.contrastMult);
      el.style.setProperty('--site-brightness', p.brightnessMult);
    }

    root.setAttribute('data-acuity-grade', p.grade);
    body.setAttribute('data-acuity-grade', p.grade);
    if (term) term.setAttribute('data-acuity-grade', p.grade);

    body.style.fontSize = (parseFloat(p.fontScale) * 15) + 'px';

    // Move Circle Thumb and Floating Badge
    var thumb = document.getElementById('slider-circle-thumb');
    if (thumb) {
      thumb.style.left = val + '%';
    }
    var badge = document.getElementById('circle-floating-badge');
    if (badge) {
      badge.textContent = p.snellen + ' (' + p.dioptersBrief + ')';
    }
    var instructionBadge = document.getElementById('gauge-live-fraction');
    if (instructionBadge) {
      instructionBadge.textContent = p.snellen + ' [' + p.diopters + '] // WEBER ' + p.weber + ' // ' + p.calib;
    }

    var slider = document.getElementById('acuity-analog-slider');
    if (slider) {
      if (parseInt(slider.value, 10) !== val) {
        slider.value = val;
      }
    }

    // Update Telemetry Items
    var telemAcuity = document.querySelector('.val-acuity');
    var telemDiopter = document.querySelector('.val-diopter');
    var telemContrast = document.querySelector('.val-contrast');
    var telemCalib = document.querySelector('.val-calib');
    var telemPower = document.querySelector('.val-power');

    if (telemAcuity) telemAcuity.textContent = p.snellen;
    if (telemDiopter) telemDiopter.textContent = p.diopters;
    if (telemContrast) telemContrast.textContent = p.weber;
    if (telemCalib) telemCalib.textContent = p.calib;
    if (telemPower) telemPower.textContent = p.power;

    // Highlight Preset Buttons
    var presetBtns = document.querySelectorAll('.acuity-node-btn');
    for (var j = 0; j < presetBtns.length; j++) {
      var btn = presetBtns[j];
      var btnGauge = parseInt(btn.getAttribute('data-gauge') || '75', 10);
      if (Math.abs(btnGauge - val) <= 15) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }

    // Highlight Ticks
    var ticks = document.querySelectorAll('.tick-link');
    for (var k = 0; k < ticks.length; k++) {
      var tick = ticks[k];
      var tickVal = parseInt(tick.getAttribute('data-val') || '0', 10);
      if (Math.abs(tickVal - val) <= 10) {
        tick.classList.add('active');
      } else {
        tick.classList.remove('active');
      }
    }
  }

  
  function applyArchetype(archId) {
    if (!archId) archId = 'heart';
    currentArchetype = archId;
    setStored('lumbros_active_archetype', archId);

    var cards = document.querySelectorAll('.archetype-card');
    var activeCard = null;
    for (var i = 0; i < cards.length; i++) {
      var c = cards[i];
      if (c.getAttribute('data-arch-id') === archId) {
        c.classList.add('active');
        activeCard = c;
      } else {
        c.classList.remove('active');
      }
    }

    if (!activeCard) {
      if (cards.length > 0) {
        activeCard = cards[0];
        activeCard.classList.add('active');
      }
    }

    if (activeCard) {
      var color = activeCard.getAttribute('data-color') || '#00ff66';
      var name = activeCard.getAttribute('data-name') || 'THE HARMONIC HEART';
      var wave = activeCard.getAttribute('data-wave') || '550nm (50%)';
      var psych = activeCard.getAttribute('data-psych') || 'TRUST & EQUILIBRIUM';

      var root = document.documentElement;
      var body = document.body;
      var term = document.getElementById('united-beats-terminal');
      var targets = [root, body];
      if (term) targets.push(term);

      for (var t = 0; t < targets.length; t++) {
        targets[t].style.setProperty('--active-archetype-color', color);
        targets[t].style.setProperty('--active-archetype-id', archId);
      }

      var telemArchetype = document.querySelector('.val-archetype');
      if (telemArchetype) {
        telemArchetype.innerHTML = '<span style="color:' + color + '">● ' + name + '</span> [' + wave + '] // ' + psych;
      }
    }
  }

  function applyTheme(theme) {
    currentTheme = theme;
    setStored('lumbros_vision_theme', theme);
    var isLight = (theme === 'light');

    var root = document.documentElement;
    var body = document.body;
    var term = document.getElementById('united-beats-terminal');

    if (isLight) {
      root.setAttribute('data-theme', 'light');
      body.setAttribute('data-theme', 'light');
      body.classList.add('theme-light');
      body.classList.remove('theme-dark');
      root.classList.add('theme-light');
      root.classList.remove('theme-dark');

      body.style.backgroundColor = '#edf3ef';
      body.style.color = '#03140a';

      if (term) {
        term.setAttribute('data-theme', 'light');
        term.classList.add('theme-light');
        term.classList.remove('theme-dark');
        term.style.setProperty('--terminal-bg', '#edf3ef');
        term.style.setProperty('--terminal-color', '#03140a');
        term.style.backgroundColor = '#edf3ef';
        term.style.background = '#edf3ef';
        term.style.color = '#03140a';
      }
    } else {
      root.setAttribute('data-theme', 'dark');
      body.setAttribute('data-theme', 'dark');
      body.classList.add('theme-dark');
      body.classList.remove('theme-light');
      root.classList.add('theme-dark');
      root.classList.remove('theme-light');

      body.style.backgroundColor = '#020403';
      body.style.color = '#7df9a6';

      if (term) {
        term.setAttribute('data-theme', 'dark');
        term.classList.add('theme-dark');
        term.classList.remove('theme-light');
        term.style.setProperty('--terminal-bg', 'radial-gradient(circle at 50% 0%, #0d1a15 0%, #040807 70%, #020403 100%)');
        term.style.setProperty('--terminal-color', '#7df9a6');
        term.style.backgroundColor = '#030805';
        term.style.background = 'radial-gradient(circle at 50% 0%, #0d1a15 0%, #040807 70%, #020403 100%)';
        term.style.color = '#7df9a6';
      }
    }

    var telemPolarity = document.querySelector('.val-polarity');
    if (telemPolarity) {
      telemPolarity.textContent = isLight ? 'LIGHT_REVERSE_ALABASTER' : 'DARK_OBSIDIAN';
    }

    var polBtns = document.querySelectorAll('.polarity-btn');
    for (var m = 0; m < polBtns.length; m++) {
      var pBtn = polBtns[m];
      if (pBtn.getAttribute('data-theme') === theme) {
        pBtn.classList.add('active');
      } else {
        pBtn.classList.remove('active');
      }
    }
  }

  function initRailDrag() {
    var rail = document.getElementById('acuity-rail-track');
    if (!rail) return;

    var dragging = false;
    function updateFromPointer(e) {
      var rect = rail.getBoundingClientRect();
      var clientX = 0;
      if (e.clientX !== undefined) {
        clientX = e.clientX;
      } else if (e.touches) {
        if (e.touches.length > 0) {
          clientX = e.touches[0].clientX;
        }
      }
      var pct = ((clientX - rect.left) / rect.width) * 100;
      pct = Math.max(0, Math.min(100, pct));
      applyPrescription(Math.round(pct));
    }

    rail.addEventListener('pointerdown', function(e) {
      dragging = true;
      try { rail.setPointerCapture(e.pointerId); } catch(err) {}
      updateFromPointer(e);
    });

    rail.addEventListener('pointermove', function(e) {
      if (dragging) updateFromPointer(e);
    });

    rail.addEventListener('pointerup', function(e) {
      dragging = false;
    });

    rail.addEventListener('pointercancel', function(e) {
      dragging = false;
    });

    var slider = document.getElementById('acuity-analog-slider');
    if (slider) {
      slider.addEventListener('input', function() {
        applyPrescription(parseInt(this.value, 10));
      });
      slider.addEventListener('change', function() {
        applyPrescription(parseInt(this.value, 10));
      });
    }
  }

  // Universal Event Delegation on document for all buttons
  document.addEventListener('click', function(e) {
    if (!e || !e.target) return;
    
        var archCard = e.target.closest ? e.target.closest('.archetype-card') : null;
    if (archCard) {
      e.preventDefault();
      var archId = archCard.getAttribute('data-arch-id');
      if (archId) applyArchetype(archId);
      return;
    }

    var polBtn = e.target.closest ? e.target.closest('.polarity-btn') : null;
    if (polBtn) {
      e.preventDefault();
      var selTheme = polBtn.getAttribute('data-theme');
      if (selTheme) applyTheme(selTheme);
      return;
    }

    var acuityBtn = e.target.closest ? e.target.closest('.acuity-node-btn') : null;
    if (acuityBtn) {
      e.preventDefault();
      var tGauge = parseInt(acuityBtn.getAttribute('data-gauge') || '75', 10);
      applyPrescription(tGauge);
      return;
    }

    var tick = e.target.closest ? e.target.closest('.tick-link') : null;
    if (tick) {
      e.preventDefault();
      var tVal = parseInt(tick.getAttribute('data-val') || '75', 10);
      applyPrescription(tVal);
      return;
    }
  });

  function boot() {
    applyTheme(currentTheme);
    applyPrescription(currentGauge);
    applyArchetype(currentArchetype);
    initRailDrag();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

  // Immediate styling
  applyTheme(currentTheme);
  applyPrescription(currentGauge);
  applyArchetype(currentArchetype);
})();

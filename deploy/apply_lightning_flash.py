import os
import re

print("===> [1/4] Updating homepage.html for 3.5s White Lightning Flash on Logo Outline...")
home_path = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add the white lightning overlay layer in ub-crt-screen-viewport
old_viewport = '<img src="/wp-content/uploads/unitedbeats-logo.jpg" alt="United Beats .ONLINE Original Master Logo" class="ub-crt-master-img" />'
new_viewport = '''<img src="/wp-content/uploads/unitedbeats-logo.jpg" alt="United Beats .ONLINE Original Master Logo" class="ub-crt-master-img" />
            <!-- Pure White Inner Outline Lightning Flash Layer (Lights up every 3.5s) -->
            <img src="/wp-content/uploads/unitedbeats-white-outline-mask.png" alt="White Lightning Inner Outline" class="ub-crt-white-lightning-layer" aria-hidden="true" />'''

if 'ub-crt-white-lightning-layer' not in content:
    content = content.replace(old_viewport, new_viewport)
    print("✔ Inserted white lightning layer into CRT screen viewport.")
else:
    print("White lightning layer already present.")

# 2. Add CSS for the 3.5s white lightning flash and turn off external box pulse borders
lightning_css = '''
    /* =========================================================================
       WHITE LIGHTNING FLASH: JUST THE WHITE OUTLINE INSIDE MAIN UNITED BEATS LOGO
       Cadence: Fires a sharp double-arc white lightning flash every 3.5 seconds
       ========================================================================= */
    .ub-crt-screen-viewport {
      position: relative;
    }

    .ub-crt-white-lightning-layer {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 5;
      opacity: 0;
      mix-blend-mode: screen;
      animation: logo-white-lightning-flash 3.5s cubic-bezier(0.16, 1, 0.3, 1) infinite;
    }

    @keyframes logo-white-lightning-flash {
      0%, 82% {
        opacity: 0;
        filter: drop-shadow(0 0 0px #ffffff);
      }
      84% { /* SHARP FIRST LIGHTNING CRACK */
        opacity: 0.95;
        filter: drop-shadow(0 0 10px #ffffff) drop-shadow(0 0 25px #ffffff) brightness(2.6);
      }
      85.2% { /* RAPID MICRO-REBOUND FLICKER */
        opacity: 0.25;
        filter: drop-shadow(0 0 4px #ffffff);
      }
      86.8% { /* SECOND INTENSE WHITE LIGHTNING FLASH */
        opacity: 1;
        filter: drop-shadow(0 0 18px #ffffff) drop-shadow(0 0 40px #ffffff) drop-shadow(0 0 70px rgba(255, 255, 255, 0.9)) brightness(3.2);
      }
      88.5% { /* ELECTRIC ARC DISPERSION */
        opacity: 0.55;
        filter: drop-shadow(0 0 8px #ffffff);
      }
      90.5% {
        opacity: 0.15;
        filter: drop-shadow(0 0 3px #ffffff);
      }
      92%, 100% {
        opacity: 0;
        filter: drop-shadow(0 0 0px #ffffff);
      }
    }

    /* Disable container box border pulses so ONLY the logo outline flashes */
    .divine-pulse-outline,
    .divine-pulse-inline {
      display: none !important;
    }
'''

if 'logo-white-lightning-flash' not in content:
    content = content.replace('</style>', lightning_css + '\n    </style>')
    print("✔ Injected CSS keyframes for 3.5s White Lightning Flash.")

with open(home_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✔ homepage.html successfully saved with 3.5s lightning flash on white outline!")

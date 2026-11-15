import os
import re
from build_pillars_system import generate_solid_pillars_rail, generate_pillars_architecture_section

with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

top_rail_html = generate_solid_pillars_rail("top-pillars-rail")
pillars_arch_section = generate_pillars_architecture_section()

# 1. Insert top solid pillars rail right after vision-calibration-deck
vision_deck_end = '<!-- HUD Telemetry Header -->'
if vision_deck_end in content:
    content = content.replace(
        vision_deck_end,
        top_rail_html + '\n\n  ' + vision_deck_end
    )
    print("Inserted top solid pillars rail.")
else:
    print("Warning: could not find vision_deck_end.")

# 2. Replace the old #sub-dock section with the new Pillars & Bricks Architecture section
sub_dock_pattern = re.compile(r'(<!-- =*?\s*SUB MENU DOCK AT BOTTOM OF PAGE[\s\S]*?</section>\s*(?=<section id="public-pages"))', re.IGNORECASE)
if sub_dock_pattern.search(content):
    content = sub_dock_pattern.sub(pillars_arch_section.strip() + '\n\n', content, count=1)
    print("Replaced old sub-dock with Pillars & Bricks Architecture section.")
else:
    print("Searching alternative sub-dock pattern...")
    sub_dock_pattern2 = re.compile(r'(<section id="sub-dock"[\s\S]*?</section>)', re.IGNORECASE)
    if sub_dock_pattern2.search(content):
        content = sub_dock_pattern2.sub(pillars_arch_section.strip(), content, count=1)
        print("Replaced sub-dock by tag.")

# 3. CSS for the Solid Line Pillars Rail, Custom Geometric Angular Shapes & Brick Towers
pillars_css = '''
    /* =========================================================================
       SOLID LINE PILLARS COMMAND STRIP & PRISMATIC ANGULAR GEOMETRIC SHAPES
       ========================================================================= */
    .pillars-solid-rail {
      position: relative;
      background: #020704;
      border: 1px solid #1c5e37;
      border-radius: 8px;
      padding: 6px;
      margin: 16px 0 24px 0;
      box-shadow: 0 0 25px rgba(0, 255, 102, 0.2), inset 0 0 20px rgba(0, 0, 0, 0.9);
      overflow: hidden;
      z-index: 5;
    }

    .rail-laser-conduit {
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(90deg, transparent 0%, #00e5ff 30%, #00ff66 50%, #00e5ff 70%, transparent 100%);
      box-shadow: 0 0 10px #00ff66;
    }

    .rail-spectrum-backplane {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(
        90deg,
        rgba(255, 0, 51, 0.08) 0%,
        rgba(255, 119, 0, 0.08) 20%,
        rgba(180, 230, 0, 0.10) 45%,
        rgba(0, 255, 102, 0.16) 50%, /* Green midpoint */
        rgba(0, 229, 255, 0.10) 65%,
        rgba(88, 0, 255, 0.08) 85%,
        rgba(224, 0, 153, 0.08) 100%
      );
      pointer-events: none;
    }

    .rail-items-track {
      display: flex;
      flex-wrap: nowrap;
      gap: 6px;
      position: relative;
      z-index: 3;
      overflow-x: auto;
      padding: 2px;
      scrollbar-width: none;
    }

    .rail-items-track::-webkit-scrollbar {
      display: none;
    }

    /* Prismatic Angular Chamfered Monolith Button Shapes (Unlike Any Site In This Universe) */
    .pillar-shape-btn {
      flex: 1 1 0;
      min-width: 170px;
      position: relative;
      padding: 12px 14px;
      background: linear-gradient(135deg, rgba(6, 18, 11, 0.95) 0%, rgba(2, 8, 4, 0.98) 100%);
      border: 1px solid rgba(0, 255, 102, 0.3);
      /* Sci-Fi 45-degree Chamfered Cut on Top-Left & Bottom-Right */
      clip-path: polygon(14px 0%, 100% 0%, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0% 100%, 0% 14px);
      text-decoration: none;
      color: #ffffff;
      cursor: pointer;
      font-family: inherit;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.8);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .pillar-shape-btn:hover {
      transform: translateY(-3px);
      border-color: #00ff66;
      background: linear-gradient(135deg, rgba(10, 32, 18, 0.95) 0%, rgba(4, 16, 8, 0.98) 100%);
      box-shadow: 0 8px 25px rgba(0, 255, 102, 0.3), inset 0 0 20px rgba(0, 255, 102, 0.2);
    }

    .pillar-chamfer-edge {
      position: absolute;
      top: 0; left: 0;
      width: 14px; height: 14px;
      border-top: 2px solid #00ff66;
      border-left: 2px solid #00ff66;
      pointer-events: none;
    }

    .pillar-inner {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .pillar-tagline {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 4px;
      font-size: 0.65rem;
      font-weight: 800;
    }

    .pillar-num {
      color: #8ce4a7;
      letter-spacing: 1px;
    }

    .pillar-status {
      font-size: 0.58rem;
      padding: 1px 4px;
      border-radius: 2px;
    }

    .pillar-status.green { background: rgba(0, 255, 102, 0.2); color: #00ff66; border: 1px solid #00ff66; }
    .pillar-status.amber { background: rgba(255, 170, 0, 0.2); color: #ffaa00; border: 1px solid #ffaa00; }
    .pillar-status.cyan  { background: rgba(0, 229, 255, 0.2); color: #00e5ff; border: 1px solid #00e5ff; }
    .pillar-status.pear  { background: rgba(180, 230, 0, 0.2); color: #b4e600; border: 1px solid #b4e600; }
    .pillar-status.red   { background: rgba(255, 0, 51, 0.2); color: #ff3355; border: 1px solid #ff0033; }

    .pillar-bricks-tag {
      font-size: 0.58rem;
      color: #00e5ff;
      letter-spacing: 0.5px;
    }

    .pillar-title {
      font-size: 0.95rem;
      font-weight: 900;
      letter-spacing: 1px;
      line-height: 1.2;
    }

    .pillar-sub {
      font-size: 0.62rem;
      color: #8ce4a7;
      letter-spacing: 0.5px;
      font-weight: 700;
    }

    /* Individual Color Accents for Chamfer Buttons */
    .pillar-public:hover  { border-color: #00ff66; }
    .pillar-private:hover { border-color: #ffaa00; box-shadow: 0 8px 25px rgba(255, 170, 0, 0.3); }
    .pillar-posts:hover   { border-color: #00e5ff; box-shadow: 0 8px 25px rgba(0, 229, 255, 0.3); }
    .pillar-chips:hover   { border-color: #b4e600; box-shadow: 0 8px 25px rgba(180, 230, 0, 0.3); }
    .pillar-secret:hover  { border-color: #ff0055; box-shadow: 0 8px 25px rgba(255, 0, 85, 0.4); }

    /* Pillars & Stackable Bricks Architecture Section */
    .pillars-architecture-section {
      background: radial-gradient(circle at 50% 20%, rgba(0, 255, 102, 0.08) 0%, rgba(3, 6, 5, 0.98) 75%);
      border: 2px solid #00ff66;
      box-shadow: 0 0 35px rgba(0, 255, 102, 0.2), inset 0 0 25px rgba(0, 0, 0, 0.9);
      margin-top: 40px;
      margin-bottom: 40px;
    }

    .pillars-solid-wrapper {
      margin: 20px 0 30px 0;
    }

    .pillars-solid-label {
      font-size: 0.72rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 1.5px;
      margin-bottom: 8px;
    }

    .pillars-monolith-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 24px;
      margin-top: 20px;
    }

    .pillar-monolith-card {
      background: rgba(4, 12, 7, 0.9);
      border: 1px solid #1c5e37;
      border-radius: 8px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.3s ease;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.6);
    }

    .pillar-monolith-card:hover {
      border-color: #00ff66;
      box-shadow: 0 8px 25px rgba(0, 255, 102, 0.25);
      transform: translateY(-3px);
    }

    .monolith-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      font-size: 0.72rem;
      font-weight: 800;
    }

    .mono-code {
      color: #00ff66;
      letter-spacing: 1.5px;
    }

    .mono-badge {
      font-size: 0.65rem;
      padding: 2px 6px;
      border-radius: 3px;
    }

    .mono-badge.green { background: rgba(0, 255, 102, 0.15); color: #00ff66; border: 1px solid #00ff66; }
    .mono-badge.amber { background: rgba(255, 170, 0, 0.15); color: #ffaa00; border: 1px solid #ffaa00; }
    .mono-badge.cyan  { background: rgba(0, 229, 255, 0.15); color: #00e5ff; border: 1px solid #00e5ff; }

    .mono-title {
      font-size: 1.3rem;
      color: #ffffff;
      margin: 0 0 8px 0;
      letter-spacing: 0.5px;
    }

    .mono-desc {
      color: #b7efc5;
      font-size: 0.85rem;
      line-height: 1.6;
      margin-bottom: 18px;
    }

    /* Stackable Bricks Tower Representation */
    .brick-stack-tower {
      display: flex;
      flex-direction: column-reverse;
      gap: 6px;
      margin-bottom: 20px;
      background: rgba(0, 0, 0, 0.5);
      border: 1px dashed #174e2d;
      border-radius: 6px;
      padding: 10px;
    }

    .brick-level {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 4px;
      font-size: 0.74rem;
      background: rgba(0, 25, 12, 0.85);
      border-left: 3px solid #00ff66;
      transition: all 0.2s ease;
    }

    .brick-level:hover {
      background: rgba(0, 40, 20, 0.95);
      border-left-color: #00e5ff;
      transform: translateX(3px);
    }

    .brick-level.foundation {
      border-left-color: #ffe600;
      background: rgba(25, 20, 0, 0.6);
    }

    .brick-level.stealth {
      border-left-color: #ff0055;
      background: rgba(30, 0, 15, 0.6);
    }

    .brick-num {
      color: #00ff66;
      font-weight: 800;
      font-size: 0.65rem;
      letter-spacing: 1px;
      white-space: nowrap;
    }

    .brick-name {
      color: #d0f5db;
      font-weight: 600;
    }

    /* Hidden Spot Easter Egg Modal */
    .hidden-spot-modal {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .hidden-spot-backdrop {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(1, 4, 2, 0.88);
      backdrop-filter: blur(8px);
    }

    .hidden-spot-dialog {
      position: relative;
      z-index: 2;
      width: 100%;
      max-width: 680px;
      background: #020704;
      border: 2px solid #ff0055;
      border-radius: 8px;
      box-shadow: 0 0 40px rgba(255, 0, 85, 0.5), inset 0 0 25px rgba(0, 0, 0, 0.95);
      overflow: hidden;
      animation: modal-burst 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    @keyframes modal-burst {
      from { opacity: 0; transform: scale(0.92); }
      to { opacity: 1; transform: scale(1); }
    }

    .hidden-spot-header {
      background: #140207;
      border-bottom: 1px solid #ff0055;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .spot-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: #ff3377;
      letter-spacing: 1.5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .spot-icon {
      font-size: 1.1rem;
      color: #ff0055;
      animation: pulse-dot 1.2s infinite;
    }

    .spot-close-btn {
      background: transparent;
      border: 1px solid #ff0055;
      color: #ff6699;
      font-family: inherit;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
    }

    .spot-close-btn:hover {
      background: #ff0055;
      color: #ffffff;
    }

    .hidden-spot-body {
      padding: 24px;
    }

    .spot-lead {
      color: #ffffff;
      font-weight: 800;
      font-size: 0.92rem;
      margin-bottom: 16px;
      letter-spacing: 1px;
    }

    .spot-terminal-code {
      background: #010302;
      border: 1px solid #ff3377;
      border-radius: 6px;
      padding: 14px;
      color: #00ff66;
      font-size: 0.78rem;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .spot-terminal-code pre {
      margin: 0;
      white-space: pre-wrap;
      font-family: 'Fira Code', 'Courier New', monospace;
    }

    .spot-footer-actions {
      display: flex;
      gap: 12px;
      justify-content: flex-end;
    }
'''

# 4. JS for Hidden Spot Easter Egg
pillars_js = '''
    // =========================================================================
    // Pillars Architecture & Hidden Secret Spot Interactive Logic
    // =========================================================================
    document.addEventListener('DOMContentLoaded', function() {
      var secretTrigger = document.getElementById('secret-spot-trigger');
      var secretModal = document.getElementById('hidden-spot-modal');
      var closeBtn = document.getElementById('spot-close-btn');
      var dismissBtn = document.getElementById('spot-dismiss-btn');

      function openSecretSpot() {
        if (secretModal) {
          secretModal.style.display = 'flex';
          // Visual click flare
          if (secretTrigger) {
            secretTrigger.style.transform = 'scale(0.96)';
            setTimeout(function() { secretTrigger.style.transform = ''; }, 200);
          }
        }
      }

      function closeSecretSpot() {
        if (secretModal) {
          secretModal.style.display = 'none';
        }
      }

      if (secretTrigger) {
        secretTrigger.addEventListener('click', openSecretSpot);
      }
      if (closeBtn) {
        closeBtn.addEventListener('click', closeSecretSpot);
      }
      if (dismissBtn) {
        dismissBtn.addEventListener('click', closeSecretSpot);
      }

      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && secretModal && secretModal.style.display === 'flex') {
          closeSecretSpot();
        }
      });
    });
'''

content = content.replace('</style>', pillars_css + '\n  </style>')
content = content.replace('</script>', pillars_js + '\n  </script>')

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: deploy/homepage.html updated with Solid Line Pillars Command Strip and stackable bricks architecture!")

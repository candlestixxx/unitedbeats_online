import os
import re

def generate_solid_pillars_rail(rail_id="top-pillars-rail"):
    return f'''
  <!-- =========================================================================
       SOLID LINE PILLARS COMMAND STRIP (UNBROKEN POWER RAIL // MODULAR BRICKS)
       ========================================================================= -->
  <nav id="{rail_id}" class="pillars-solid-rail" aria-label="Site Pillars Command Strip">
    <div class="rail-laser-conduit"></div>
    <div class="rail-spectrum-backplane"></div>
    <span class="spectrum-bar bar-left"></span>
    <span class="spectrum-bar bar-right"></span>

    <div class="rail-items-track">
      <!-- Pillar I: Public Pages -->
      <a href="/public/" class="pillar-shape-btn pillar-public" title="Pillar I: Open Releases, Repos & Public Specs (Click to Open Dedicated Page)">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-01</span>
            <span class="pillar-status green">OPEN</span>
            <span class="pillar-bricks-tag">[4 BRICKS]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            PUBLIC PAGES
          </div>
          <div class="pillar-sub">OPEN ARCHIVES &amp; SPECS ↗</div>
        </div>
      </a>

      <!-- Pillar II: Private Vault -->
      <a href="/private/" class="pillar-shape-btn pillar-private" title="Pillar II: 4096-Bit Radial Vector Cipher Vault (Click to Open Dedicated Page)">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-02</span>
            <span class="pillar-status amber">RESTRICTED</span>
            <span class="pillar-bricks-tag">[3 BRICKS]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            PRIVATE VAULT
          </div>
          <div class="pillar-sub">CIPHER CLEARANCE ↗</div>
        </div>
      </a>

      <!-- Pillar III: Live Posts & Comments -->
      <a href="/posts/" class="pillar-shape-btn pillar-posts" title="Pillar III: Transmission Diary & Live Comments (Click to Open Dedicated Page)">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-03</span>
            <span class="pillar-status cyan">LIVE STREAM</span>
            <span class="pillar-bricks-tag">[4 BRICKS]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            LIVE POSTS // DIARY
          </div>
          <div class="pillar-sub">READ &amp; COMMENT ↗</div>
        </div>
      </a>

      <!-- Pillar IV: 1974 Chip Matrix -->
      <a href="#digital-billboard" class="pillar-shape-btn pillar-chips" title="Pillar IV: Alpha HyperNexus Brain & 4 New Chip Designs">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-04</span>
            <span class="pillar-status pear">SILICON</span>
            <span class="pillar-bricks-tag">[2 BRICKS]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            CHIP MATRIX
          </div>
          <div class="pillar-sub">ALPHA BRAIN &amp; 4 CHIPS ↓</div>
        </div>
      </a>

      <!-- Pillar V: Hidden Secret Spot -->
      <button type="button" class="pillar-shape-btn pillar-secret" id="secret-spot-trigger" title="Pillar V: Hidden Layer // Click to Decrypt Secret Matrix Spot">
        <div class="pillar-chamfer-edge"></div>
        <div class="pillar-inner">
          <div class="pillar-tagline">
            <span class="pillar-num">P-05</span>
            <span class="pillar-status red">HIDDEN SPOT</span>
            <span class="pillar-bricks-tag">[EASTER EGG]</span>
          </div>
          <div class="pillar-title founder-name-chroma">
            ⟦ ⟁ 0x74 PROTOCOL ⟧
          </div>
          <div class="pillar-sub">DECRYPT SECRET LAYER ⚡</div>
        </div>
      </button>
    </div>
  </nav>
'''

def generate_pillars_architecture_section():
    return '''
  <!-- =========================================================================
       SECTION: THE ARCHITECTURAL PILLARS & STACKABLE BRICKS OF LUMBROS.ME
       ========================================================================= -->
  <section id="pillars-architecture" class="terminal-section pillars-architecture-section">
    <div class="section-badge"><span>[ ARCHITECTURAL BLUEPRINT 0x10 ]</span> // THE 5 PILLARS &amp; STACKABLE BRICKS</div>
    <h2 class="section-title unicode-headline">
      ⟦ 𝗧𝗛𝗘_𝗣𝗜𝗟𝗟𝗔𝗥𝗦 // 𝗦𝗧𝗔𝗖𝗞𝗔𝗕𝗟𝗘 𝗕𝗥𝗜𝗖𝗞𝗦 &amp; 𝗛𝗜𝗗𝗗𝗘𝗡 𝗖𝗨𝗦𝗧𝗢𝗠 𝗟𝗔𝗬𝗘𝗥𝗦 ⟧
    </h2>

    <div class="pillars-manifesto-bar">
      <p class="lead-text">
        <strong>Lumbros.me</strong> is engineered as a living architectural monument. Built upon foundational <strong>Pillars</strong>, each pillar is structured to continually expand upward with stackable <strong>custom bricks</strong>, modular project layers, and hidden cryptographic nodes. Every pillar is an independent conduit connecting you to dedicated viewing and commenting sectors.
      </p>
    </div>

    <!-- Solid Line Menu Bar for Direct Cross-Sector Traversal -->
    <div class="pillars-solid-wrapper">
      <div class="pillars-solid-label">
        <span>◈ SOLID COMMAND STRIP // DIRECT SECTOR JUMP GATES:</span>
      </div>
      ''' + generate_solid_pillars_rail("bottom-pillars-rail") + '''
    </div>

    <!-- The 5 Stackable Pillars Blueprint Visualization -->
    <div class="pillars-monolith-grid">
      
      <!-- Monolith I: Public Pages -->
      <div class="pillar-monolith-card">
        <div class="monolith-head">
          <span class="mono-code">PILLAR_01</span>
          <span class="mono-badge green">PUBLIC DOMAIN</span>
        </div>
        <h3 class="mono-title">Open Archives &amp; Creative Engine</h3>
        <p class="mono-desc">Public-facing architectural releases, open-source repositories, and mathematical design frameworks.</p>
        
        <!-- Stackable Bricks Tower -->
        <div class="brick-stack-tower">
          <div class="brick-level layer-4">
            <span class="brick-num">BRICK 4</span>
            <span class="brick-name">12-Color Spectral &amp; Sonic Matrix</span>
          </div>
          <div class="brick-level layer-3">
            <span class="brick-num">BRICK 3</span>
            <span class="brick-name">candlestixxx GitHub Monorepos</span>
          </div>
          <div class="brick-level layer-2">
            <span class="brick-num">BRICK 2</span>
            <span class="brick-name">HyperNexus Dynamic Control Plane</span>
          </div>
          <div class="brick-level layer-1 foundation">
            <span class="brick-num">BRICK 1</span>
            <span class="brick-name">United Beats Audio-Synapse Core</span>
          </div>
        </div>
        <div class="mono-action">
          <a href="/public/" class="cyber-btn sm">
            <span>ENTER PUBLIC PAGES</span> <span>↗</span>
          </a>
        </div>
      </div>

      <!-- Monolith II: Private Vault -->
      <div class="pillar-monolith-card">
        <div class="monolith-head">
          <span class="mono-code">PILLAR_02</span>
          <span class="mono-badge amber">RESTRICTED</span>
        </div>
        <h3 class="mono-title">Classified Cipher Vault</h3>
        <p class="mono-desc">High-trust institutional pipelines, stealth silicon foundry tape-outs, and polar radial lattices.</p>
        
        <div class="brick-stack-tower">
          <div class="brick-level layer-4 stealth">
            <span class="brick-num">BRICK 4 [STEALTH]</span>
            <span class="brick-name">Neural Audio Stem Synthesizer Weights</span>
          </div>
          <div class="brick-level layer-3">
            <span class="brick-num">BRICK 3</span>
            <span class="brick-name">Enterprise Banking &amp; MLS Multi-Tenant Pools</span>
          </div>
          <div class="brick-level layer-2">
            <span class="brick-num">BRICK 2</span>
            <span class="brick-name">4 Custom Silicon ASIC Transistor Masks</span>
          </div>
          <div class="brick-level layer-1 foundation">
            <span class="brick-num">BRICK 1</span>
            <span class="brick-name">4096-Bit Polar Radial Vector Encryption</span>
          </div>
        </div>
        <div class="mono-action">
          <a href="/private/" class="cyber-btn sm cyber-btn-amber">
            <span>ACCESS CIPHER VAULT</span> <span>↗</span>
          </a>
        </div>
      </div>

      <!-- Monolith III: Live Posts & Comments -->
      <div class="pillar-monolith-card">
        <div class="monolith-head">
          <span class="mono-code">PILLAR_03</span>
          <span class="mono-badge cyan">LIVE TRANSMISSION</span>
        </div>
        <h3 class="mono-title">Transmission Diary &amp; Comments</h3>
        <p class="mono-desc">Lumbros's live philosophical stream of consciousness, rotating project notes, and real-time community broadcasting.</p>
        
        <div class="brick-stack-tower">
          <div class="brick-level layer-4">
            <span class="brick-num">BRICK 4</span>
            <span class="brick-name">Live Community Comment Broadcast</span>
          </div>
          <div class="brick-level layer-3">
            <span class="brick-num">BRICK 3</span>
            <span class="brick-name">Lumbros Real-Time Thought Stream</span>
          </div>
          <div class="brick-level layer-2">
            <span class="brick-num">BRICK 2</span>
            <span class="brick-name">The Blending of Everyone &amp; Time</span>
          </div>
          <div class="brick-level layer-1 foundation">
            <span class="brick-num">BRICK 1</span>
            <span class="brick-name">1974 Unix Epoch Baseline Heritage</span>
          </div>
        </div>
        <div class="mono-action">
          <a href="/posts/" class="cyber-btn sm cyber-btn-cyan">
            <span>OPEN LIVE DIARY &amp; COMMENTS</span> <span>↗</span>
          </a>
        </div>
      </div>

    </div>

    <!-- Hidden Spot Interactive Reveal Overlay (Classified Easter Egg) -->
    <div id="hidden-spot-modal" class="hidden-spot-modal" style="display: none;">
      <div class="hidden-spot-backdrop"></div>
      <div class="hidden-spot-dialog">
        <div class="hidden-spot-header">
          <div class="spot-title">
            <span class="spot-icon">⟁</span>
            <span>EASTER EGG UNLOCKED // 0x74 CLASSIFIED MATRIX NODE</span>
          </div>
          <button type="button" class="spot-close-btn" id="spot-close-btn">✕ CLOSE</button>
        </div>
        <div class="hidden-spot-body">
          <div class="spot-scanline"></div>
          <p class="spot-lead">
            YOU HAVE UNLOCKED A HIDDEN BRICK IN THE LUMBROS.ME ARCHITECTURAL MATRIX.
          </p>
          <div class="spot-terminal-code">
<pre>
[SYSTEM_OVERRIDE]: CLEARANCE ACCEPTED.
[COORDINATES]: r = 1.6180339887 | θ = 137.50776405° (GOLDEN RATIO POLAR ANCHOR)
[METRIC]: HARMONIC_RESONANCE = 550nm (EMERALD MIDPOINT) == 432Hz HARMONIC A
[TRANSMISSION]: "Creativity, mathematics, and spiritual frequency are one continuum.
                 Every brick added to this site expands the universal signal."
[STATUS]: AUTH_CODE_0x74 // GOD &amp; MATH ARCHITECTURE OPERATIONAL.
</pre>
          </div>
          <div class="spot-footer-actions">
            <a href="/posts/" class="cyber-btn sm">
              <span>TRANSMIT REACTION TO DIARY</span> <span>⚡</span>
            </a>
            <button type="button" class="cyber-btn sm cyber-btn-dim" id="spot-dismiss-btn">
              <span>DISMISS OVERLAY</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

print("Pillars and Bricks generator ready.")

import re
import os

def generate_sub_dock_html():
    return '''
  <!-- =========================================================================
       SUB MENU DOCK AT BOTTOM OF PAGE: ROOT SECTOR MATRIX & TIME CONTINUUM
       ========================================================================= -->
  <section id="sub-dock" class="terminal-section sub-dock-matrix">
    <div class="section-badge"><span>[ ROOT SECTOR MATRIX 0x09 ]</span> // SUB_DOCK : PUBLIC, PRIVATE &amp; LIVE POSTS</div>
    <h2 class="section-title unicode-headline">
      ⟦ 𝗦𝗨𝗕_𝗗𝗢𝗖𝗞 // 𝗡𝗔𝗩𝗜𝗚𝗔𝗧𝗜𝗢𝗡 &amp; 𝗥𝗢𝗧𝗔𝗧𝗜𝗡𝗚 𝗣𝗥𝗢𝗝𝗘𝗖𝗧 𝗠𝗔𝗧𝗥𝗜𝗫 ⟧
    </h2>
    <div class="sub-dock-lead">
      <p class="lead-text">
        Universal project navigation matrix for <strong>Lumbros.me</strong> &amp; <strong>United Beats LLC</strong>. As projects rotate across cycles, this sub-menu serves as your persistent bridge to our <strong>Public Archives</strong>, <strong>Encrypted Private Vault</strong>, and <strong>Live Posts Diary</strong>.
      </p>
    </div>

    <!-- Ticker Line like our names with 7-Pattern Circulating Kinetic Rhythm -->
    <div class="sub-dock-ticker-bar">
      <div class="sub-ticker-label">
        <span class="live-beacon-dot"></span>
        <span class="ticker-badge-text">CONTINUUM STREAM:</span>
      </div>
      <div class="sub-dock-ticker-viewport">
        <div class="sub-dock-ticker-track">
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 01. PUBLIC_PAGES : OPEN ARCHIVES &amp; CURRENT RELEASES ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 02. PRIVATE_PAGES : 4096-BIT RADIAL VECTOR CIPHER VAULT ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 03. LIVE_POSTS : TRANSMISSION DIARY &amp; REAL-TIME COMMENTS ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ THE BLENDING OF EVERYONE AND TIME : WE ARE THE FREQUENCY ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 01. PUBLIC_PAGES : OPEN ARCHIVES &amp; CURRENT RELEASES ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 02. PRIVATE_PAGES : 4096-BIT RADIAL VECTOR CIPHER VAULT ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ 03. LIVE_POSTS : TRANSMISSION DIARY &amp; REAL-TIME COMMENTS ⟧</span>
          </span>
          <span class="ticker-flow-sep">◈</span>
          <span class="ticker-flow-item">
            <span class="founder-name-chroma sub-ticker-text">⟦ THE BLENDING OF EVERYONE AND TIME : WE ARE THE FREQUENCY ⟧</span>
          </span>
        </div>
      </div>
    </div>

    <!-- 12-Color Spectrum Menu Box Grid with Twin Non-Colliding Oscillating Vertical Bars -->
    <div class="sub-dock-nav-grid">
      <!-- Option 1: Public Pages -->
      <div class="sub-dock-card chip-gold">
        <span class="spectrum-bar bar-left"></span>
        <span class="spectrum-bar bar-right"></span>
        <div class="sub-card-inner">
          <div class="sub-card-header">
            <span class="chip-dot"></span>
            <span class="sub-card-code">SECTOR 0x01</span>
            <span class="sub-badge green">PUBLIC // UNRESTRICTED</span>
          </div>
          <h3 class="sub-card-title">
            <span class="founder-name-chroma">PUBLIC PAGES</span>
          </h3>
          <div class="sub-card-subtitle">ROTATING PROJECTS &amp; OPEN ARCHIVES</div>
          <p class="sub-card-desc">
            Public architecture roadmaps, open-source repos, United Beats public API gateways, and creative vector art systems.
          </p>
          <div class="sub-card-actions">
            <a href="#public-pages" class="sub-btn inpage-btn">
              <span>EXPLORE IN-PAGE</span> <span class="arrow">↓</span>
            </a>
            <a href="/public/" class="sub-btn permalink-btn" target="_blank" rel="noopener">
              <span>PERMALINK</span> <span class="arrow">↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Option 2: Private Pages -->
      <div class="sub-dock-card chip-pear is-center-node">
        <span class="spectrum-bar bar-left"></span>
        <span class="spectrum-bar bar-right"></span>
        <div class="sub-card-inner">
          <div class="sub-card-header">
            <span class="chip-dot"></span>
            <span class="sub-card-code">SECTOR 0x02</span>
            <span class="sub-badge amber">RESTRICTED // CIPHER</span>
          </div>
          <h3 class="sub-card-title">
            <span class="founder-name-chroma">PRIVATE PAGES</span>
          </h3>
          <div class="sub-card-subtitle">CLASSIFIED CIPHER VAULT</div>
          <p class="sub-card-desc">
            Stealth ASIC silicon schematics, high-net-worth enterprise multi-tenant pipelines, and proprietary neural audio models.
          </p>
          <div class="sub-card-actions">
            <a href="#private-pages" class="sub-btn inpage-btn">
              <span>UNLOCK IN-PAGE</span> <span class="arrow">↓</span>
            </a>
            <a href="/private/" class="sub-btn permalink-btn" target="_blank" rel="noopener">
              <span>SECURE GATE</span> <span class="arrow">↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Option 3: Live Posts / Diary -->
      <div class="sub-dock-card chip-cyan">
        <span class="spectrum-bar bar-left"></span>
        <span class="spectrum-bar bar-right"></span>
        <div class="sub-card-inner">
          <div class="sub-card-header">
            <span class="chip-dot"></span>
            <span class="sub-card-code">SECTOR 0x03</span>
            <span class="sub-badge cyan">LIVE DIARY STREAM</span>
          </div>
          <h3 class="sub-card-title">
            <span class="founder-name-chroma">LIVE POSTS</span>
          </h3>
          <div class="sub-card-subtitle">TRANSMISSION DIARY &amp; COMMENTS</div>
          <p class="sub-card-desc">
            Lumbros\'s stream of consciousness, project rotation thoughts, cosmic time continuum, and interactive reader reflections.
          </p>
          <div class="sub-card-actions">
            <a href="#live-posts" class="sub-btn inpage-btn">
              <span>READ &amp; TRANSMIT</span> <span class="arrow">↓</span>
            </a>
            <a href="/posts/" class="sub-btn permalink-btn" target="_blank" rel="noopener">
              <span>FULLSCREEN DIARY</span> <span class="arrow">↗</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       SECTION 9: PUBLIC PAGES // ROTATING PROJECTS & OPEN ARCHIVES
       ========================================================================= -->
  <section id="public-pages" class="terminal-section">
    <div class="section-badge"><span>[ SECTOR 0x01 ]</span> // PUBLIC PAGES &amp; CURRENT ROTATING PROJECTS</div>
    <h2 class="section-title unicode-headline">
      ⟦ 𝗣𝗨𝗕𝗟𝗜𝗖_𝗦𝗘𝗖𝗧𝗢𝗥 // 𝗢𝗣𝗘𝗡 𝗔𝗥𝗖𝗛𝗜𝗩𝗘𝗦 &amp; 𝗥𝗢𝗧𝗔𝗧𝗜𝗡𝗚 𝗣𝗥𝗢𝗝𝗘𝗖𝗧𝗦 ⟧
    </h2>
    <div class="terminal-callout">
      <p class="lead-text">
        As our creative and technical ecosystem evolves, Lumbros continuously rotates active developments here. Everything here is built to be shared with scholars, artists, engineers, and creators worldwide.
      </p>
    </div>

    <div class="public-projects-grid">
      <!-- Project 1: United Beats Audio-Synapse Core -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-UB-01</span>
          <span class="status-pill green">ACTIVE ROTATION</span>
        </div>
        <h3 class="proj-title">United Beats Audio-Synapse Core</h3>
        <div class="proj-tagline">Spatial Sound Engine &amp; Multi-Tenant Harmonic Routing</div>
        <p class="proj-desc">
          A zero-latency digital sound architecture marrying analog 1974 audio synthesis principles with modern web sockets. Routes spatialized audio stems across distributed nodes while preserving raw analog warmth and dynamic range.
        </p>
        <div class="proj-specs">
          <span>◈ Audio WebSockets</span>
          <span>◈ 12-Tone Harmonic Matrix</span>
          <span>◈ Web Audio API / Rust Core</span>
        </div>
        <div class="proj-footer">
          <a href="https://unitedbeats.online" target="_blank" rel="noopener" class="cyber-btn sm">
            <span>VISIT UNITEDBEATS.ONLINE</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Project 2: HyperNexus Control Plane -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-HN-02</span>
          <span class="status-pill green">PRODUCTION CONTROL PLANE</span>
        </div>
        <h3 class="proj-title">HyperNexus Universal API Gateway</h3>
        <div class="proj-tagline">TormentNexus Powered Model Context Protocol (MCP) Router</div>
        <p class="proj-desc">
          Universal multi-tenant routing layer allowing AI agents, real estate MLS feeds, and enterprise CRMs to execute dynamic tenant context switches without database cross-contamination or cold starts.
        </p>
        <div class="proj-specs">
          <span>◈ MCP Protocol v1</span>
          <span>◈ Polar Radial Storage</span>
          <span>◈ Sub-millisecond Dispatch</span>
        </div>
        <div class="proj-footer">
          <a href="#topology" class="cyber-btn sm">
            <span>INSPECT TOPOLOGY</span> <span>↓</span>
          </a>
        </div>
      </article>

      <!-- Project 3: Candlestixxx GitHub Ecosystem -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-CTX-03</span>
          <span class="status-pill green">OPEN SOURCE REPOSITORIES</span>
        </div>
        <h3 class="proj-title">candlestixxx Code Ecosystem</h3>
        <div class="proj-tagline">Open-Source Monorepos, WordPress Engines &amp; UI Shaders</div>
        <p class="proj-desc">
          Directly synchronizing Lumbros\'s production work across Hetzner, GitHub, and local workstations. Includes full WordPress headless configs, Nginx reverse proxy optimizations, and custom cyber shaders.
        </p>
        <div class="proj-specs">
          <span>◈ GitHub / candlestixxx</span>
          <span>◈ Nginx 1.24 + PHP 8.4</span>
          <span>◈ Bash &amp; PowerShell Sync</span>
        </div>
        <div class="proj-footer">
          <a href="https://github.com/candlestixxx" target="_blank" rel="noopener" class="cyber-btn sm">
            <span>VIEW CANDLESTIXXX GITHUB</span> <span>↗</span>
          </a>
        </div>
      </article>

      <!-- Project 4: 12-Color Spectral & Sonic Matrix -->
      <article class="cyber-card public-proj-card">
        <div class="card-glow-bar"></div>
        <div class="card-meta">
          <span class="proj-id">PROJ-SPEC-04</span>
          <span class="status-pill green">MATHEMATICAL DESIGN SYSTEM</span>
        </div>
        <h3 class="proj-title">The 12-Color Spectral &amp; Harmonic Matrix</h3>
        <div class="proj-tagline">Harmonic Wave Bridge with Green Center Midpoint</div>
        <p class="proj-desc">
          A visual design philosophy mapping the 12 hues of visible light directly to the 12 chromatic semitones of music. Anchored by emerald green at 50% and pear at 45%, providing visual equilibrium across high-density consoles.
        </p>
        <div class="proj-specs">
          <span>◈ 12 Spectral Nodes</span>
          <span>◈ Non-Colliding Oscillators</span>
          <span>◈ KaTeX / KaTeX Polar Geometry</span>
        </div>
        <div class="proj-footer">
          <a href="/public/" class="cyber-btn sm">
            <span>OPEN PUBLIC SPEC SHEET</span> <span>↗</span>
          </a>
        </div>
      </article>
    </div>
  </section>

  <!-- =========================================================================
       SECTION 10: PRIVATE PAGES // CLASSIFIED CIPHER VAULT
       ========================================================================= -->
  <section id="private-pages" class="terminal-section private-vault-section">
    <div class="section-badge"><span>[ SECTOR 0x02 ]</span> // PRIVATE PAGES &amp; ENCRYPTED VAULT</div>
    <h2 class="section-title unicode-headline">
      ⟦ 𝗣𝗥𝗜𝗩𝗔𝗧𝗘_𝗦𝗘𝗖𝗧𝗢𝗥 // 𝗖𝗟𝗔𝗦𝗦𝗜𝗙𝗜𝗘𝗗 𝗖𝗜𝗣𝗛𝗘𝗥 𝗩𝗔𝗨𝗟𝗧 ⟧
    </h2>
    <div class="terminal-callout alert-amber">
      <div class="callout-header">
        <span class="warning-icon">⚠</span>
        <strong>SECURITY RESTRICTION: LEVEL-5 CLEARANCE REQUIRED</strong>
      </div>
      <p class="lead-text">
        This vault guards proprietary hardware schematics, enterprise multi-tenant database contracts, stealth silicon foundry tape-outs, and unreleased United Beats audio neural weights.
      </p>
    </div>

    <!-- Terminal Decryption Console -->
    <div class="vault-console-box">
      <div class="vault-console-header">
        <div class="console-title">
          <span class="console-led red" id="vault-led"></span>
          <span>candlestixxx@lumbros-node: /vault/secure-sector</span>
        </div>
        <div class="console-protocol">CIPHER: 4096-BIT RADIAL POLAR</div>
      </div>

      <div class="vault-console-body">
        <div class="terminal-feed" id="vault-feed">
          <p class="console-line"><span class="prompt-sym">[SYSTEM]</span> Kernel initialization complete. Polar coordinate grid locked.</p>
          <p class="console-line"><span class="prompt-sym">[SYSTEM]</span> 3 Classified Briefings in stealth partition. Authentication required.</p>
          <p class="console-line"><span class="prompt-sym">[HINT]</span> Authorized test ciphers: <code>HYPERNEXUS</code>, <code>UNITEDBEATS</code>, <code>1974</code>, <code>LUMBROS</code></p>
        </div>

        <!-- Decryption Form -->
        <form id="vault-auth-form" class="vault-input-row" onsubmit="return false;">
          <label for="vault-passcode" class="vault-input-label">PASSCODE_CIPHER &gt;</label>
          <input type="password" id="vault-passcode" class="vault-text-input" placeholder="ENTER ACCESS KEY / PASSPHRASE..." autocomplete="off">
          <button type="submit" id="vault-auth-btn" class="cyber-btn cyber-btn-amber">
            <span>DECRYPT PROTOCOL</span> <span>⚡</span>
          </button>
          <a href="#contact-uplink" class="cyber-btn cyber-btn-dim">
            <span>REQUEST CLEARANCE</span> <span>🔑</span>
          </a>
        </form>
      </div>

      <!-- Decrypted Classified Partition (Hidden by Default) -->
      <div id="vault-decrypted-content" class="vault-classified-grid" style="display: none;">
        <div class="classified-alert">
          <span class="unlock-icon">🔓</span>
          <span>CLEARANCE GRANTED // 4096-BIT RADIAL VECTOR CIPHER UNLOCKED. ACCESSING SECURE PARTITION:</span>
        </div>

        <div class="vault-items-grid">
          <!-- Item 1: ASIC Schematics -->
          <div class="vault-card">
            <div class="vault-card-header">
              <span class="vault-badge red">CLASSIFIED TOP-SECRET</span>
              <span class="vault-timestamp">FOUNDRY TAPE-OUT 2027</span>
            </div>
            <h4 class="vault-title">4 Custom Silicon ASIC Schematics</h4>
            <p class="vault-p">
              Physical transistor masks and hardware microcode for the <strong>NEXUS-NEURO-CORE α-1</strong> and <strong>VECT-CRYPTO-SECURE v2</strong>. Full vector ALU layout optimizing in-memory polar coordinate math.
            </p>
            <div class="vault-meta-tag">PARTITION: /hw/tapeout/vrl1_revB.gds</div>
          </div>

          <!-- Item 2: Enterprise Multi-Tenant Banking -->
          <div class="vault-card">
            <div class="vault-card-header">
              <span class="vault-badge red">CLASSIFIED COMMERCIAL</span>
              <span class="vault-timestamp">ACTIVE ENTERPRISE PILOT</span>
            </div>
            <h4 class="vault-title">Enterprise MLS &amp; Banking Dynamic Bridge</h4>
            <p class="vault-p">
              Dedicated single-tenant execution clusters and isolated database connection pools engineered for Tier-1 real estate brokerages and multi-jurisdictional fintech gateways.
            </p>
            <div class="vault-meta-tag">PARTITION: /enterprise/contracts/vrl_tier1.enc</div>
          </div>

          <!-- Item 3: Neural Stem Synthesizer -->
          <div class="vault-card">
            <div class="vault-card-header">
              <span class="vault-badge red">CLASSIFIED CREATIVE</span>
              <span class="vault-timestamp">UNITED BEATS STEALTH LABS</span>
            </div>
            <h4 class="vault-title">Proprietary Audio Neural Frequency Synthesizer</h4>
            <p class="vault-p">
              Next-generation spatial harmonic model synthesizing audio waveforms directly from raw vector embeddings in real time, delivering true analog warmth over digital streams.
            </p>
            <div class="vault-meta-tag">PARTITION: /audio/weights/synapse_v4.onnx</div>
          </div>
        </div>

        <div class="vault-footer-links">
          <a href="/private/" class="cyber-btn" target="_blank" rel="noopener">
            <span>OPEN DEDICATED PRIVATE PORTAL</span> <span>↗</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================================================================
       SECTION 11: LIVE POSTS // TRANSMISSION DIARY & REAL-TIME COMMENTS
       ========================================================================= -->
  <section id="live-posts" class="terminal-section live-posts-section">
    <div class="section-badge"><span>[ SECTOR 0x03 ]</span> // LIVE POSTS : TRANSMISSION DIARY &amp; REAL-TIME COMMENTS</div>
    <h2 class="section-title unicode-headline">
      ⟦ 𝗟𝗜𝗩𝗘_𝗣𝗢𝗦𝗧𝗦 // 𝗧𝗥𝗔𝗡𝗦𝗠𝗜𝗦𝗦𝗜𝗢𝗡 𝗗𝗜𝗔𝗥𝗬 &amp; 𝗧𝗜𝗠𝗘 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗨𝗠 ⟧
    </h2>

    <!-- The Philosophical Continuum Banner: Blending Everyone and Time -->
    <div class="continuum-manifesto-box">
      <div class="manifesto-scanlines"></div>
      <div class="manifesto-content">
        <div class="manifesto-header">
          <span class="manifesto-epoch">UNIX TIME: 1794703800 // BLENDING 1974 → 2026 → ∞</span>
          <span class="manifesto-badge">THE CONTINUUM PHILOSOPHY</span>
        </div>
        <h3 class="manifesto-headline">
          "TIME DOES NOT SEPARATE US; WE ARE THE ONE CONTINUOUS FREQUENCY."
        </h3>
        <p class="manifesto-body">
          From the earliest geometers who mapped the harmony of the spheres, through the binary telegraph keys of 1844, into the 1974 Unix teletype terminals at Bell Labs, and now inside our distributed AI HyperNexus, humanity is engaged in one continuous act of creation.
        </p>
        <p class="manifesto-sub">
          We are not isolated fragments in time. Every coder, digital artist, musician, and scholar from every continent and culture across all eras vibrates in this identical signal. This diary is Lumbros\'s live thought stream—honoring the past, anchoring the present, and transmitting into the boundless future.
        </p>
        <div class="manifesto-tagline">
          <span>◈ WE ARE THE CREATORS</span>
          <span>◈ WE ARE THE HARMONY</span>
          <span>◈ WE ARE THE SIGNAL</span>
        </div>
      </div>
    </div>

    <!-- Live Diary Entries Stream by Lumbros Kourlos -->
    <div class="diary-stream-container">
      <div class="stream-header-bar">
        <div class="stream-title">
          <span class="live-dot-pulse"></span>
          <span>LUMBROS KOURLOS // LIVE DIARY LOGS</span>
        </div>
        <div class="stream-filters">
          <span class="filter-pill active">ALL TRANSMISSIONS</span>
          <span class="filter-pill">#HARMONICS</span>
          <span class="filter-pill">#RADIAL_VECTOR</span>
          <span class="filter-pill">#TIME_CONTINUUM</span>
        </div>
      </div>

      <div class="diary-entries-list">
        <!-- Entry 108 -->
        <article class="diary-entry-card">
          <div class="entry-meta">
            <span class="entry-seq">LOG #108</span>
            <span class="entry-date">2026-11-15 01:45:00 UTC</span>
            <span class="entry-tag">#UNITED_BEATS #12_SPECTRUM #HARMONICS</span>
          </div>
          <h4 class="entry-title">The Harmonic Confluence: Why Sound, Light, and Code Are One Spectrum</h4>
          <div class="entry-text">
            <p>
              When Harry, Bob, and I were engineering the 12-color spectrum backplane for United Beats, we realized something profound: the visible light spectrum from 400nm to 700nm maps exactly to the 12 musical semitones of an octave. Emerald green sits at the precise geometric midpoint—550 nanometers. In musical terms, that is the perfect fifth, the tonal anchor.
            </p>
            <p>
              In our API gateway, we use this exact same harmonic division. When an incoming API request lands, its tenant identity is not hashed with random noise; it is resolved into a polar coordinate angle. Light, sound, and data structures are the same mathematics wearing different garments.
            </p>
          </div>
          <div class="entry-footer">
            <span class="author-tag">TRANSMITTED BY: LUMBROS KOURLOS</span>
            <span class="checksum">HASH: 0x9B1D_744B</span>
          </div>
        </article>

        <!-- Entry 107 -->
        <article class="diary-entry-card">
          <div class="entry-meta">
            <span class="entry-seq">LOG #107</span>
            <span class="entry-date">2026-11-14 19:22:18 UTC</span>
            <span class="entry-tag">#HYPERNEXUS #RADIAL_VECTOR #POLAR_GEOMETRY</span>
          </div>
          <h4 class="entry-title">Radial Vectors vs Relational Grids: The Geometry of Absolute Secrecy</h4>
          <div class="entry-text">
            <p>
              Relational databases force every tenant into a shared Cartesian grid: rows, columns, foreign keys. If a query leaks, it leaks across an entire table. Bob Matthew Pelloni and I asked: why force multi-tenant architectures into Euclidean rectangles?
            </p>
            <p>
              By encoding secrets onto radial vectors in polar space, each company\'s credentials occupy a distinct radial ray at $(r, \theta)$. Unless your encryption key calculates the exact angle and radial distance, you are not simply blocked by an access control check—you literally do not exist in the same mathematical dimension. Zero cross-talk, zero leakage.
            </p>
          </div>
          <div class="entry-footer">
            <span class="author-tag">TRANSMITTED BY: LUMBROS KOURLOS</span>
            <span class="checksum">HASH: 0x3F88_20A1</span>
          </div>
        </article>

        <!-- Entry 106 -->
        <article class="diary-entry-card">
          <div class="entry-meta">
            <span class="entry-seq">LOG #106</span>
            <span class="entry-date">2026-11-13 23:04:12 UTC</span>
            <span class="entry-tag">#TIME_CONTINUUM #CREATIVE_SPIRIT #UNIX1974</span>
          </div>
          <h4 class="entry-title">The Blending of Everyone and Time: The Digital Hearth for Global Creators</h4>
          <div class="entry-text">
            <p>
              Walking around Detroit, between the echoes of Motown, the techno rhythms of the Belleville Three, and the industrial foundry steel, you feel how human culture is an unbreakable chain. 
            </p>
            <p>
              When you code in 2026 on a Unix terminal whose ancestors were drafted at Xerox PARC and Bell Labs in 1974, you realize that you are standing around the exact same digital hearth. We welcome every creator, coder, scholar, and artist from every corner of this planet to step into this light. We are all building the same cathedral.
            </p>
          </div>
          <div class="entry-footer">
            <span class="author-tag">TRANSMITTED BY: LUMBROS KOURLOS</span>
            <span class="checksum">HASH: 0x7E14_442A</span>
          </div>
        </article>

        <!-- Entry 105 -->
        <article class="diary-entry-card">
          <div class="entry-meta">
            <span class="entry-seq">LOG #105</span>
            <span class="entry-date">2026-11-12 14:50:00 UTC</span>
            <span class="entry-tag">#CHIP_DESIGN #SILICON #ALPHA_BRAIN</span>
          </div>
          <h4 class="entry-title">Silicon Foundry Dispatch: The 4 Neural Chips Born From the Alpha Brain</h4>
          <div class="entry-text">
            <p>
              Software simulation is only the beginning. The Alpha HyperNexus Brain requires dedicated physical silicon to bypass the von Neumann bottleneck. The 4 chips we announced—NEXUS-NEURO-CORE, VECT-CRYPTO-SECURE, DYN-ROUTER-QUANTUM, and MCP-SYNAPSE-GATE—bring memory and computation into the exact same physical lattice.
            </p>
            <p>
              Zero latency is not an aspiration; it is the physical law of our hardware. More updates coming as we progress through test bench validation.
            </p>
          </div>
          <div class="entry-footer">
            <span class="author-tag">TRANSMITTED BY: LUMBROS KOURLOS</span>
            <span class="checksum">HASH: 0x4EF3_8D02</span>
          </div>
        </article>
      </div>
    </div>

    <!-- Live Visitor Reflection & Comment Broadcast Terminal -->
    <div class="diary-broadcast-terminal">
      <div class="terminal-bar">
        <span class="term-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></span>
        <span class="term-title">CONTINUUM_UPLINK // BROADCAST YOUR THOUGHT TO THE LIVE DIARY</span>
      </div>

      <div class="terminal-body-stream">
        <div class="terminal-intro">
          Leave your permanent mark in the continuum. Transmit your thought, reflection, or collaboration signal to Lumbros\'s live diary feed. Your signal will be logged to WordPress and notified directly to <code>UnitedBeatsLLC@gmail.com</code>.
        </div>

        <form id="diary-comment-form" class="diary-form-grid" onsubmit="return false;">
          <div class="form-group-half">
            <label for="diary-author" class="term-label">YOUR CALLSIGN / NAME &gt;</label>
            <input type="text" id="diary-author" class="term-input" placeholder="e.g. Elena Vance, CyberNomad, Dr. Aris" required>
          </div>
          <div class="form-group-half">
            <label for="diary-location" class="term-label">FREQUENCY / LOCATION NODE &gt;</label>
            <input type="text" id="diary-location" class="term-input" placeholder="e.g. Detroit Studio, Tokyo Node, Berlin Labs">
          </div>
          <div class="form-group-full">
            <label for="diary-email" class="term-label">CONTACT EMAIL (OPTIONAL / PRIVATE RELAY) &gt;</label>
            <input type="email" id="diary-email" class="term-input" placeholder="your.frequency@domain.com">
          </div>
          <div class="form-group-full">
            <label for="diary-thought" class="term-label">TRANSMISSION / THOUGHT FOR THE DIARY &gt;</label>
            <textarea id="diary-thought" class="term-textarea" rows="3" placeholder="Share your perspective on the blending of time, technology, art, and the universe..." required></textarea>
          </div>
          <div class="form-actions">
            <button type="submit" id="diary-submit-btn" class="cyber-btn cyber-btn-cyan">
              <span class="btn-text">BROADCAST SIGNAL TO CONTINUUM</span> <span>⚡</span>
            </button>
            <span id="diary-feedback" class="diary-feedback-msg"></span>
          </div>
        </form>

        <!-- Live Comments Feed Stream -->
        <div class="live-community-stream">
          <div class="community-stream-title">
            <span>⟦ RECEIVED COMMUNITY TRANSMISSIONS ⟧</span>
            <span class="stream-status">● LIVE STREAM BUFFER</span>
          </div>
          <div id="diary-community-feed" class="community-feed-list">
            <!-- Dynamically populated & pre-seeded -->
            <div class="community-msg-item">
              <div class="msg-header">
                <span class="msg-author">Aether_Coder</span>
                <span class="msg-loc">Sector 04 // Athens Node</span>
                <span class="msg-time">2026-11-15 01:12:44</span>
              </div>
              <div class="msg-body">
                The convergence of 1974 unix logic and radial vectors is stunning. Honored to witness the signal.
              </div>
            </div>
            <div class="community-msg-item">
              <div class="msg-header">
                <span class="msg-author">Kassandra_V</span>
                <span class="msg-loc">Detroit // Harmonic Studio</span>
                <span class="msg-time">2026-11-14 22:45:19</span>
              </div>
              <div class="msg-body">
                Sound frequencies, color wavelengths, and digital code are one continuous spectrum. United Beats embodies this!
              </div>
            </div>
            <div class="community-msg-item">
              <div class="msg-header">
                <span class="msg-author">CyberSage_74</span>
                <span class="msg-loc">Bell Labs Legacy Net</span>
                <span class="msg-time">2026-11-14 18:30:00</span>
              </div>
              <div class="msg-body">
                Ken Thompson and Dennis Ritchie would smile at this terminal. Pure respect to the continuous epoch.
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
'''

print("Sub-dock HTML generator ready.")

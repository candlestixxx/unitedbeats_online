import re

with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Executive Summary Top Menu Chip
content = content.replace(
    '<span class="chip-content"><span class="chip-dot"></span>01. EXECUTIVE SUMMARY</span>',
    '<span class="chip-content"><span class="chip-dot"></span>01. LEADERSHIP &amp; INTEGRITY PLAN</span>'
)

# 2. Update Executive Summary Header & Lead Text
exec_old = '''  <!-- Section 1: Executive Summary -->
  <section id="executive-summary" class="terminal-section">
    <div class="section-badge"><span>[ SECTION 0x01 ]</span> // CORE MISSION MANIFESTO</div>
    <h2 class="section-title">⚡ Executive Summary</h2>
    <div class="terminal-callout">
      <p class="lead-text">
        This business plan outlines the architecture for a <strong>universal, multi-tenant API gateway and dynamic control plane</strong> engineered under the <strong>HyperNexus</strong> umbrella for <strong>United Beats LLC</strong> and enterprise intelligence ecosystems.
      </p>'''

exec_new = '''  <!-- Section 1: Executive Summary -->
  <section id="executive-summary" class="terminal-section">
    <div class="section-badge"><span>[ SECTION 0x01 ]</span> // LEADERSHIP WITH BUSINESS INTEGRITY PLAN</div>
    <h2 class="section-title">⚡ Executive Summary // Leadership with Business Integrity</h2>
    <div class="terminal-callout">
      <p class="lead-text">
        Anchored in executive leadership with uncompromising business integrity, this strategic architectural plan outlines the deployment of a <strong>universal, multi-tenant API gateway and dynamic control plane</strong> engineered under the <strong>HyperNexus</strong> umbrella for <strong>United Beats LLC</strong> and enterprise intelligence ecosystems.
      </p>'''

if exec_old in content:
    content = content.replace(exec_old, exec_new)
    print("Replaced Executive Summary with Leadership with Business Integrity.")
else:
    print("Warning: Executive summary block not matched exactly, trying regex.")
    content = re.sub(
        r'This business plan outlines the architecture for a <strong>universal, multi-tenant API gateway',
        r'Anchored in executive leadership with uncompromising business integrity, this strategic architectural plan outlines the deployment of a <strong>universal, multi-tenant API gateway',
        content
    )

# 3. Update Lumbros Kourlos Command Leadership Card
lum_bio_old = '''        <div class="founder-role">SYS_ARCHITECT | CREATIVE DIRECTOR | CO-FOUNDER</div>
        <div class="founder-bio">
          <p>
            Fusing enterprise systems architecture with raw artistic discipline. Educated at <strong>Wayne State University</strong> and the <strong>College for Creative Studies</strong>, Lumbros architects resilient digital ecosystems designed with mathematical precision and visceral human connection.
          </p>
          <ul class="skills-list">
            <li><span class="bullet">▣</span> High-End UI/UX Graphic Design &amp; Brand Systems</li>
            <li><span class="bullet">▣</span> Autonomous AI Workflow Routing &amp; Agent Mesh</li>
            <li><span class="bullet">▣</span> Grassroots Community Action &amp; Tech Evangelism</li>
            <li><span class="bullet">▣</span> Enterprise CRM Synthesis &amp; Growth Mechanics</li>
          </ul>
        </div>
        <div class="card-footer">
          <span class="status-pill green">STATUS: ACCEPTING NETWORKING INQUIRIES</span>
        </div>'''

lum_bio_new = '''        <div class="founder-role">ABSTRACT MATHEMATICIAN | VISUAL ARTIST | SYSTEMS ARCHITECT</div>
        <div class="founder-bio">
          <p>
            Awarded a scholarship to <strong>Wayne State University</strong>, Lumbros is an abstract mathematician who approaches complex system architectures through visual reasoning as an accomplished visual &amp; digital artist. By translating multidimensional mathematical abstractions into spatial visual structures, he architects resilient digital ecosystems designed with mathematical precision, deep integrity, and visceral human connection.
          </p>
          <ul class="skills-list">
            <li><span class="bullet">▣</span> Abstract Mathematical Modeling &amp; Spatial Visual Reasoning</li>
            <li><span class="bullet">▣</span> High-End UI/UX Graphic Design &amp; Brand Systems</li>
            <li><span class="bullet">▣</span> Autonomous AI Workflow Routing &amp; Agent Mesh</li>
            <li><span class="bullet">▣</span> Enterprise Systems Architecture &amp; Dynamic Gateways</li>
          </ul>
        </div>
        <div class="card-footer" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
          <span class="status-pill green">STATUS: ACCEPTING NETWORKING INQUIRIES</span>
          <a href="https://github.com/candlestixxx" target="_blank" rel="noopener" class="founder-gh-btn">
            <span>⌨ GITHUB: @candlestixxx</span> <span>↗</span>
          </a>
        </div>'''

if lum_bio_old in content:
    content = content.replace(lum_bio_old, lum_bio_new)
    print("Updated Lumbros Kourlos command leadership card.")
else:
    print("Warning: lum_bio_old not matched exactly.")

# 4. Update Robert Matthew Pelloni Command Leadership Card
bob_bio_old = '''        <div class="card-footer">
          <span class="status-pill green">STATUS: ACCEPTING NETWORKING INQUIRIES</span>
        </div>
      </article>'''

bob_bio_new = '''        <div class="card-footer" style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
          <span class="status-pill green">STATUS: ACCEPTING NETWORKING INQUIRIES</span>
          <a href="https://github.com/robertpelloni" target="_blank" rel="noopener" class="founder-gh-btn">
            <span>⌨ GITHUB: @robertpelloni</span> <span>↗</span>
          </a>
        </div>
      </article>'''

# Make sure we only replace in Bob's card
pattern_bob = re.compile(r'(<article class="cyber-card founder-bob-card">[\s\S]*?)<div class="card-footer">\s*<span class="status-pill green">STATUS: ACCEPTING NETWORKING INQUIRIES</span>\s*</div>\s*</article>')
if pattern_bob.search(content):
    content = pattern_bob.sub(r'\1' + bob_bio_new, content, count=1)
    print("Updated Robert Matthew Pelloni card with live GitHub link.")
else:
    print("Warning: Bob card pattern not matched.")

# 5. Update Creator Persona Card in Section 2.5
persona_old = '''        <!-- Creator Persona Card -->
        <div class="creator-persona-card">
          <div class="creator-title-badge">COMMAND ARCHITECT // MULTIVERSE CREATOR</div>
          <h3 class="creator-name">LUMBROS KOURLOS</h3>
          <div class="creator-roles">
            <span>◈ SYSTEMS ARCHITECT</span>
            <span>◈ VISUAL &amp; DIGITAL ARTIST</span>
            <span>◈ TECH CREATOR</span>
          </div>
          <p class="creator-statement">
            Bridging raw artistic intuition with enterprise systems architecture. We architect digital ecosystems that possess structural integrity, aesthetic soul, and universal harmony. We humbly invite forward-thinking minds, scholars, mathematical engineers, digital artists, and everyday creators from every culture on this planet and beyond to connect and build with us.
          </p>
        </div>'''

persona_new = '''        <!-- Creator Persona Card -->
        <div class="creator-persona-card">
          <div class="creator-title-badge">COMMAND ARCHITECT // MULTIVERSE CREATOR</div>
          <h3 class="creator-name">LUMBROS KOURLOS</h3>
          <div class="creator-roles">
            <span>◈ ABSTRACT MATHEMATICIAN</span>
            <span>◈ VISUAL &amp; DIGITAL ARTIST</span>
            <span>◈ SYSTEMS ARCHITECT</span>
          </div>
          <p class="creator-statement">
            Awarded a scholarship to <strong>Wayne State University</strong>, Lumbros is an abstract mathematician who channels visual reasoning through his identity as a visual artist to solve complex architectural problems. We architect digital ecosystems that possess mathematical rigor, structural integrity, and aesthetic soul. We humbly invite forward-thinking minds, scholars, mathematical engineers, digital artists, and everyday creators from every culture on this planet and beyond to connect and build with us.
          </p>
          <div style="margin-top: 12px;">
            <a href="https://github.com/candlestixxx" target="_blank" rel="noopener" class="founder-gh-btn">
              <span>⌨ GITHUB PROFILE: @candlestixxx</span> <span>↗</span>
            </a>
          </div>
        </div>'''

if persona_old in content:
    content = content.replace(persona_old, persona_new)
    print("Updated Creator Persona card.")
else:
    print("Warning: persona_old not matched exactly.")

# 6. Add CSS for .founder-gh-btn
gh_css = '''
    .founder-gh-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 1px;
      color: #00e5ff;
      background: rgba(0, 229, 255, 0.12);
      border: 1px solid rgba(0, 229, 255, 0.4);
      border-radius: 4px;
      text-decoration: none;
      transition: all 0.2s ease;
    }
    .founder-gh-btn:hover {
      background: #00e5ff;
      color: #030605;
      box-shadow: 0 0 12px #00e5ff;
      transform: translateY(-2px);
    }
'''

content = content.replace('</style>', gh_css + '\n  </style>')

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: deploy/homepage.html updated!")

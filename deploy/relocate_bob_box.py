import os

home_file = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Target block to remove from uplink-form-col
block_to_remove = '''

        <!-- Creator Persona Card: Robert Matthew Pelloni (Lower Right Sector) -->
        <div class="creator-persona-card bob-persona-card">
          <div class="creator-title-badge">LEAD SOFTWARE ARCHITECT // CO-FOUNDER</div>
          <h3 class="creator-name">ROBERT MATTHEW PELLONI</h3>
          <div class="creator-roles">
            <span>◈ FULL STACK DEVELOPER</span>
            <span>◈ COMPUTER PROGRAMMER</span>
            <span>◈ SOFTWARE ARCHITECT</span>
            <span>◈ GAME CREATOR</span>
            <span>◈ MCP MASTER &amp; MULTI-SYSTEMS EXPERT</span>
          </div>
          <p class="creator-statement">
            Full Stack Developer, Computer Programmer, and Software Architect who engineered and built his own proprietary video game from the ground up. An expert in multi-systems engineering and master in Model Context Protocol (MCP), Bob solves massive data organization challenges at scale, constructing high-throughput, zero-latency digital architectures and distributed pipelines designed for extreme computing envelopes.
          </p>
          <div style="margin-top: 14px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
            <a href="https://github.com/robertpelloni" target="_blank" rel="noopener noreferrer" class="founder-gh-btn bob-profile-btn" style="border-color: #00e5ff; color: #00e5ff;">
              <span>⌨ GITHUB PROFILE: @robertpelloni</span> <span>↗</span>
            </a>
            <span style="font-size: 0.72rem; color: #00e5ff; letter-spacing: 1px; font-weight: 600;">[ MULTI-SYSTEMS &amp; MCP EXPERT ]</span>
          </div>
        </div>

        <!-- Negative Reverse Horizontal Bar Contact Hub: Robert Matthew Pelloni (Lower Right Corner) -->
        <div class="contact-neg-bar bob-contact-bar">
          <div class="neg-bar-beam"></div>
          <div class="contact-item">
            <span class="contact-label">DIRECT PHONE:</span>
            <a href="tel:5867443333" class="contact-val spectrum-flash-text">+1 (586) 744-3333</a>
          </div>
          <div class="contact-divider">|</div>
          <div class="contact-item">
            <span class="contact-label">EMAIL UPLINK:</span>
            <a href="mailto:UnitedBeatsLLC@gmail.com" class="contact-val spectrum-flash-text">UnitedBeatsLLC@gmail.com</a>
          </div>
          <div class="contact-divider">|</div>
          <div class="contact-item">
            <span class="contact-label">SECTOR:</span>
            <span class="contact-val" style="color: #00e5ff; font-size: 0.95rem; font-weight: 700; letter-spacing: 1.5px; text-shadow: 0 0 8px rgba(0, 229, 255, 0.6);">CO-FOUNDER // ARCHITECT</span>
          </div>
        </div>'''

if block_to_remove not in content:
    print("ERROR: block_to_remove not found!")
    exit(1)

content = content.replace(block_to_remove, '')
print("✔ Removed new box menu from uplink-form-col.")

# 2. Target insertion point: right after Robert's GitHub ecosystem box closing tag, inside uplink-profile-col
# Robert's GitHub box closes at:
#             </div>
#           </div>
#         </div>
# </div>
#
#       <!-- Right Column: Interactive Quantum Uplink Form -->

old_end_of_left_col = '''              <a href="https://github.com/robertpelloni/workspace" target="_blank" rel="noopener noreferrer" class="repo-chip">
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
</div>'''

bob_vertical_box = '''              <a href="https://github.com/robertpelloni/workspace" target="_blank" rel="noopener noreferrer" class="repo-chip">
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

        <!-- Creator Persona Card: Robert Matthew Pelloni (Under Robert's GitHub Section) -->
        <div class="creator-persona-card bob-persona-card">
          <div class="creator-title-badge">LEAD SOFTWARE ARCHITECT // CO-FOUNDER</div>
          <h3 class="creator-name">ROBERT MATTHEW PELLONI</h3>
          <div class="creator-roles">
            <span>◈ FULL STACK DEVELOPER</span>
            <span>◈ COMPUTER PROGRAMMER</span>
            <span>◈ SOFTWARE ARCHITECT</span>
            <span>◈ GAME CREATOR</span>
            <span>◈ MCP MASTER &amp; MULTI-SYSTEMS EXPERT</span>
          </div>
          <p class="creator-statement">
            Full Stack Developer, Computer Programmer, and Software Architect who engineered and built his own proprietary video game from the ground up. An expert in multi-systems engineering and master in Model Context Protocol (MCP), Bob solves massive data organization challenges at scale, constructing high-throughput, zero-latency digital architectures and distributed pipelines designed for extreme computing envelopes.
          </p>
          <div style="margin-top: 12px;">
            <a href="https://github.com/robertpelloni" target="_blank" rel="noopener noreferrer" class="founder-gh-btn bob-profile-btn" style="border-color: #00e5ff; color: #00e5ff;">
              <span>⌨ GITHUB PROFILE: @robertpelloni</span> <span>↗</span>
            </a>
          </div>
        </div>

        <!-- Negative Reverse Horizontal Bar Contact Hub: Robert Matthew Pelloni -->
        <div class="contact-neg-bar bob-contact-bar">
          <div class="neg-bar-beam"></div>
          <div class="contact-item">
            <span class="contact-label">DIRECT PHONE:</span>
            <a href="tel:5867443333" class="contact-val spectrum-flash-text">+1 (586) 744-3333</a>
          </div>
          <div class="contact-divider">|</div>
          <div class="contact-item">
            <span class="contact-label">EMAIL UPLINK:</span>
            <a href="mailto:UnitedBeatsLLC@gmail.com" class="contact-val spectrum-flash-text">UnitedBeatsLLC@gmail.com</a>
          </div>
        </div>
      </div>'''

if old_end_of_left_col not in content:
    print("ERROR: old_end_of_left_col not found!")
    exit(1)

content = content.replace(old_end_of_left_col, bob_vertical_box)
print("✔ Placed Robert Pelloni persona card & contact bar in vertical box under Robert's GitHub section.")

with open(home_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Updated homepage.html!")

import os

home_file = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix @ROBERBELLONI typos
content = content.replace('@ROBERBELLONI', '@ROBERTPELLONI')

# Check if bob-persona-card already present
if 'bob-persona-card' in content:
    print('Already present in homepage.html!')
    exit(0)

# 1. Add CSS for bob-persona-card and bob-contact-bar
css_marker = '/* Negative Reverse Horizontal Bar Contact Hub */'
bob_css = '''    /* Robert Matthew Pelloni Creator Persona & Contact Bar (Lower Right Corner) */
    .bob-persona-card {
      background: rgba(3, 14, 24, 0.75);
      border: 1px solid #00e5ff55;
      border-left: 4px solid #00e5ff;
      border-radius: 8px;
      padding: 22px;
      margin-top: 24px;
      margin-bottom: 16px;
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 0 25px rgba(0, 229, 255, 0.08), 0 0 20px rgba(0, 229, 255, 0.15);
    }

    .bob-persona-card::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #00e5ff, #8000ff, #00ff66);
    }

    .bob-persona-card .creator-title-badge {
      color: #00e5ff;
      letter-spacing: 2px;
      font-weight: 700;
      font-size: 0.72rem;
      margin-bottom: 6px;
    }

    .bob-persona-card .creator-name {
      color: #ffffff;
      font-size: 1.35rem;
      margin: 0 0 6px 0;
      text-shadow: 0 0 10px rgba(0, 229, 255, 0.6);
    }

    .bob-persona-card .creator-roles {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      font-size: 0.74rem;
      color: #00e5ff;
      font-weight: 700;
      margin-bottom: 12px;
      letter-spacing: 1px;
    }

    .bob-persona-card .creator-statement {
      color: #c0f4fc;
      font-size: 0.88rem;
      line-height: 1.65;
      margin: 0;
    }

    .bob-contact-bar {
      border: 1px solid rgba(0, 229, 255, 0.45) !important;
      box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.95), 0 0 25px rgba(0, 229, 255, 0.22) !important;
    }

    .bob-contact-bar .contact-label {
      color: #00e5ff !important;
    }

    .bob-contact-bar .contact-divider {
      color: #0a4f66 !important;
    }

'''

if css_marker not in content:
    print(f"ERROR: {css_marker} not found!")
    exit(1)

content = content.replace(css_marker, bob_css + css_marker)

# 2. Add Bob's Persona Card and Contact Bar in uplink-form-col below the form
target_form_close = '''            <div class="form-action-row">
              <button type="submit" id="uplink-submit-btn" class="uplink-submit-button">
                <span class="btn-text">TRANSMIT UPLINK SIGNAL</span>
                <span class="btn-glyph">⚡</span>
              </button>
              <div id="uplink-status-feedback" class="form-feedback-area"></div>
            </div>
          </form>
        </div>'''

bob_html_insertion = '''

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

if target_form_close not in content:
    print('ERROR: target_form_close not found in homepage.html!')
    exit(1)

content = content.replace(target_form_close, target_form_close + bob_html_insertion)

with open(home_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('SUCCESS: Updated deploy/homepage.html!')

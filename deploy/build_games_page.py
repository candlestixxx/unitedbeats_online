import os
import re

print("===> Building deploy/games.html from original Sections 9 & 9.5...")

# We can read original Sections 9 and 9.5
# In the previous git commit b8fdb77, homepage.html contained sections 9 and 9.5
import subprocess
res = subprocess.run(['git', 'show', 'b8fdb77:deploy/homepage.html'], capture_output=True, text=True, encoding='utf-8')
old_home = res.stdout

s_9_marker = old_home.find('<section id="shadertoy-tribute"')
s_pillars_marker = old_home.find('<section id="pillars-architecture"')

if s_9_marker != -1 and s_pillars_marker != -1:
    games_content = old_home[s_9_marker:s_pillars_marker]
    print(f"✔ Extracted {len(games_content)} characters for games.html.")
else:
    print("ERROR: Could not find sections in HEAD:deploy/homepage.html")
    exit(1)

# Now read modern homepage.html for styles, scripts, header, audio
home_path = os.path.join(os.path.dirname(__file__), 'homepage.html')
with open(home_path, 'r', encoding='utf-8') as f:
    home = f.read()

# Extract <style>...</style> block
style_match = re.search(r'(<style>[\s\S]*?</style>)', home)
styles = style_match.group(1) if style_match else ''

# Extract <script>...</script> block
script_match = re.search(r'(<script>[\s\S]*?</script>)', home)
scripts = script_match.group(1) if script_match else ''

# Extract ASCII Header
header_match = re.search(r'(<header class="ascii-hero[^>]*>[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

# Extract Top Pillars Navigation Rail
pillars_match = re.search(r'(<nav class="pillars-solid-rail[^>]*" id="top-pillars-rail"[\s\S]*?</nav>)', home)
top_pillars_rail = pillars_match.group(1) if pillars_match else ''

# Extract Footer
footer_match = re.search(r'(<footer class="terminal-footer">[\s\S]*?</footer>)', home)
footer = footer_match.group(1) if footer_match else ''

# Extract Floating Audio Engine
audio_hud_match = re.search(r'(<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->)', home)
audio_hud = audio_hud_match.group(1) if audio_hud_match else ''

games_page_html = f'''<div class="terminal-wrapper theme-cyberpunk">
  <!-- Top Terminal HUD Banner -->
  <div class="hud-top-bar">
    <div class="hud-status-badge">
      <span class="live-dot-pulse"></span>
      <span>SYSTEM OPERATIONAL // NODE: UNITEDBEATS.ONLINE // COOL CONCEPT GAMES</span>
    </div>
    <div class="hud-nav-links">
      <a href="/" class="hud-link">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link">LIVE POSTS</a>
      <span class="hud-sep">|</span>
      <a href="/games/" class="hud-link active">COOL CONCEPT GAMES</a>
    </div>
  </div>

  {top_pillars_rail}

  {ascii_header}

  <!-- Page Breadcrumbs -->
  <div class="terminal-section" style="margin-bottom: 20px; padding: 12px 20px;">
    <div style="font-size: 0.76rem; letter-spacing: 1.5px; color: #8ce4a7; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
      <div>
        <a href="/" style="color: #00ff66; text-decoration: none;">ROOT</a> / 
        <span style="color: #00e5ff; font-weight: 800;">COOL CONCEPT GAMES // PROCEDURAL SHADERTOY &amp; SPECTRUM MONOPOLY</span>
      </div>
      <div style="color: #00ff66; font-weight: 700;">
        ARCADE SECTOR // GPU COMPUTE: ACTIVE
      </div>
    </div>
  </div>

  {games_content}

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

games_file = os.path.join(os.path.dirname(__file__), 'games.html')
with open(games_file, 'w', encoding='utf-8') as f:
    f.write(games_page_html)

print("✔ deploy/games.html successfully created!")

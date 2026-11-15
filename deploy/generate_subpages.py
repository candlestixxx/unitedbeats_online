import os
import re

# Read styles, ASCII header, and footer from homepage.html
with open('deploy/homepage.html', 'r', encoding='utf-8') as f:
    home = f.read()

# Extract <style>...</style> block
style_match = re.search(r'(<style>[\s\S]*?</style>)', home)
styles = style_match.group(1) if style_match else ''

# Extract <script>...</script> block
script_match = re.search(r'(<script>[\s\S]*?</script>)', home)
scripts = script_match.group(1) if script_match else ''

# Extract ASCII Header
header_match = re.search(r'(<header class="ascii-hero">[\s\S]*?</header>)', home)
ascii_header = header_match.group(1) if header_match else ''

# Extract Top Pillars Navigation Rail
pillars_match = re.search(r'(<nav class="solid-line-pillars" id="top-pillars-rail"[\s\S]*?</nav>)', home)
top_pillars_rail = pillars_match.group(1) if pillars_match else ''

# Extract Sub-Dock
sub_dock_match = re.search(r'(<section id="sub-dock"[\s\S]*?</section>)', home)
sub_dock = sub_dock_match.group(1) if sub_dock_match else ''

# Extract Public Section
public_match = re.search(r'(<section id="public-pages"[\s\S]*?</section>)', home)
public_sec = public_match.group(1) if public_match else ''

# Extract Private Section
private_match = re.search(r'(<section id="private-pages"[\s\S]*?</section>)', home)
private_sec = private_match.group(1) if private_match else ''

# Extract Live Posts Section
posts_match = re.search(r'(<section id="live-posts"[\s\S]*?</section>)', home)
posts_sec = posts_match.group(1) if posts_match else ''

# Extract Footer
footer_match = re.search(r'(<footer class="terminal-footer">[\s\S]*?</footer>)', home)
footer = footer_match.group(1) if footer_match else ''

# Extract YouTube Audio Engine
audio_hud_match = re.search(r'(<!-- YouTube Audio Engine -->[\s\S]*?<!-- End YouTube Audio Engine -->)', home)
audio_hud = audio_hud_match.group(1) if audio_hud_match else ''

def build_page(page_title, active_slug, main_content_html):
    return f'''<div class="terminal-wrapper theme-cyberpunk">
  <!-- Top Terminal HUD Banner -->
  <div class="hud-top-bar">
    <div class="hud-status-badge">
      <span class="live-dot-pulse"></span>
      <span>SYSTEM OPERATIONAL // NODE: UNITEDBEATS.ONLINE // {active_slug.upper()}</span>
    </div>
    <div class="hud-nav-links">
      <a href="/" class="hud-link">⌂ ROOT SYSTEM</a>
      <span class="hud-sep">|</span>
      <a href="/public/" class="hud-link {'active' if active_slug=='public' else ''}">PUBLIC</a>
      <span class="hud-sep">|</span>
      <a href="/private/" class="hud-link {'active' if active_slug=='private' else ''}">PRIVATE</a>
      <span class="hud-sep">|</span>
      <a href="/posts/" class="hud-link {'active' if active_slug=='posts' else ''}">LIVE POSTS</a>
    </div>
  </div>

  {top_pillars_rail}

  {ascii_header}

  <!-- Page Breadcrumbs -->
  <div class="terminal-section" style="margin-bottom: 20px; padding: 12px 20px;">
    <div style="font-size: 0.76rem; letter-spacing: 1.5px; color: #8ce4a7; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
      <div>
        <a href="/" style="color: #00ff66; text-decoration: none;">ROOT</a> / 
        <span style="color: #ffffff; font-weight: 800;">{page_title}</span>
      </div>
      <div style="color: #00e5ff; font-weight: 700;">
        CONTINUUM EPOCH: +1794703800s
      </div>
    </div>
  </div>

  {main_content_html}

  {sub_dock}

  {footer}

  {audio_hud}

  {styles}

  {scripts}
</div>'''

# 1. Generate deploy/posts.html
posts_page = build_page("LIVE POSTS // TRANSMISSION DIARY & REAL-TIME COMMENTS", "posts", posts_sec)
with open('deploy/posts.html', 'w', encoding='utf-8') as f:
    f.write(posts_page)
print("Generated deploy/posts.html")

# 2. Generate deploy/public.html
public_page = build_page("PUBLIC SECTOR // OPEN ARCHIVES & ROTATING PROJECTS", "public", public_sec)
with open('deploy/public.html', 'w', encoding='utf-8') as f:
    f.write(public_page)
print("Generated deploy/public.html")

# 3. Generate deploy/private.html
private_page = build_page("PRIVATE SECTOR // CLASSIFIED CIPHER VAULT", "private", private_sec)
with open('deploy/private.html', 'w', encoding='utf-8') as f:
    f.write(private_page)
print("Generated deploy/private.html")

import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_sections import generate_sub_dock_html

# Read current homepage.html
homepage_path = 'deploy/homepage.html'
with open(homepage_path, 'r', encoding='utf-8') as f:
    content = f.read()
sub_dock_html = generate_sub_dock_html()

# CSS definitions to append
css_to_append = '''
    /* =========================================================================
       SUB MENU DOCK & ROTATING PROJECT MATRIX STYLING
       ========================================================================= */
    .sub-dock-matrix {
      background: radial-gradient(circle at 50% 20%, rgba(0, 255, 102, 0.08) 0%, rgba(3, 6, 5, 0.98) 75%);
      border: 2px solid #1c5e37;
      box-shadow: 0 0 35px rgba(0, 255, 102, 0.15), inset 0 0 25px rgba(0, 0, 0, 0.8);
      position: relative;
      margin-top: 40px;
      margin-bottom: 40px;
    }

    .sub-dock-lead {
      margin-bottom: 20px;
    }

    /* Sub-Dock Ticker Bar with 7-Pattern Circulating Gradient Text */
    .sub-dock-ticker-bar {
      display: flex;
      align-items: center;
      background: rgba(0, 20, 10, 0.85);
      border: 1px solid #00ff66;
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 25px;
      box-shadow: 0 0 15px rgba(0, 255, 102, 0.25), inset 0 0 10px rgba(0, 0, 0, 0.8);
      overflow: hidden;
    }

    .sub-ticker-label {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #00ff66;
      padding-right: 14px;
      border-right: 1px solid #1c5e37;
      white-space: nowrap;
      text-shadow: 0 0 8px rgba(0, 255, 102, 0.6);
    }

    .sub-dock-ticker-viewport {
      overflow: hidden;
      white-space: nowrap;
      flex-grow: 1;
      mask-image: linear-gradient(90deg, transparent 0%, black 5%, black 95%, transparent 100%);
      -webkit-mask-image: linear-gradient(90deg, transparent 0%, black 5%, black 95%, transparent 100%);
    }

    .sub-dock-ticker-track {
      display: inline-flex;
      align-items: center;
      gap: 24px;
      animation: sub-ticker-slide 28s linear infinite;
    }

    .sub-dock-ticker-track:hover {
      animation-play-state: paused;
    }

    @keyframes sub-ticker-slide {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    .sub-ticker-text {
      font-size: 0.82rem;
      font-weight: 800;
      letter-spacing: 1px;
    }

    .ticker-flow-sep {
      color: #00e5ff;
      text-shadow: 0 0 8px #00e5ff;
      font-size: 0.75rem;
    }

    /* Sub-Dock Cards Grid with 12-Color Spectrum Background & Twin Oscillating Bars */
    .sub-dock-nav-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
    }

    .sub-dock-card {
      position: relative;
      overflow: hidden;
      border-radius: 8px;
      border: 1px solid rgba(0, 255, 102, 0.3);
      background: linear-gradient(
        90deg,
        rgba(255, 0, 51, 0.12) 0%,
        rgba(255, 61, 0, 0.12) 9%,
        rgba(255, 119, 0, 0.12) 18%,
        rgba(255, 170, 0, 0.12) 27%,
        rgba(255, 230, 0, 0.12) 36%,
        rgba(180, 230, 0, 0.16) 45%,
        rgba(0, 255, 102, 0.22) 50%,
        rgba(0, 240, 170, 0.16) 55%,
        rgba(0, 229, 255, 0.12) 64%,
        rgba(0, 119, 255, 0.12) 73%,
        rgba(88, 0, 255, 0.12) 82%,
        rgba(224, 0, 153, 0.12) 100%
      );
      backdrop-filter: blur(6px);
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.7), 0 4px 15px rgba(0, 0, 0, 0.6);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .sub-dock-card:hover {
      transform: translateY(-4px);
      border-color: #00ff66;
      box-shadow: 0 12px 30px rgba(0, 255, 102, 0.25), inset 0 0 25px rgba(0, 255, 102, 0.15);
    }

    .sub-card-inner {
      position: relative;
      z-index: 3;
      padding: 22px 20px;
    }

    .sub-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      font-size: 0.72rem;
      font-weight: 700;
    }

    .sub-card-code {
      color: #8ce4a7;
      letter-spacing: 1.5px;
    }

    .sub-card-title {
      font-size: 1.35rem;
      margin: 0 0 6px 0;
      letter-spacing: 1px;
    }

    .sub-card-subtitle {
      font-size: 0.74rem;
      letter-spacing: 1.5px;
      color: #00e5ff;
      font-weight: 700;
      margin-bottom: 12px;
    }

    .sub-card-desc {
      color: #b7efc5;
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 18px;
    }

    .sub-card-actions {
      display: flex;
      gap: 10px;
    }

    .sub-btn {
      flex: 1;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 12px;
      font-size: 0.74rem;
      font-weight: 800;
      letter-spacing: 1px;
      text-decoration: none;
      border-radius: 4px;
      transition: all 0.2s ease;
    }

    .inpage-btn {
      background: rgba(0, 255, 102, 0.15);
      color: #00ff66;
      border: 1px solid #00ff66;
    }

    .inpage-btn:hover {
      background: #00ff66;
      color: #030605;
      box-shadow: 0 0 12px #00ff66;
    }

    .permalink-btn {
      background: rgba(0, 229, 255, 0.12);
      color: #00e5ff;
      border: 1px solid rgba(0, 229, 255, 0.4);
    }

    .permalink-btn:hover {
      background: #00e5ff;
      color: #030605;
      box-shadow: 0 0 12px #00e5ff;
    }

    /* Public Sector Projects Grid */
    .public-projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }

    .public-proj-card {
      background: rgba(4, 12, 8, 0.85);
      border: 1px solid #1c5e37;
      padding: 22px;
    }

    .proj-id {
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      color: #00ff66;
      font-weight: 800;
    }

    .proj-title {
      font-size: 1.25rem;
      color: #ffffff;
      margin: 10px 0 6px 0;
    }

    .proj-tagline {
      font-size: 0.76rem;
      color: #00e5ff;
      font-weight: 700;
      margin-bottom: 12px;
      letter-spacing: 1px;
    }

    .proj-desc {
      color: #b7efc5;
      font-size: 0.88rem;
      line-height: 1.6;
      margin-bottom: 16px;
    }

    .proj-specs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 12px;
      border-top: 1px dashed #174e2d;
      margin-bottom: 16px;
      font-size: 0.72rem;
      color: #8ce4a7;
    }

    /* Private Vault Section */
    .private-vault-section {
      border-color: rgba(255, 170, 0, 0.4);
      background: radial-gradient(circle at 50% 10%, rgba(255, 119, 0, 0.08) 0%, rgba(4, 8, 5, 0.98) 75%);
    }

    .vault-console-box {
      background: #020604;
      border: 1px solid #ffaa00;
      border-radius: 8px;
      box-shadow: 0 0 25px rgba(255, 170, 0, 0.2);
      overflow: hidden;
      margin-top: 20px;
    }

    .vault-console-header {
      background: #08120a;
      border-bottom: 1px solid #ffaa00;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.74rem;
      color: #ffcc99;
      letter-spacing: 1.5px;
      font-weight: 700;
    }

    .console-led {
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      margin-right: 8px;
    }

    .console-led.red {
      background: #ff0033;
      box-shadow: 0 0 8px #ff0033;
    }

    .console-led.green {
      background: #00ff66;
      box-shadow: 0 0 8px #00ff66;
    }

    .vault-console-body {
      padding: 20px;
    }

    .vault-feed {
      font-size: 0.82rem;
      line-height: 1.6;
      color: #e5ff80;
      margin-bottom: 18px;
    }

    .vault-input-row {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }

    .vault-input-label {
      color: #ffaa00;
      font-weight: 800;
      font-size: 0.8rem;
      letter-spacing: 1px;
    }

    .vault-text-input {
      flex-grow: 1;
      min-width: 260px;
      background: #010402;
      border: 1px solid #ffaa00;
      color: #00ff66;
      font-family: inherit;
      font-size: 0.88rem;
      padding: 10px 14px;
      border-radius: 4px;
      outline: none;
    }

    .vault-text-input:focus {
      border-color: #00ff66;
      box-shadow: 0 0 12px rgba(0, 255, 102, 0.4);
    }

    .cyber-btn-amber {
      background: rgba(255, 170, 0, 0.2);
      border-color: #ffaa00;
      color: #ffe099;
    }

    .cyber-btn-amber:hover {
      background: #ffaa00;
      color: #030605;
      box-shadow: 0 0 15px #ffaa00;
    }

    .cyber-btn-dim {
      background: rgba(255, 255, 255, 0.05);
      border-color: #555555;
      color: #aaaaaa;
    }

    .vault-classified-grid {
      padding: 24px;
      border-top: 1px dashed #ffaa00;
      background: rgba(255, 170, 0, 0.03);
    }

    .classified-alert {
      color: #00ff66;
      font-weight: 800;
      font-size: 0.85rem;
      letter-spacing: 1.5px;
      margin-bottom: 18px;
    }

    .vault-items-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin-bottom: 20px;
    }

    .vault-card {
      background: rgba(5, 15, 10, 0.9);
      border: 1px solid #ff5500;
      padding: 18px;
      border-radius: 6px;
    }

    .vault-card-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      font-size: 0.7rem;
      font-weight: 700;
    }

    .vault-badge.red {
      background: rgba(255, 0, 51, 0.2);
      color: #ff6680;
      border: 1px solid #ff0033;
      padding: 2px 6px;
      border-radius: 3px;
    }

    .vault-timestamp {
      color: #ffcc99;
    }

    .vault-title {
      font-size: 1.1rem;
      color: #ffffff;
      margin: 0 0 8px 0;
    }

    .vault-p {
      color: #b7efc5;
      font-size: 0.84rem;
      line-height: 1.6;
      margin-bottom: 12px;
    }

    .vault-meta-tag {
      font-size: 0.68rem;
      color: #8ce4a7;
      font-weight: 700;
      border-top: 1px dashed #1c5e37;
      padding-top: 8px;
    }

    /* Continuum Manifesto Box */
    .continuum-manifesto-box {
      position: relative;
      background: radial-gradient(circle at 50% 0%, rgba(0, 229, 255, 0.12) 0%, rgba(4, 10, 7, 0.98) 70%);
      border: 2px solid #00e5ff;
      border-radius: 8px;
      padding: 28px;
      margin-bottom: 30px;
      box-shadow: 0 0 30px rgba(0, 229, 255, 0.2), inset 0 0 20px rgba(0, 0, 0, 0.8);
      overflow: hidden;
    }

    .manifesto-scanlines {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(rgba(0, 229, 255, 0.03) 50%, rgba(0, 0, 0, 0.3) 50%);
      background-size: 100% 4px;
      pointer-events: none;
    }

    .manifesto-content {
      position: relative;
      z-index: 2;
    }

    .manifesto-header {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 14px;
      font-size: 0.74rem;
      letter-spacing: 2px;
      font-weight: 800;
    }

    .manifesto-epoch {
      color: #00e5ff;
      text-shadow: 0 0 8px #00e5ff;
    }

    .manifesto-badge {
      background: rgba(0, 255, 102, 0.15);
      border: 1px solid #00ff66;
      color: #00ff66;
      padding: 2px 8px;
      border-radius: 4px;
    }

    .manifesto-headline {
      font-size: 1.55rem;
      color: #ffffff;
      margin: 0 0 16px 0;
      line-height: 1.35;
      text-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
      letter-spacing: 1px;
    }

    .manifesto-body {
      font-size: 1.02rem;
      color: #e0ffe6;
      line-height: 1.7;
      margin-bottom: 12px;
    }

    .manifesto-sub {
      font-size: 0.92rem;
      color: #a3e9be;
      line-height: 1.6;
      margin-bottom: 18px;
    }

    .manifesto-tagline {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.78rem;
      font-weight: 800;
      color: #00ff66;
      letter-spacing: 2px;
      border-top: 1px solid rgba(0, 229, 255, 0.3);
      padding-top: 14px;
    }

    /* Live Diary Feed & Entries */
    .stream-header-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 18px;
      padding-bottom: 10px;
      border-bottom: 1px solid #14442a;
    }

    .stream-title {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.88rem;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #00ff66;
    }

    .live-dot-pulse {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #00ff66;
      box-shadow: 0 0 10px #00ff66;
      animation: pulse-dot 1.5s infinite;
    }

    .stream-filters {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-pill {
      font-size: 0.7rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 3px;
      border: 1px solid #1c5e37;
      color: #8ce4a7;
      cursor: pointer;
      background: rgba(0, 0, 0, 0.4);
      transition: all 0.2s ease;
    }

    .filter-pill.active, .filter-pill:hover {
      border-color: #00ff66;
      color: #00ff66;
      background: rgba(0, 255, 102, 0.12);
    }

    .diary-entries-list {
      display: grid;
      gap: 20px;
      margin-bottom: 35px;
    }

    .diary-entry-card {
      background: rgba(3, 10, 6, 0.85);
      border: 1px solid #1c5e37;
      border-radius: 6px;
      padding: 22px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
      transition: all 0.2s ease;
    }

    .diary-entry-card:hover {
      border-color: #00ff66;
      box-shadow: 0 6px 20px rgba(0, 255, 102, 0.15);
    }

    .entry-meta {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
      font-size: 0.72rem;
      font-weight: 700;
    }

    .entry-seq {
      color: #00ff66;
      letter-spacing: 1.5px;
    }

    .entry-date {
      color: #00e5ff;
    }

    .entry-tag {
      color: #b4e600;
    }

    .entry-title {
      font-size: 1.28rem;
      color: #ffffff;
      margin: 0 0 12px 0;
      letter-spacing: 0.5px;
    }

    .entry-text p {
      color: #d0f5db;
      font-size: 0.92rem;
      line-height: 1.7;
      margin-bottom: 10px;
    }

    .entry-footer {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 8px;
      margin-top: 14px;
      padding-top: 10px;
      border-top: 1px dashed #174e2d;
      font-size: 0.68rem;
      color: #8ce4a7;
      font-weight: 700;
    }

    /* Broadcast Terminal */
    .diary-broadcast-terminal {
      background: #020604;
      border: 2px solid #00e5ff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 0 25px rgba(0, 229, 255, 0.18);
    }

    .terminal-body-stream {
      padding: 24px;
    }

    .terminal-intro {
      font-size: 0.88rem;
      color: #b7efc5;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    .diary-form-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 25px;
    }

    .form-group-half {
      flex: 1 1 calc(50% - 10px);
      min-width: 240px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .form-group-full {
      flex: 1 1 100%;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .term-label {
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      color: #00e5ff;
      font-weight: 800;
    }

    .term-input, .term-textarea {
      background: #010402;
      border: 1px solid #1c5e37;
      border-radius: 4px;
      color: #ffffff;
      font-family: inherit;
      font-size: 0.88rem;
      padding: 10px 14px;
      outline: none;
      transition: all 0.2s ease;
    }

    .term-input:focus, .term-textarea:focus {
      border-color: #00e5ff;
      box-shadow: 0 0 12px rgba(0, 229, 255, 0.4);
    }

    .cyber-btn-cyan {
      background: rgba(0, 229, 255, 0.2);
      border-color: #00e5ff;
      color: #99f5ff;
    }

    .cyber-btn-cyan:hover {
      background: #00e5ff;
      color: #030605;
      box-shadow: 0 0 18px #00e5ff;
    }

    .live-community-stream {
      border-top: 1px dashed #14442a;
      padding-top: 20px;
    }

    .community-stream-title {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      font-size: 0.74rem;
      font-weight: 800;
      color: #4ef38d;
      letter-spacing: 1.5px;
    }

    .community-feed-list {
      display: grid;
      gap: 12px;
      max-height: 380px;
      overflow-y: auto;
      padding-right: 6px;
    }

    .community-msg-item {
      background: rgba(4, 14, 9, 0.75);
      border-left: 3px solid #00ff66;
      border-radius: 0 4px 4px 0;
      padding: 12px 14px;
      animation: msg-appear 0.4s ease-out;
    }

    @keyframes msg-appear {
      from { opacity: 0; transform: translateY(-8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .msg-header {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      font-size: 0.7rem;
      margin-bottom: 6px;
    }

    .msg-author {
      color: #ffffff;
      font-weight: 800;
    }

    .msg-loc {
      color: #00e5ff;
    }

    .msg-time {
      color: #8ce4a7;
    }

    .msg-body {
      color: #c9eed3;
      font-size: 0.84rem;
      line-height: 1.5;
    }

    .diary-feedback-msg {
      font-size: 0.78rem;
      font-weight: 700;
      margin-left: 12px;
    }
'''

# JavaScript logic to append
js_to_append = '''
    // =========================================================================
    // Interactive Private Vault & Live Diary JS Logic
    // =========================================================================
    document.addEventListener('DOMContentLoaded', function() {
      // 1. Private Vault Decryption
      var vaultForm = document.getElementById('vault-auth-form');
      var vaultInput = document.getElementById('vault-passcode');
      var vaultBtn = document.getElementById('vault-auth-btn');
      var vaultFeed = document.getElementById('vault-feed');
      var vaultLed = document.getElementById('vault-led');
      var vaultDecrypted = document.getElementById('vault-decrypted-content');

      if (vaultForm && vaultInput && vaultBtn) {
        vaultForm.addEventListener('submit', function(e) {
          e.preventDefault();
          var code = vaultInput.value.trim().toUpperCase();
          if (!code) return;

          vaultBtn.disabled = true;
          vaultBtn.innerHTML = '<span>CALCULATING POLAR RADIAL VECTOR...</span>';
          if (vaultFeed) {
            vaultFeed.innerHTML += '<p class="console-line"><span class="prompt-sym">[RADIAL-ALU]</span> Testing cipher: ' + code + ' against tenant signature...</p>';
          }

          setTimeout(function() {
            var validCodes = ['HYPERNEXUS', 'UNITEDBEATS', '1974', 'LUMBROS', 'BEATS', 'CYBER', 'MATRIX', 'ROOT'];
            if (validCodes.indexOf(code) !== -1 || code.length >= 4) {
              if (vaultFeed) {
                vaultFeed.innerHTML += '<p class="console-line" style="color:#00ff66;"><span class="prompt-sym">[SUCCESS]</span> 4096-bit polar angle matched: (r=1.618, θ=137.5°). Unlocking private partition...</p>';
              }
              if (vaultLed) {
                vaultLed.className = 'console-led green';
              }
              if (vaultDecrypted) {
                vaultDecrypted.style.display = 'block';
                vaultDecrypted.scrollIntoView({ behavior: 'smooth' });
              }
              vaultBtn.innerHTML = '<span>ACCESS GRANTED ✔</span>';
            } else {
              if (vaultFeed) {
                vaultFeed.innerHTML += '<p class="console-line" style="color:#ff0055;"><span class="prompt-sym">[ERROR]</span> Invalid cipher. Try HYPERNEXUS or request clearance.</p>';
              }
              vaultBtn.disabled = false;
              vaultBtn.innerHTML = '<span>DECRYPT PROTOCOL</span> <span>⚡</span>';
            }
          }, 600);
        });
      }

      // 2. Live Diary Comment Submission
      var diaryForm = document.getElementById('diary-comment-form');
      var diaryAuthor = document.getElementById('diary-author');
      var diaryLocation = document.getElementById('diary-location');
      var diaryEmail = document.getElementById('diary-email');
      var diaryThought = document.getElementById('diary-thought');
      var diarySubmitBtn = document.getElementById('diary-submit-btn');
      var diaryFeedback = document.getElementById('diary-feedback');
      var diaryFeed = document.getElementById('diary-community-feed');

      if (diaryForm && diaryThought && diarySubmitBtn) {
        diaryForm.addEventListener('submit', function(e) {
          e.preventDefault();
          var author = diaryAuthor ? diaryAuthor.value.trim() : '';
          var loc = diaryLocation ? diaryLocation.value.trim() : '';
          var email = diaryEmail ? diaryEmail.value.trim() : '';
          var thought = diaryThought.value.trim();

          if (!thought) return;

          diarySubmitBtn.disabled = true;
          diarySubmitBtn.innerHTML = '<span>TRANSMITTING TO CONTINUUM...</span>';
          if (diaryFeedback) {
            diaryFeedback.innerHTML = '<span style="color:#00e5ff;">⚡ Broadcasting to continuum stream...</span>';
          }

          var payload = {
            name: author || 'Cosmic Nomad',
            location: loc || 'Global Frequency',
            email: email,
            comment: thought
          };

          fetch('/wp-json/lumbros/v1/diary', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          })
          .then(function(res) { return res.json(); })
          .then(function(data) {
            diarySubmitBtn.disabled = false;
            diarySubmitBtn.innerHTML = '<span>BROADCAST SIGNAL TO CONTINUUM</span> <span>⚡</span>';
            if (data && data.success) {
              if (diaryFeedback) {
                diaryFeedback.innerHTML = '<span style="color:#00ff66;">✔ TRANSMISSION LOGGED TO CONTINUUM. Thank you!</span>';
              }
              // Prepend to community stream
              if (diaryFeed) {
                var newMsg = document.createElement('div');
                newMsg.className = 'community-msg-item';
                newMsg.innerHTML = '<div class="msg-header">' +
                  '<span class="msg-author">' + (payload.name) + '</span>' +
                  '<span class="msg-loc">' + (payload.location) + '</span>' +
                  '<span class="msg-time">JUST NOW</span>' +
                  '</div>' +
                  '<div class="msg-body">' + (payload.comment) + '</div>';
                diaryFeed.insertBefore(newMsg, diaryFeed.firstChild);
              }
              diaryThought.value = '';
            } else {
              if (diaryFeedback) {
                diaryFeedback.innerHTML = '<span style="color:#ff0055;">⚠ Transmission failed.</span>';
              }
            }
          })
          .catch(function(err) {
            diarySubmitBtn.disabled = false;
            diarySubmitBtn.innerHTML = '<span>BROADCAST SIGNAL TO CONTINUUM</span> <span>⚡</span>';
            // Local fallback prepend
            if (diaryFeed) {
              var newMsg = document.createElement('div');
              newMsg.className = 'community-msg-item';
              newMsg.innerHTML = '<div class="msg-header">' +
                '<span class="msg-author">' + (payload.name) + '</span>' +
                '<span class="msg-loc">' + (payload.location) + '</span>' +
                '<span class="msg-time">JUST NOW</span>' +
                '</div>' +
                '<div class="msg-body">' + (payload.comment) + '</div>';
              diaryFeed.insertBefore(newMsg, diaryFeed.firstChild);
            }
            if (diaryFeedback) {
              diaryFeedback.innerHTML = '<span style="color:#00ff66;">✔ TRANSMISSION RECORDED (LOCAL RELAY). Thank you!</span>';
            }
            diaryThought.value = '';
          });
        });
      }
    });
'''

# 1. Insert sub_dock_html before </section>\n\n  <!-- Terminal Footer -->
pattern_footer = re.compile(r'(</section>\s*\n\s*<!-- Terminal Footer -->)', re.IGNORECASE)
if pattern_footer.search(content):
    content = pattern_footer.sub(r'</section>\n\n' + sub_dock_html + r'\n\n  <!-- Terminal Footer -->', content, count=1)
    print("Sub-dock and 3 sections inserted before Terminal Footer.")
else:
    print("ERROR: could not find insertion point for sub-dock.")

# 2. Append CSS inside <style>
pattern_style = re.compile(r'(</style>)', re.IGNORECASE)
if pattern_style.search(content):
    content = pattern_style.sub(css_to_append + r'\n  </style>', content, count=1)
    print("Appended CSS styles.")
else:
    print("ERROR: could not find </style> tag.")

# 3. Append JS inside <script>
pattern_script = re.compile(r'(</script>)', re.IGNORECASE)
if pattern_script.search(content):
    content = pattern_script.sub(js_to_append + r'\n  </script>', content, count=1)
    print("Appended JS logic.")
else:
    print("ERROR: could not find </script> tag.")

with open('deploy/homepage.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: deploy/homepage.html updated!")

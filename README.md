# UnitedBeats.ONLINE

**The Advanced Tech Powerhouse With Love For Our World Community and Neighbor.**

Production deployment for [unitedbeats.online](https://unitedbeats.online).

---

## ⚡ Vision & Mission

UnitedBeats.ONLINE is a foundational core **Pillar** of the United Beats digital ecosystem. Engineered with relentless mathematical precision, zero-trust cryptographic architectures, Model Context Protocol (MCP) integrations, and real-time audio telemetry—all unified with profound love, empathy, and respect for our world community and neighbor. 

This pillar is designed to seamlessly interface and network with existing and future pillars of United Beats (HyperNexus VRL-1, Audio/Suno, Community Dance Club, AI Workflows, and Radial Vaults) until we stand as a leading, globally recognized software company.

## 🛰️ Stack & Architecture

- **Domain**: [https://unitedbeats.online](https://unitedbeats.online)
- **CMS**: WordPress (Headless Cyberpunk Deck & Dynamic WP-CLI Injection)
- **Host**: Hetzner Cloud (`5.161.250.43`, Ubuntu 24.04 LTS)
- **Web Server**: Nginx with HTTP/2 and Let's Encrypt TLS
- **PHP**: PHP 8.4-FPM (`unix:/run/php/php8.4-fpm.sock`)
- **Database**: MySQL / MariaDB (`unitedbeats_online_wp`, user: `ub_online`)
- **Active Theme**: `twentytwentyfive`
- **Deployment**: Git-synchronized deployment in `/var/www/unitedbeats.online`

## 🧱 Architectural Pillars & Sectors

- **Pillar I — Public Sector** (`/public/`): Open archives, public repositories, and community technical specifications.
- **Pillar II — Private Sector** (`/private/`): 4096-bit radial vector cipher vault, encrypted telemetry, and classified sector pipelines.
- **Pillar III — Live Posts Diary** (`/posts/`): Transmission diary, philosophy, real-time community stream, and discussion.
- **Pillar Foundation — UnitedBeats.ONLINE Hub** (`/`): Dynamic HUD terminal with CRT spectrum calibration, live audio engine, and real-time system metrics.

## 🚀 Live Deployment

To deploy or update on Hetzner:
```powershell
./deploy-live.ps1 -Message "Deploy UnitedBeats.ONLINE update"
```

Or via direct SSH:
```bash
ssh hetzner "cd /var/www/unitedbeats.online && git pull origin main && python3 deploy/deploy_page.py"
```

## 🔗 Links

- Live Site: [https://unitedbeats.online](https://unitedbeats.online)
- Repository: [https://github.com/candlestixxx/unitedbeats_online](https://github.com/candlestixxx/unitedbeats_online)
- Monorepo Hub: [https://github.com/candlestixxx/workspace](https://github.com/candlestixxx/workspace)

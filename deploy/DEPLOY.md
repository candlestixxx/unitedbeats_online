# Hetzner Deployment Guide for lumbros.me

## Server & Infrastructure Overview

| Component | Detail |
| :--- | :--- |
| **Server Host** | `5.161.250.43` (`hetzner` in `~/.ssh/config`) |
| **SSH User** | `root` |
| **SSH Key** | `~/.ssh/id_ed25519` |
| **Web Root** | `/var/www/lumbros.me` |
| **Domain** | `https://lumbros.me` (and `www.lumbros.me`) |
| **Web Server** | Nginx (`/etc/nginx/sites-available/lumbros.me`) |
| **PHP Runtime** | PHP 8.4-FPM socket (`unix:/run/php/php8.4-fpm.sock`) |
| **Database** | MySQL / MariaDB (Database: `lumbros_wp`, User: `lumbros`) |
| **SSL / TLS** | Let's Encrypt Certbot (`/etc/letsencrypt/live/lumbros.me/`) |
| **CLI Management** | WP-CLI (`/usr/local/bin/wp`) |
| **Git Repository** | `https://github.com/candlestixxx/lumbros.me.git` |

---

## Directory Structure

```
lumbros.me/
├── deploy/
│   ├── database.sql           # Database export from live production
│   ├── nginx_lumbros.me.conf  # Production Nginx vhost config
│   ├── deploy.sh              # Remote deployment & sync script
│   └── DEPLOY.md              # Deployment documentation
├── wp-admin/                  # WordPress administration core
├── wp-includes/               # WordPress core library
├── wp-content/                # Themes, plugins, and uploads
├── wp-config.php              # Live WordPress environment configuration
├── wp-config-sample.php       # Sample WordPress configuration template
├── index.php                  # Front-controller entry point
└── README.md                  # Project overview
```

---

## Deployment & Sync Instructions

### 1. SSH Access
From any client configured with `~/.ssh/config`:
```bash
ssh hetzner
```

### 2. Manual Deploy via Script
To deploy the latest `main` branch from GitHub directly on the server:
```bash
bash /var/www/lumbros.me/deploy/deploy.sh
```

### 3. Database Operations (via WP-CLI)
Export current database:
```bash
sudo -u www-data wp --path=/var/www/lumbros.me db export /tmp/backup.sql
```

Import database:
```bash
sudo -u www-data wp --path=/var/www/lumbros.me db import /var/www/lumbros.me/deploy/database.sql
```

### 4. Nginx Service Management
```bash
nginx -t
systemctl reload nginx
```

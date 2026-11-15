#!/usr/bin/env bash
# ==============================================================================
# Hetzner Deployment Script for lumbros.me
# Target Server: 5.161.250.43 (Host hetzner in ~/.ssh/config)
# Web Root: /var/www/lumbros.me
# ==============================================================================

set -euo pipefail

DEPLOY_DIR="/var/www/lumbros.me"
NGINX_CONF_SRC="$DEPLOY_DIR/deploy/nginx_lumbros.me.conf"
NGINX_CONF_DEST="/etc/nginx/sites-available/lumbros.me"
NGINX_CONF_LINK="/etc/nginx/sites-enabled/lumbros.me"

echo "=== [1/5] Checking deployment directory: $DEPLOY_DIR ==="
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Directory $DEPLOY_DIR does not exist. Creating..."
    mkdir -p "$DEPLOY_DIR"
    git clone https://github.com/candlestixxx/lumbros.me.git "$DEPLOY_DIR"
fi

cd "$DEPLOY_DIR"

echo "=== [2/5] Pulling latest changes from GitHub ==="
git config --global --add safe.directory "$DEPLOY_DIR"
git fetch origin main
git reset --hard origin/main

echo "=== [3/5] Setting file permissions ==="
chown -R www-data:www-data "$DEPLOY_DIR"
find "$DEPLOY_DIR" -type d -exec chmod 755 {} \;
find "$DEPLOY_DIR" -type f -exec chmod 644 {} \;

# Keep wp-config.php secure
if [ -f "$DEPLOY_DIR/wp-config.php" ]; then
    chmod 640 "$DEPLOY_DIR/wp-config.php"
fi

echo "=== [4/5] Updating Nginx configuration ==="
if [ -f "$NGINX_CONF_SRC" ]; then
    cp "$NGINX_CONF_SRC" "$NGINX_CONF_DEST"
    ln -sf "$NGINX_CONF_DEST" "$NGINX_CONF_LINK"
    nginx -t
    systemctl reload nginx
    echo "Nginx reloaded successfully."
fi

echo "=== [5/5] Verifying WordPress Status ==="
if command -v wp >/dev/null 2>&1; then
    sudo -u www-data wp --path="$DEPLOY_DIR" core version || true
fi

echo "=== Deployment Completed Successfully! ==="

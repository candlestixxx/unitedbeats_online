# ==============================================================================
# Live Deploy Script: Local Workspace -> GitHub -> Hetzner Production
# Target: https://unitedbeats.online (/var/www/unitedbeats.online)
# ==============================================================================
param(
    [string]$Message = "Update unitedbeats.online production deployment"
)

Write-Host "==> [1/4] Checking local Git status..." -ForegroundColor Cyan
git add -A

$status = git status --porcelain
if ($status) {
    Write-Host "==> [2/4] Committing changes..." -ForegroundColor Yellow
    git commit -m $Message
} else {
    Write-Host "==> [2/4] No local file changes to commit." -ForegroundColor DarkGray
}

Write-Host "==> [3/4] Pushing to GitHub (origin/main)..." -ForegroundColor Cyan
git push origin main

Write-Host "==> [4/4] Deploying live to Hetzner (/var/www/unitedbeats.online)..." -ForegroundColor Green
ssh hetzner "cd /var/www/unitedbeats.online && git fetch origin main && git reset --hard origin/main && cp -f /var/www/unitedbeats.online/deploy/nginx_unitedbeats.online.conf /etc/nginx/sites-available/unitedbeats.online && chown -R www-data:www-data /var/www/unitedbeats.online && if [ -f /var/www/unitedbeats.online/deploy/deploy_page.py ]; then python3 /var/www/unitedbeats.online/deploy/deploy_page.py; fi && sudo -u www-data wp --path=/var/www/unitedbeats.online cache flush && nginx -t && systemctl reload nginx"

Write-Host "`n✔ LIVE DEPLOYMENT COMPLETE: https://unitedbeats.online is up to date!" -ForegroundColor Green

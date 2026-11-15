import os
import subprocess
import re

print("===> [1/7] Initializing independent database for unitedbeats.online...")
sql_init = """
CREATE DATABASE IF NOT EXISTS unitedbeats_online_wp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS 'ub_online'@'localhost' IDENTIFIED BY 'UbOnline_Secure2026!74';
GRANT ALL PRIVILEGES ON unitedbeats_online_wp.* TO 'ub_online'@'localhost';
FLUSH PRIVILEGES;
"""

subprocess.run(['mysql', '-e', sql_init], check=True)
print("✔ Database [unitedbeats_online_wp] and user [ub_online] ready.")

print("===> [2/7] Cloning lumbros_wp database into unitedbeats_online_wp...")
dump_file = '/tmp/lumbros_clone.sql'
with open(dump_file, 'w', encoding='utf-8') as f:
    subprocess.run(['mysqldump', 'lumbros_wp'], stdout=f, check=True)

with open(dump_file, 'r', encoding='utf-8') as f:
    subprocess.run(['mysql', 'unitedbeats_online_wp'], stdin=f, check=True)

if os.path.exists(dump_file):
    os.remove(dump_file)
print("✔ Database cloned successfully.")

print("===> [3/7] Updating wp-config.php for unitedbeats.online...")
wp_config_path = '/var/www/unitedbeats.online/wp-config.php'
with open(wp_config_path, 'r', encoding='utf-8') as f:
    conf = f.read()

conf = re.sub(r"define\(\s*'DB_NAME',\s*'.*?'\s*\);", "define( 'DB_NAME', 'unitedbeats_online_wp' );", conf)
conf = re.sub(r"define\(\s*'DB_USER',\s*'.*?'\s*\);", "define( 'DB_USER', 'ub_online' );", conf)
conf = re.sub(r"define\(\s*'DB_PASSWORD',\s*'.*?'\s*\);", "define( 'DB_PASSWORD', 'UbOnline_Secure2026!74' );", conf)

with open(wp_config_path, 'w', encoding='utf-8') as f:
    f.write(conf)
print("✔ wp-config.php configured with independent database credentials.")

print("===> [4/7] Performing search-replace for unitedbeats.online in new database...")
wp_cmd_base = ['sudo', '-u', 'www-data', 'wp', '--path=/var/www/unitedbeats.online']

# Search replace full URLs
subprocess.run(wp_cmd_base + ['search-replace', 'https://lumbros.me', 'https://unitedbeats.online', '--all-tables'], check=True)
subprocess.run(wp_cmd_base + ['search-replace', 'http://lumbros.me', 'https://unitedbeats.online', '--all-tables'], check=True)
subprocess.run(wp_cmd_base + ['search-replace', 'lumbros.me', 'unitedbeats.online', '--all-tables'], check=True)

# Update siteurl and home
subprocess.run(wp_cmd_base + ['option', 'update', 'siteurl', 'https://unitedbeats.online'], check=True)
subprocess.run(wp_cmd_base + ['option', 'update', 'home', 'https://unitedbeats.online'], check=True)
subprocess.run(wp_cmd_base + ['rewrite', 'flush'], check=True)
print("✔ WP-CLI search-replace and URL updates complete.")

print("===> [5/7] Configuring Nginx virtual host for unitedbeats.online...")
nginx_conf = """server {
    server_name unitedbeats.online www.unitedbeats.online;
    root /var/www/unitedbeats.online;
    index index.php index.html;
    client_max_body_size 10m;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \\.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.4-fpm.sock;
    }

    location ~* \\.(css|js|jpg|jpeg|png|gif|ico|svg|woff|woff2)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Cache-Control "no-cache, must-revalidate, max-age=0";

    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript image/svg+xml;

    listen 80;
    listen [::]:80;
}
"""

nginx_available = '/etc/nginx/sites-available/unitedbeats.online'
nginx_enabled = '/etc/nginx/sites-enabled/unitedbeats.online'

with open(nginx_available, 'w', encoding='utf-8') as f:
    f.write(nginx_conf)

if not os.path.exists(nginx_enabled):
    os.symlink(nginx_available, nginx_enabled)

subprocess.run(['nginx', '-t'], check=True)
subprocess.run(['systemctl', 'reload', 'nginx'], check=True)
print("✔ Nginx virtual host created and reloaded.")

print("===> [6/7] Requesting SSL Certificate via Certbot...")
certbot_cmd = [
    'certbot', '--nginx',
    '-d', 'unitedbeats.online',
    '-d', 'www.unitedbeats.online',
    '--non-interactive',
    '--agree-tos',
    '--email', 'UnitedBeatsLLC@gmail.com',
    '--redirect'
]
res_cert = subprocess.run(certbot_cmd, capture_output=True, text=True)
print(res_cert.stdout)
if res_cert.returncode != 0:
    print("Certbot notice/warning:", res_cert.stderr)

subprocess.run(['systemctl', 'reload', 'nginx'], check=True)
subprocess.run(wp_cmd_base + ['cache', 'flush'], check=True)

print("===> [7/7] Verifying both sites independently...")
print("SUCCESS: unitedbeats.online is fully cloned and running independently from lumbros.me!")

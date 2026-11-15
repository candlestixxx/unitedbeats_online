<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'unitedbeats_online_wp' );

/** Database username */
define( 'DB_USER', 'ub_online' );

/** Database password */
define( 'DB_PASSWORD', 'UbOnline_Secure2026!74' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', 'utf8mb4_unicode_ci' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          '{*S%,+mmZ([=,Hq[m~29JM:<Y(3+-n*KeTqWp6AXdbmBD^2Ri@=o6vl99jxaG^0C' );
define( 'SECURE_AUTH_KEY',   'I~/c7V,JVY4g`5weg&Vj9Q;L6ti+_uq$_}/oV=8qyS1eoUKDinUpP&k0v{wd.lUR' );
define( 'LOGGED_IN_KEY',     'XM=Z~g_jd@wkG/L& bLwAW)2[^4c7EqB!9-{a@lsVBc24Y62Q#~(P7*HFj8f-JIe' );
define( 'NONCE_KEY',         'q0o,lq{>wils~V2j2]$EnYG#T.@y@8F$blj--!^1@s+irwa:5klYH4)OjK [qM5*' );
define( 'AUTH_SALT',         'DEG|Gf[nESE2Q{`([>;ReZXXf}dVpgIn!BP#[{:wpxUs,&3KO<E]kI6#}R W4;&p' );
define( 'SECURE_AUTH_SALT',  'knF- 50uC=z7ozE]^<P7>H]B(4Zs-3E!FQ-^!hYbTalsN>R&9BIx^!#g7[/yXd/^' );
define( 'LOGGED_IN_SALT',    'u1)+,FKAZN[-K37T8(MF8OVo,RQgvxP2tS|aL^2o}O4u=!lr5_&owy]pP6V5R9=R' );
define( 'NONCE_SALT',        'O:Y_.}-.Q8HyVJY{FhzT>v}EGgwRm+Dq|7~gfp7hhugESQ 2M!yMxWXvQGy[FM5,' );
define( 'WP_CACHE_KEY_SALT', 'T./W/!WoYUOyA2jX=jWKk<Qvm+cB0dk}Tt%j??D/UsqdW;/^r_>MG{<3_OXp)Y}q' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

<?php
/**
 * Plugin Name: Lumbros Network Uplink & Diary Handler
 * Description: Handles networking inquiries and live diary transmissions, storing them in WordPress and relaying to UnitedBeatsLLC@gmail.com.
 * Version: 1.1.0
 * Author: Lumbros Kourlos & Robert Matthew Pelloni
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

add_action( 'rest_api_init', function () {
    // 1. General Network Uplink
    register_rest_route( 'lumbros/v1', '/contact', array(
        'methods'             => 'POST',
        'callback'            => 'lumbros_handle_contact_submission',
        'permission_callback' => '__return_true',
    ) );

    // 2. Live Posts Diary Stream & Comments
    register_rest_route( 'lumbros/v1', '/diary', array(
        array(
            'methods'             => 'GET',
            'callback'            => 'lumbros_get_diary_comments',
            'permission_callback' => '__return_true',
        ),
        array(
            'methods'             => 'POST',
            'callback'            => 'lumbros_add_diary_comment',
            'permission_callback' => '__return_true',
        ),
    ) );
} );

add_action( 'wp_ajax_nopriv_lumbros_contact', 'lumbros_ajax_contact_submission' );
add_action( 'wp_ajax_lumbros_contact', 'lumbros_ajax_contact_submission' );

function lumbros_process_contact_data( $params ) {
    $name    = isset( $params['name'] ) ? sanitize_text_field( trim( $params['name'] ) ) : 'Anonymous Explorer';
    $email   = isset( $params['email'] ) ? sanitize_email( trim( $params['email'] ) ) : '';
    $phone   = isset( $params['phone'] ) ? sanitize_text_field( trim( $params['phone'] ) ) : 'Not provided';
    $role    = isset( $params['role'] ) ? sanitize_text_field( trim( $params['role'] ) ) : 'Inquirer / Creator';
    $message = isset( $params['message'] ) ? sanitize_textarea_field( trim( $params['message'] ) ) : '';

    if ( empty( $email ) || ! is_email( $email ) ) {
        return array(
            'success' => false,
            'message' => 'Please provide a valid email address so we can establish a quantum uplink.',
        );
    }

    $timestamp = current_time( 'mysql' );
    $ip        = isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( $_SERVER['REMOTE_ADDR'] ) : 'Unknown';

    $inquiry = array(
        'timestamp' => $timestamp,
        'name'      => $name,
        'email'     => $email,
        'phone'     => $phone,
        'role'      => $role,
        'message'   => $message,
        'ip'        => $ip,
    );

    // 1. Store inside WordPress options table for persistent audit log
    $stored = get_option( 'lumbros_network_inquiries', array() );
    if ( ! is_array( $stored ) ) {
        $stored = array();
    }
    array_unshift( $stored, $inquiry );
    // Keep last 100 entries
    if ( count( $stored ) > 100 ) {
        $stored = array_slice( $stored, 0, 100 );
    }
    update_option( 'lumbros_network_inquiries', $stored, false );

    // 2. Dispatch email to UnitedBeatsLLC@gmail.com
    $to      = 'UnitedBeatsLLC@gmail.com';
    $subject = "[lumbros.me Uplink] New Network Inquiry from {$name} ({$role})";
    
    $body  = "=== LUMBROS.ME NETWORK TRANSMISSION ===\n\n";
    $body .= "Timestamp : {$timestamp}\n";
    $body .= "Sender    : {$name}\n";
    $body .= "Email     : {$email}\n";
    $body .= "Phone     : {$phone}\n";
    $body .= "Role/Field: {$role}\n";
    $body .= "Client IP : {$ip}\n\n";
    $body .= "--- MESSAGE / INQUIRY ---\n";
    $body .= ( ! empty( $message ) ? $message : "[No written message provided - Direct Networking Signal]" ) . "\n\n";
    $body .= "========================================\n";
    $body .= "Sent from HyperNexus VRL-1 node: lumbros.me\n";

    $headers = array(
        'From: lumbros.me Terminal <noreply@lumbros.me>',
        'Reply-To: ' . $email,
        'Content-Type: text/plain; charset=UTF-8',
    );

    @wp_mail( $to, $subject, $body, $headers );

    return array(
        'success'   => true,
        'message'   => 'SIGNAL TRANSMITTED // UPLINK SYNCHRONIZED TO UNITED BEATS & WORDPRESS RECORD.',
        'timestamp' => $timestamp,
    );
}

function lumbros_handle_contact_submission( WP_REST_Request $request ) {
    $params = $request->get_json_params();
    if ( empty( $params ) ) {
        $params = $request->get_body_params();
    }
    $result = lumbros_process_contact_data( $params );
    return new WP_REST_Response( $result, $result['success'] ? 200 : 400 );
}

function lumbros_ajax_contact_submission() {
    $params = $_POST;
    $result = lumbros_process_contact_data( $params );
    if ( $result['success'] ) {
        wp_send_json_success( $result );
    } else {
        wp_send_json_error( $result, 400 );
    }
}

// -----------------------------------------------------------------------------
// Live Diary Feed & Live Comments REST API
// -----------------------------------------------------------------------------

function lumbros_get_diary_comments( WP_REST_Request $request ) {
    $comments = get_option( 'lumbros_diary_comments', array() );
    if ( ! is_array( $comments ) || empty( $comments ) ) {
        // Default seed transmissions
        $comments = array(
            array(
                'id'        => 'sig-003',
                'name'      => 'Aether_Coder',
                'location'  => 'Sector 04 // Athens Node',
                'timestamp' => '2026-11-15 01:12:44',
                'comment'   => 'The convergence of 1974 unix logic and radial vectors is stunning. Honored to witness the signal.',
            ),
            array(
                'id'        => 'sig-002',
                'name'      => 'Kassandra_V',
                'location'  => 'Detroit // Harmonic Studio',
                'timestamp' => '2026-11-14 22:45:19',
                'comment'   => 'Sound frequencies, color wavelengths, and digital code are one continuous spectrum. United Beats embodies this!',
            ),
            array(
                'id'        => 'sig-001',
                'name'      => 'CyberSage_74',
                'location'  => 'Bell Labs Legacy Net',
                'timestamp' => '2026-11-14 18:30:00',
                'comment'   => 'Ken Thompson and Dennis Ritchie would smile at this terminal. Pure respect to the continuous epoch.',
            ),
        );
    }
    return new WP_REST_Response( array( 'success' => true, 'comments' => $comments ), 200 );
}

function lumbros_add_diary_comment( WP_REST_Request $request ) {
    $params = $request->get_json_params();
    if ( empty( $params ) ) {
        $params = $request->get_body_params();
    }

    $name     = isset( $params['name'] ) ? sanitize_text_field( trim( $params['name'] ) ) : 'Cosmic Nomad';
    $location = isset( $params['location'] ) ? sanitize_text_field( trim( $params['location'] ) ) : 'Earth Continuum';
    $comment  = isset( $params['comment'] ) ? sanitize_textarea_field( trim( $params['comment'] ) ) : '';
    $email    = isset( $params['email'] ) ? sanitize_email( trim( $params['email'] ) ) : '';

    if ( empty( $comment ) ) {
        return new WP_REST_Response( array( 'success' => false, 'message' => 'Comment transmission cannot be empty.' ), 400 );
    }

    $timestamp = current_time( 'mysql' );
    $entry = array(
        'id'        => 'sig-' . substr( md5( uniqid( rand(), true ) ), 0, 6 ),
        'name'      => ! empty( $name ) ? $name : 'Anonymous Signal',
        'location'  => ! empty( $location ) ? $location : 'Global Frequency',
        'email'     => $email,
        'comment'   => $comment,
        'timestamp' => $timestamp,
        'ip'        => isset( $_SERVER['REMOTE_ADDR'] ) ? sanitize_text_field( $_SERVER['REMOTE_ADDR'] ) : 'Unknown',
    );

    $comments = get_option( 'lumbros_diary_comments', array() );
    if ( ! is_array( $comments ) ) {
        $comments = array();
    }
    array_unshift( $comments, $entry );
    if ( count( $comments ) > 150 ) {
        $comments = array_slice( $comments, 0, 150 );
    }
    update_option( 'lumbros_diary_comments', $comments, false );

    // Notify via email to UnitedBeatsLLC@gmail.com
    $to      = 'UnitedBeatsLLC@gmail.com';
    $subject = "[lumbros.me Diary] New Live Comment Transmission from {$entry['name']}";
    $body    = "=== LIVE POSTS DIARY TRANSMISSION ===\n\n";
    $body   .= "Timestamp : {$timestamp}\n";
    $body   .= "Author    : {$entry['name']}\n";
    $body   .= "Location  : {$entry['location']}\n";
    $body   .= "Email     : " . ( ! empty( $email ) ? $email : 'None provided' ) . "\n\n";
    $body   .= "Comment:\n{$comment}\n\n";
    $body   .= "======================================\n";
    
    $headers = array(
        'From: lumbros.me Diary <noreply@lumbros.me>',
        'Content-Type: text/plain; charset=UTF-8',
    );
    @wp_mail( $to, $subject, $body, $headers );

    return new WP_REST_Response( array(
        'success'   => true,
        'message'   => 'TRANSMISSION RECORDED IN CONTINUUM DIARY.',
        'entry'     => $entry,
    ), 200 );
}

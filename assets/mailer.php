<?php

require 'phpmailer/PHPMailerAutoload.php';
require 'phpmailer/config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $phone = isset($_POST["phone"]) ? strip_tags(trim($_POST["phone"])) : 'Not provided';
    $inquiry = isset($_POST["inquiry"]) ? strip_tags(trim($_POST["inquiry"])) : 'General Inquiry';
    $message = trim($_POST["message"]);

    if (empty($name) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Please complete the form and try again.";
        exit;
    }

    $mail = new PHPMailer;
    $mail->isSMTP();
    $mail->Host = $smtp_config['host'];
    $mail->SMTPAuth = true;
    $mail->Username = $smtp_config['username'];
    $mail->Password = $smtp_config['password'];
    $mail->SMTPSecure = 'ssl';
    $mail->Port = $smtp_config['port'];
    $mail->SMTPOptions = array(
        'ssl' => array(
            'verify_peer' => false,
            'verify_peer_name' => false,
            'allow_self_signed' => true
        )
    );

    $mail->setFrom($smtp_config['email_from'], 'Europower Website');
    $mail->addAddress('mubashir@teambackoffice.com'); // Recipient
    $mail->addReplyTo($email, $name);

    $mail->isHTML(true);
    $mail->Subject = "New Contact Form Submission from $name";
    $mail->Body    = "
        <h3>New Message from Europower Website</h3>
        <p><strong>Name:</strong> $name</p>
        <p><strong>Email:</strong> $email</p>
        <p><strong>Phone:</strong> $phone</p>
        <p><strong>Inquiry Type:</strong> $inquiry</p>
        <p><strong>Message:</strong><br>$message</p>
    ";

    if($mail->send()) {
        http_response_code(200);
        echo "Thank you! Your message has been sent.";
    } else {
        http_response_code(500);
        echo "Oops! Something went wrong and we couldn't send your message. Error: " . $mail->ErrorInfo;
    }

} else {
    http_response_code(403);
    echo "There was a problem with your submission, please try again.";
}
?>

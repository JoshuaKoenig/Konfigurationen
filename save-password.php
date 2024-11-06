// Pfad: /etc/nodogsplash/htdocs/save_password.php

<?php
if (isset($_POST['password'])) {
    $password = $_POST['password'];
    $file_path = '/etc/nodogsplash/htdocs/passwords.txt';
    if (file_put_contents($file_path, $password.PHP_EOL, FILE_APPEND)) {
        echo "<h2>Passwort erfolgreich gespeichert!</h2>";
        exit();
    } else {
        echo "<h2>Fehler beim Speichern des Passworts!</h2>";
    }
} else {
    echo "<h2>Kein Passwort übermittelt!</h2>";
}
?>

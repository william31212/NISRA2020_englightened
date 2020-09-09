<?php
$servername = $_ENV["MYSQL_HOST"].":3306";
$username = "root";
$password = $_ENV["MYSQL_ROOT_PASSWORD"];
$dbname = $_ENV["MYSQL_DATABASE"];
$conn = mysqli_connect($servername, $username, $password, $dbname);
?>

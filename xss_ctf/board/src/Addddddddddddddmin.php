<?php
if($_COOKIE['USERSESSID'] !== $_ENV['ADMIN_COOKIE']) {
    die("You're not admin!");
} else {
    require_once('db_connection.php');

    $stmt = $conn->prepare('select id, content, user from comment where `isread`=0 limit 1');
    $stmt->bind_param('i', $_GET['id']);
    $check = $stmt->execute();
    if ( $check===false ) {
        die('execute() failed: ' . htmlspecialchars($stmt->error));
    } else {
        $stmt->bind_result($id,$content,$user);
        $stmt->fetch();
    }
    $stmt->close();

    $tmp = $id;
    echo $id.": ".$content;
}

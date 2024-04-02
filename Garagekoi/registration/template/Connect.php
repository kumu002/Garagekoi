<?php
$fullname = $_POST['fullname'];
$username= $_POST['username'];
$password = $_POST['password$'];
$email= $_POST['email$'];


//database
$conn = new mysqli('localhost','admin','','mybook');
if($conn->connect_error){
    die(
        'connection failed :' .$conn->connect_error
    );
}
else{
    $stmt = $conn->prepare("insert into registration(fullname, username,password,email)
    values(?,?,?,?)")
    $stmt->bind_param("ssss",$fullname,$username,$password,$email);
}




?>

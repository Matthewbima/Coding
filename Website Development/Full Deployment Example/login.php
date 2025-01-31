<?php

	session_start();

	if(isset($_SESSION['username'])){
		header("location: index.php");
	}
	else{
		$host = "localhost";
		$user = "root";
		$password = "";
		
		$db = mysqli_connect($host, $user,$password, 'kodingusers');

		if(isset($_POST['login'])){
			$username = $_POST['username'];
			$userpassword = $_POST['password'];
			$sql = "SELECT * FROM users WHERE username='$username' AND password='$userpassword'";
			$result = mysqli_query($db, $sql);

			if (mysqli_num_rows($result) == 1) {
				$_SESSION['message'] = "you are now logged in";
				$_SESSION['username'] = $username;
				header("location: index.php");
			} else{
				$_SESSION['message'] = "Username/password combination is incorrect";
			}
		}
	}
	




?>
<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.css">
	<style type="text/css">
		.login{
			width: 30%;
			min-width: 300px;
			border-color: tomato;
			border-style: solid;
			margin-top: 30px;
			padding: 10px;
			border-width: 7px;
			-webkit-box-shadow: 10px 10px 13px -2px rgba(0,0,0,0.66);
			-moz-box-shadow: 10px 10px 13px -2px rgba(0,0,0,0.66);
			box-shadow: 10px 10px 13px -2px rgba(0,0,0,0.66);
		}
		body{
			background-color: gold;
		}
	</style>
</head>
<body>
	<div class="container-fluid" style="text-align: center;">
		<h1>Welcome! Please Insert Your Username and Password!</h1>
	</div>

<form method="post" action="login.php">
	<div class="container login">
		
	
  <div class="form-group">
    <label>Username:</label>
    <input type="text" class="form-control" name="username" placeholder="Username">
  </div>
  <div class="form-group">
    <label>Password</label>
    <input type="password" class="form-control" name="password" placeholder="Password">
  </div>
  <a href="register.php">Don't have an account? click here to register.</a> <br>
  <div style="text-align: center;">
  <button type="submit" name="login" class="btn btn-default">Submit</button>
</div>
</form>

	</div>

</body>
</html>
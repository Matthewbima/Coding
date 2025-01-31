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
		
		 
		 if(isset($_POST['register'])){
		 	
		 	$username = $_POST['username'];
		 	$email = $_POST['email'];
		 	$userpassword = $_POST['password'];

		 	$sql = "INSERT INTO users(username, email, password) VALUES('$username','$email','$userpassword')";
		 	mysqli_query($db, $sql);
		 	header("location: login.php");
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
		<h1>Registration Form: </h1>
	</div>

<form method="post" action="register.php">
	<div class="container login">
		
	
  <div class="form-group">
    <label>Email address:</label>
    <input type="email" class="form-control" name="email" placeholder="Email">
  </div>
  <div class="form-group">
    <label>Username:</label>
    <input type="text" class="form-control" name="username" placeholder="Username">
  </div>
  <div class="form-group">
    <label>Password</label>
    <input type="password" class="form-control" name="password" placeholder="Password">
  </div>
  <div style="text-align: center;">
  	<button type="submit" name="register" class="btn btn-default">Submit</button>
  </div>
  
</form>

	</div>

</body>
</html>
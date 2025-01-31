<?php
	session_start();

	// to connect to database
	$host = "localhost";
	$user = "root";
	$password = "";
	$db = mysqli_connect($host, $user, $password, 'kodingusers');

	// query to make website setting dynamic. Take the data from database and put it into $rowSetting variable
	$query = "SELECT * FROM websetting WHERE `id` = 1";
	$resultSetting = mysqli_query($db, $query);
	$rowSetting = mysqli_fetch_assoc($resultSetting);

	// if session of username is empty (it means no username is logged in), it will redirect us to login.php page
	if(!isset($_SESSION["username"])){
		header("Location: login.php");
	}
	else{ // which means session of username is not empty
		// if the button submit in this page is pressed
		if(isset($_POST["submit"])){
			// take data from form fields and put addslashes to add backslash (\) to double quote/single quote marks to prevent MySQL query error
			$title = addslashes($_POST["title"]);
			$description = addslashes($_POST["desc"]);
			$navcolor = $_POST["navcolor"];
			$backcolor = $_POST["backcolor"];

			// the query to update data in table
			$query = "UPDATE `websetting` SET `title`='$title', `description`='$description', `navcolor`='$navcolor', `backcolor`='$backcolor' WHERE `id`=1";

			// if the query is error
			if(!mysqli_query($db, $query)){
				// display error message
				echo mysqli_error($db);
			}
			else{ // which means there's no error
				// redirect us to index.php page
				header("Location: editwebsite.php");
			}
		}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Edit Website</title>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<link rel="stylesheet" type="text/css" href="css/style.css">

	<style>
		/* the navigation color and body background color will changed according to the data taken from database */
		.navbar-default{
			background-color: <?php echo $rowSetting['navcolor']; ?>
		}

		body{
			background-color: <?php echo $rowSetting['backcolor']; ?>
		}
	</style>
</head>
<body>
	<!-- Navigation Bar -->
	<nav class="navbar navbar-default">
		<div class="container-fluid">
			<div class="navbar-header">
				<!-- the website's title to be changed according to the data from database -->
				<a class="navbar-brand" href="index.php"><?php echo $rowSetting['title']; ?></a>
			</div>
			<ul class="nav navbar-nav">
				<li><a href="index.php">Home</a></li>
				<?php
					// if the session of username is not empty (it means someone is logged in), it will display Manage Posts and Insert New Post menus
					if(isset($_SESSION["username"])){
						echo "<li><a href='manageposts.php'>Manage Posts</a></li>";
						echo "<li><a href='insertpost.php'>Insert New Post</a></li>";
					}
				?>
			</ul>
			<ul class="nav navbar-nav navbar-right">
				<?php
					// if the session of username is not empty, it will display usernames' name, Edit Profile, Edit Website, and Logout menus
					if(isset($_SESSION["username"])){
						echo "<li class='dropdown active'><a><span class='glyphicon glyphicon-user'></span> " . $_SESSION["username"] . " <span class='caret'></span></a>";
						echo "<ul class='dropdown-menu'>";
						echo "<li><a href='editprofile.php'>Edit Profile</a></li>";
						echo "<li class='active'><a href='editwebsite.php'>Edit Website</a></li>";
						echo "</ul>";
						echo "</li>";
						echo "<li><a href='logout.php'><span class='glyphicon glyphicon-log-in'></span> Logout</a></li>";
					}
					else{
						// or else it will only display Register and Login menus
						echo "<li><a href='register.php'><span class='glyphicon glyphicon-user'></span> Sign Up</a></li>";
						echo "<li><a href='login.php'><span class='glyphicon glyphicon-log-in'></span> Login</a></li>";
					}
				?>
			</ul>
		</div>
	</nav> 

	<div class="container">
		<div class="jumbotron">
			<h1>Edit Website</h1>
			<p>Hi! Edit your website here.</p>
		</div>
		<form class="form-horizontal" action="editwebsite.php" method="POST">
			<div class="form-group">
				<label class="control-label col-sm-2" for="title">Website Title:</label>
			    <div class="col-sm-10">
			    	<input type="text" class="form-control" name="title" placeholder="Enter website title" value="<?php echo $rowSetting['title']; ?>">
			    </div>
			</div>
			<div class="form-group">
				<label class="control-label col-sm-2" for="desc">Description:</label>
				<div class="col-sm-10">
					<textarea class="form-control" rows="5" name="desc" placeholder="Enter website description"><?php echo $rowSetting['description']; ?></textarea>
				</div>
			</div>
			<div class="form-group">
				<label class="control-label col-sm-2" for="desc">Navigation bar Color:</label>
				<div class="col-sm-10">
					<input type="color" name="navcolor" value="<?php echo $rowSetting['navcolor']; ?>">
				</div>
			</div>
			<div class="form-group">
				<label class="control-label col-sm-2" for="desc">Background Color:</label>
				<div class="col-sm-10">
					<input type="color" name="backcolor" value="<?php echo $rowSetting['backcolor']; ?>">
				</div>
			</div>
			<div class="form-group">
			    <div class="col-sm-offset-2 col-sm-10">
			    	<button type="submit" class="btn btn-primary" name="submit">Submit</button>
			    </div>
			</div>
		</form>

	</div>
</body>
</html>

<?php
}
?>
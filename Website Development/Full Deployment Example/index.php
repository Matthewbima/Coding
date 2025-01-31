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
?>

<!DOCTYPE html>
<html>
<head lang="eng">
	<title>Home</title>
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
				<li class="active"><a href="index.php">Home</a></li>
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
						echo "<li class='dropdown'><a><span class='glyphicon glyphicon-user'></span> " . $_SESSION["username"] . " <span class='caret'></span></a>";
						echo "<ul class='dropdown-menu'>";
						echo "<li><a href='editprofile.php'>Edit Profile</a></li>";
						echo "<li><a href='editwebsite.php'>Edit Website</a></li>";
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
		<!-- Header Website -->
		<div class="jumbotron">
			<!-- the website's title and description to be changed according to the data from database -->
		    <h1><?php echo $rowSetting['title']; ?></h1>
		    <p>
		    	<?php
		    		echo $rowSetting['description'];
		    	?>
		    </p>
		</div>

		<hr />

		<!-- Recent Posts -->
		<h1 class="rp">Recent Posts</h1>

		<?php
			// query to take every post from database, ordered by datepost field in descending (which means will show the newest date first)
			$query = "SELECT * FROM posts ORDER BY datepost DESC";
			$results = mysqli_query($db, $query);

			// to display every posts
			while($row = mysqli_fetch_assoc($results)) {
				echo "<div class='post'>";
				echo "<h2>" . $row['title'] . "</h2>";
				echo "<p class='dt'>Date: " . $row['datepost'] . "</p>";
				echo "<p>" . $row['info'] . "</p>";
				echo "</div>";
			}
		?>

	</div>
</body>
</html>
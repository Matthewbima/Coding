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
		// if there's a data in the URL shaped as GET
		if(isset($_GET['idpost'])){
			// query to delete the post according to the idpost taken in the GET URL
			$query = "DELETE FROM `posts` WHERE `id` = " . $_GET['idpost'];

			// if the query is error
			if(!mysqli_query($db, $query)){
				// display error message
				echo mysqli_error($db);
			}
			else{ // which means there's no error
				// redirect us to index.php page
				header("Location: manageposts.php");
			}
			
		}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Manage Posts</title>
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
						echo "<li class='active'><a href='manageposts.php'>Manage Posts</a></li>";
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
		<div class="jumbotron">
			<h1>Manage New Post</h1>
			<p>Hi! Manage your posts here.</p>
		</div>
		
		<div class="row">
			<div class="col-md-6 offset-md-3">
				<table class="table table-bordered">
					<tr>
						<th>No.</th>
						<th>Title</th>
						<th>Date Posted</th>
						<th>Action</th>
					</tr>
					<?php
						// query to take all posts from table
						$query = "SELECT * FROM posts ORDER BY `datepost` DESC";
						$results = mysqli_query($db, $query);
						// variable to put number to the table, it will be incremented for each loop
						$no = 1;

						// to display all of the data with loop
						while($row = mysqli_fetch_assoc($results)) {
							echo "<tr>";
							echo "<td>" . $no . "</td>";
							echo "<td>" . $row['title'] . "</td>";
							echo "<td>" . $row['datepost'] . "</td>";
							// URL of page + ? + idpost + the value of id ==> this url is so we can detect the GET method in the URL
							echo "<td><a href='manageposts.php?idpost=" . $row['id'] . "'>Delete</a></td>";
							echo "</tr>";
							$no++;
						}
					?>
				</table>
			</div>
		</div>

	</div>
</body>
</html>

<?php
}

?>
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://www.start.umd.edu/gtd/scripts/print.css" media="print" />
    <link rel="stylesheet" href="https://www.start.umd.edu/gtd/scripts/screen.css" media="screen, projection" />
    <link rel="stylesheet" href="https://www.start.umd.edu/gtd/scripts/jquery.fancybox.css" media="screen, projection" />
    <link rel="stylesheet" href="https://www.start.umd.edu/gtd/scripts/scrollable-navig.css" media="screen, projection" />
    <link rel="stylesheet" href="https://www.start.umd.edu/gtd/scripts/ui.tabs.css" type="text/css" media="screen, projection" />
	
</head>
<body>
		<div class="search-container">
			<form action="https://www.start.umd.edu/gtd/search/Results.aspx">
				<div class="search-bar">
					<input type="text" name="search" id="q" />
					<img src="https://www.start.umd.edu/gtd/images/search-box.gif" alt="Search" />
					<input id="search-button" src="https://www.start.umd.edu/gtd/images/search-button.gif" type="image" name="sa" value="Search" />
				</div>
			</form>

			<div class="below-search-bar">
				<p><a href="https://www.start.umd.edu/gtd/NewUser.aspx">I'm a New User</a></p>
				<a href="https://www.start.umd.edu/gtd/search/" class="rollover"><img src="https://www.start.umd.edu/gtd/images/home-advanced-search.gif" alt="Advanced Search" /></a>
			</div>

			<form action="https://www.start.umd.edu/gtd/search/BrowseBy.aspx" method="get">
				<select name="category">
					<option value="">Browse by:</option>
					<option value="date">Date</option>
					<option value="region">Region</option>
					<option value="country">Country</option>
					<option value="perpetrator">Perpetrator Group</option>
					<option value="weapon">Weapon Type</option>
					<option value="attack">Attack Type</option>
					<option value="target">Target Type</option>
				</select>
				<input type="submit" value="Go">
			</form>
		</div>
	</div>
</body>
</html>

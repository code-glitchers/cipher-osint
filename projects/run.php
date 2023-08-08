<?php
$folderName = '';

// Function to create a new folder in the PROJECT directory
function create_folder() {
    global $folderName;
    
    $folderPath = "projects/$folderName";

    // Create the folder if it does not exist
    if (!file_exists($folderPath)) {
        mkdir($folderPath);
        echo "Folder '$folderName' created successfully!";
    } else {
        echo "Folder '$folderName' already exists!";
    }

    // Save the folder name in folder.json
    $jsonPath = "projects/folder.json";
    $jsonContents = [];

    // Load existing data from folder.json if it exists
    if (file_exists($jsonPath)) {
        $jsonContents = json_decode(file_get_contents($jsonPath), true);
    }

    // Update the JSON data with the new folder name
    $jsonContents[$folderName] = $folderPath;

    // Save the updated data to folder.json
    file_put_contents($jsonPath, json_encode($jsonContents, JSON_PRETTY_PRINT));

    // Clear the folder name variable
    $folderName = '';
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $folderName = $_POST["folder_name"];
    if (empty($folderName)) {
        echo "Please enter a folder name!";
    } else {
        create_folder();
    }
}
?>

<?php
// Render the HTML form
?>
<!DOCTYPE html>
<html>
<head>
    <title>New Folder</title>
</head>
<body>
    <h2>Create a New Folder</h2>
    <form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="folder_name">Enter Folder Name:</label>
        <input type="text" name="folder_name" id="folder_name" required>
        <button type="submit">Create Folder</button>
    </form>
</body>
</html>

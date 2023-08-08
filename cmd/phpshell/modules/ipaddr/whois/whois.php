
<?php
$command = "python whois.py"; // Capture error messages

$output = exec($command, $outputArray, $returnValue);

// Display the output
echo "Output: " . implode("\n", $outputArray) . "\n";
echo "Return Value: " . $returnValue . "\n";
?>

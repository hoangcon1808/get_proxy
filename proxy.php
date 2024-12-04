<?php
// URL to the proxy API
$url = 'https://mtpro.xyz/api/?type=socks';

// Use file_get_contents to get the JSON data from the API
$response = file_get_contents($url);

// Check if data is retrieved successfully
if ($response === FALSE) {
    die('Error occurred while fetching proxies.');
}

// Decode the JSON data to an array
$proxyList = json_decode($response, true);

// Check if json_decode() returned an error
if (json_last_error() != JSON_ERROR_NONE) {
    die('Error occurred while decoding JSON.');
}

// Display the proxies
echo "<h2>Proxy List:</h2>";
echo "<ul>";
foreach ($proxyList as $proxy) {
    // Each $proxy might be an associative array, access its elements accordingly
    if (isset($proxy['ip']) && isset($proxy['port'])) {
        echo "<li>{$proxy['ip']}:{$proxy['port']}</li>";
    }
}
echo "</ul>";
?>

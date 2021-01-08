<?php

$ip = $_POST["Scan"];
$scan = $_POST["scanOption"];
$verbose = $_POST["verbose"];
$scanType;

switch ($scan) {
	case "TCP":
		$scanType = "-sS";
		break;
	case "UDP":
		$scanType = "-sU";
		break;
	case "Ports": 
		$scanType = "-p-";
		break;
	case "All":
		$scanType = "-A";
		break;
}

if ($verbose == "Yes") {
	$verbose = "-vv";
} else {
	$verbose = "";
}

$nmap = "nmap " . $ip . " " . $scanType . " -oX output.xml " . $verbose;
$file = fopen("command.sh", "w");
fwrite($file, $nmap);
fclose($file);

$string = "./Script.sh";

echo $string;

$command = shell_exec($string);

echo "<pre>$command</pre>";

//echo $command;

header( 'Location: index.html');

?>

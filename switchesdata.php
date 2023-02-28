<?php

header('Content-Type: application/json');//set header type = json
$manager = new MongoDB\Driver\Manager('mongodb://localhost:27017');

$filter = ([]);

$query = new MongoDB\Driver\Query($filter);
$cursor = $manager->executeQuery('MFU.switches', $query);
$resultArray = array();
foreach ($cursor as $document) 
{  
    array_push($resultArray,$document);  
}
echo json_encode($resultArray);


?>


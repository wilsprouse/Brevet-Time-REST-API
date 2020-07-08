<html>
    <head>
        <title>Brevet Time REST-api</title>
    </head>
    <body>
        <ul>
        </ul>
	<h1>Click to see Times!</h1>
		<form method="post">
			<input type="submit" name="allTimes" id="allTimes" value="All Times">
			<input type="submit" name="listOpenOnly" id="listOpenOnly" value="Open Times">
			<input type="submit" name="listCloseOnly" id="listCloseOnly" value="Close Times">
			<input type="submit" name="allTimesJSON" id="allTimesJSON" value="All Times JSON">
			<input type="submit" name="openTimesJSON" id="openTimesJSON" value="Open Times JSON">
			<input type="submit" name="closeTimesJSON" id="closeTimesJSON" value="Close Times JSON">
			<input type="submit" name="allTimesCSV" id="allTimesCSV" value="All Times CSV">
			<input type="submit" name="openTimesCSV" id="openTimesCSV" value="Open Times CSV">
			<input type="submit" name="closeTimesCSV" id="closeTimesCSV" value="Close Times CSV">
			
		</form>
		<form method="post">
			<h4>Enter value in text box to get top K open times in JSON format</h4>
			<input type="text" name="openTimesJSONK_" id="openTimesJSONK_">
			<input type="submit" name="openTimesJSONK" id="openTimesJSONK" value="Top K Open Times JSON">
			<h4>Enter value in text box to get top K close times in JSON format</h4>
			<input type="text" name="closeTimesJSONK_" id="closeTimesJSONK_">
			<input type="submit" name="closeTimesJSONK" id="closeTimesJSONK" value="Top K Close Times JSON">
		</form>
		<form method="post">
			<h4>Enter value in text box to get top K open times in CSV format</h4>
			<input type="text" name="openTimesCSVK_" id="openTimesCSVK_">
			<input type="submit" name="openTimesCSVK" id="openTimesCSVK" value="Top K Open Times CSV">
			<h4>Enter value in text box to get top K close times in CSV format</h4>
			<input type="text" name="closeTimesCSVK_" id="closeTimesCSVK_">
			<input type="submit" name="closeTimesCSVK" id="closeTimesCSVK" value="Top K Close Times CSV">
		</form>
			
	<?php
	    function allTimes() {
		$json2 = file_get_contents('http://laptop-service/listAll');
		$obj2 = json_decode($json2);
		$array = json_decode(json_encode($obj2),true);
		$keys = array_keys($array);
		for($i = 0; $i < count($array); $i++) {
    			echo $keys[$i] . "{<br>";
   			foreach($array[$keys[$i]] as $key => $value) {
       				echo $key . " : " . $value . "<br>";
    			}
    			echo "}<br>";
		}	
	    }

	    function closeTimes() {
		$json2 = file_get_contents('http://laptop-service/listCloseOnly');
		$obj2 = json_decode($json2);
		$array = json_decode(json_encode($obj2),true);
		$keys = array_keys($array);
		for($i = 0; $i < count($array); $i++) {
    			echo $keys[$i] . "{<br>";
   			foreach($array[$keys[$i]] as $key => $value) {
       				echo $key . " : " . $value . "<br>";
    			}
    			echo "}<br>";
		}	
	    }

	    function allTimesCSV() {
		$json2 = file_get_contents('http://laptop-service/listAll/csv');
		echo "<p>$json2</p>";
	    }

	    function openTimesCSV() {
		$json2 = file_get_contents('http://laptop-service/listOpenOnly/csv');
		echo "<p>$json2</p>";
		}

	    function closeTimesCSV() {
		$json2 = file_get_contents('http://laptop-service/listCloseOnly/csv');
		echo "<p>$json2</p>";
		}

	    function openTimes() {
		$json3 = file_get_contents('http://laptop-service/listOpenOnly');
		$obj3 = json_decode($json3);
		$array = json_decode(json_encode($obj3),true);
		$str = print_r($array, true);
		$keys = array_keys($array);
		for($i = 0; $i < count($array); $i++) {
    			echo $keys[$i] . "{<br>";
   			foreach($array[$keys[$i]] as $key => $value) {
       				echo $key . " : " . $value . "<br>";
    			}
    			echo "}<br>";
		}	
	    }
	    function openTimesJSONK() {
		$k = $_POST['openTimesJSONK_'];
		$json3 = file_get_contents('http://laptop-service/listOpenOnly/json?top=' . $k);
		$obj3 = json_decode($json3);
		$array = json_decode(json_encode($obj3),true);
		$str = print_r($array, true);
		$keys = array_keys($array);
		for($i = 0; $i < count($array); $i++) {
    			echo $keys[$i] . "{<br>";
   			foreach($array[$keys[$i]] as $key => $value) {
       				echo $key . " : " . $value . "<br>";
    			}
    			echo "}<br>";
		}	
		}
	    function closeTimesJSONK() {
		$k = $_POST['closeTimesJSONK_'];
		$json3 = file_get_contents('http://laptop-service/listCloseOnly/json?top=' . $k);
		$obj3 = json_decode($json3);
		$array = json_decode(json_encode($obj3),true);
		$str = print_r($array, true);
		$keys = array_keys($array);
		for($i = 0; $i < count($array); $i++) {
    			echo $keys[$i] . "{<br>";
   			foreach($array[$keys[$i]] as $key => $value) {
       				echo $key . " : " . $value . "<br>";
    			}
    			echo "}<br>";
		}	
		}
	    function openTimesCSVK() {
		$k = $_POST['openTimesCSVK_'];
		$json3 = file_get_contents('http://laptop-service/listOpenOnly/csv?top=' . $k);
		echo "<p>$json3</p>";
		}
	    function closeTimesCSVK() {
		$k = $_POST['closeTimesCSVK_'];
		$json3 = file_get_contents('http://laptop-service/listCloseOnly/csv?top=' . $k);
		echo "<p>$json3</p>";
		}
	    if (array_key_exists("allTimes", $_POST)) {
		    allTimes();
	    }
	    if (array_key_exists("listOpenOnly", $_POST)) {
		    openTimes();
	    }
	    if (array_key_exists("listCloseOnly", $_POST)) {
		    closeTimes();
	    }
	    if (array_key_exists("allTimesJSON", $_POST)) {
		    allTimes();
	    }
	    if (array_key_exists("openTimesJSON", $_POST)) {
		    openTimes();
	    }
	    if (array_key_exists("closeTimesJSON", $_POST)) {
		    closeTimes();
	    }
	    if (array_key_exists("allTimesCSV", $_POST)) {
		    allTimesCSV();
	    }
	    if (array_key_exists("openTimesCSV", $_POST)) {
		    openTimesCSV();
	    }
	    if (array_key_exists("closeTimesCSV", $_POST)) {
		    closeTimesCSV();
	    }
	    if (array_key_exists("openTimesJSONK", $_POST)) {
		    openTimesJSONK();
	    }
	    if (array_key_exists("closeTimesJSONK", $_POST)) {
		    closeTimesJSONK();
	    }
	    if (array_key_exists("openTimesCSVK", $_POST)) {
		    openTimesCSVK();
	    }
	    if (array_key_exists("closeTimesCSVK", $_POST)) {
		    closeTimesCSVK();
	    }
	?>

    </body>
</html>

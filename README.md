Brevet-Time-REST-api
--------------------

This application is a simple listing service to show expose 
data that is stored within a database.

If you are a user:
------------------
Start by launching the web page that is on port 5000.

You can enter in control times and submit them to a database.
Once they are in the database, you can view them with the display
button.

Once times are entered into the database, you may navigate to
"http://<host:5002>" where you can use a series of buttons and
forms to find the information of your choice, and it will show on the web
page.


If you are a developer:
-----------------------
After times have been entered into the database, you can navigate to 
port 5001 and enter in the following urls to retrieve information as you choose.

URLS:
-----
* "http://<host:5001>/listAll" returns all open and close times in the database
* "http://<host:5001>/listOpenOnly" returns open times only
* "http://<host:5001>/listCloseOnly" returns close times only

* "http://<host:5001>/listAll/csv" returns all open and close times in CSV format
* "http://<host:5001>/listOpenOnly/csv" returns open times only in CSV format
* "http://<host:5001>/listCloseOnly/csv" returns close times only in CSV format
* "http://<host:5001>/listAll/json" returns all open and close times in JSON format
* "http://<host:5001>/listOpenOnly/json" returns open times only in JSON format
* "http://<host:5001>/listCloseOnly/json" returns close times only in JSON format

* "http://<host:5001>/listOpenOnly/csv?top=k" returns top k open times only (in ascending order) in CSV format
* "http://<host:5001>/listOpenOnly/json?top=k" returns top k open times only (in ascending order) in JSON format
* "http://<host:5001>/listCloseOnly/csv?top=k" returns top k close times only (in ascending order) in CSV format
* "http://<host:5001>/listCloseOnly/json?top=k" returns top k close times only (in ascending order) in JSON format

The docker-compose is within proj6-rest/DockerRestAPI, and it creates three four containers, one for the ACP Brevet
Time Calculator, one for the website service which is the user interface, one for the laptop service (The url exposing service)
and one to create the mongodb image to store data.

The Dockerfile for the laptop service it in proj6-rest/DockerRestAPI/laptop/
The Dockerfile for the ACP Brevet Time Calculator is in proj6-rest/DockerRestAPI/proj5-mongo/DockerMongo

The JSON ad CSV display for the URL (port 5001) and Button (port 5002) display the values as raw data, and are not altered
by the program. They are simply display as is within the html of the webpage. 



Author: Wil Sprouse
email: wils@cs.uoregon.edu















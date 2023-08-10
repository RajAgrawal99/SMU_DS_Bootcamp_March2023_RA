
ALL screen shots are in --Module 15 Challenge-leaflet.PDF

Module 15 Challenge - Leaflet
SMU DS – Raj Agrawal   
Submitted on: 09-AUG-2023
Repository – https://github.com/RajAgrawal99/SMU_DS_Bootcamp_March2023_RA.git
Folder – leaflet-challenge

Data source
https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
 

Sample index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Leaflet Step-1</title>

Sample logic.js
// SMU DS leaflet-challenge Part 1: Create the Earthquake Visualization
function clickListener() {
  let filter = document.getElementById('earthquake_filter').value;
  // STEP 0: GET THE DATA
  // Store our API endpoint as queryUrl.
  let queryUrl = `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_${filter}.geojson`;
  let url2 = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";
Part 1: Create the Earthquake Visualization

1.	Import and visualize the data by doing the following:
o	Using Leaflet, create a map that plots all the earthquakes from your dataset based on their longitude and latitude.
	Your data markers should reflect the magnitude of the earthquake by their size and the depth of the earthquake by color. Earthquakes with higher magnitudes should appear larger, and earthquakes with greater depth should appear darker in color.
	Hint: The depth of the earth can be found as the third coordinate for each earthquake.
o	Include popups that provide additional information about the earthquake when its associated marker is clicked.
o	Create a legend that will provide context for your map data.
o	Your visualization should look something like the preceding map.

  



README.md file added to the folder

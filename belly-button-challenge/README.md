
ALL screen shots are in --Module 14 Challenge.PDF

Module 14 Challenge - The Belly Button Biodiversity
SMU DS – Raj Agrawal   
Submitted on: 09-AUG-2023
Repository – https://github.com/RajAgrawal99/SMU_DS_Bootcamp_March2023_RA.git
Folder – belly-button-challenge

Data source
samples.json from the URL -   https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json
Index.html


Use the D3 library to read in�samples.json�from the URL�

Example of index.html

<!DOCTYPE html>
<html lang="en">

<head>
� <meta charset="UTF-8">
� <meta name="viewport" content="width=device-width, initial-scale=1.0">
� <meta http-equiv="X-UA-Compatible" content="ie=edge">
� <title>Bellybutton Biodiversity</title>
� <script src="https://d3js.org/d3.v7.min.js"></script>
� <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
� <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
</head>
<body>
� <div class="container-fluid">
� � <div class="row">
� � � <div class="col-md-12 jumbotron text-center">
� � � � <h1>Belly Button Biodiversity Dashboard</h1>
� � � � <p>Use below interactive charts, to explore the dataset</p>
� � � </div>
� � </div>

Example of app.js

// on page start...

d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then(function (data) {
console.log(data);



2.	horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
Use�sample_values�as the values for the bar chart.
Use�otu_ids�as the labels for the bar chart.
Use�otu_labels�as the hovertext for the chart.
 

3.	bubble chart that displays each sample.
Use�otu_ids�for the x values.
Use�sample_values�for the y values.
Use�sample_values�for the marker size.
Use�otu_ids�for the marker colors.
Use�otu_labels�for the text values.

 










4.	Display the sample metadata, i.e., an individual's demographic information.

5.	Display each key-value pair from the metadata JSON object somewhere on the page.


 

6.	An example dashboard is shown 

 

 

7.	README.md file

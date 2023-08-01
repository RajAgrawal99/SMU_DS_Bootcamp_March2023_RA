function clickListener() {

  let min_size = parseInt(document.getElementById('min_size').value);
  let max_size = parseInt(document.getElementById('max_size').value);
  let state = document.getElementById('state').value
  let url = `/api/v1.0/${min_size}/${max_size}/${state}`;

  // nuke map
  d3.select("#map_container").html("");
  d3.select("#map_container").html("<div id='map'></div>");

  d3.json(url).then(function (data) {
    console.log(data);

    makePlots(data.raw_data, data.month_data);
    createMap(data.raw_data);
  });
}
function makePlots(raw_data, month_data) {
    // Slice the first 10 objects for plotting
    let data_sub = raw_data.slice(0, 9);
    // Reverse the array to accommodate Plotly's defaults
    data_sub.reverse();
    // Trace for the wildfire Data
    let trace1 = {
      x: data_sub.map(row => row.fire_size),
      y: data_sub.map(row => row.fire_name),
      name: `wildfires`,
      type: 'bar',
      orientation: "h",
      marker: {color: '#ff6464'}
    };
    // Data array
    let data = [trace1];
    // Apply a title to the layout
    let layout = {
      "title": `Largest Wildfires by Acres`,
      xaxis:{
        title:{
          text:'Est. Acres Burned'
        }
      },
      width: 950
    }
    // Render the plot to the div tag with id "plot"
    Plotly.newPlot("bar", data, layout);

    let trace2 = {
      type: 'pie',
      hole: 0.4,
      marker:{
        colors: ['#ff6464','#ff8264','#ffaa64','#fff5a5','#212121','#c06c84','#f8b595','#edf798','#ffad5a','#4f9da6','#1a0841','#bb5a5a']
      },
      labels: month_data.map(row => row.month),
      values: month_data.map(row => row.counts),
  }
    let data2 = [trace2];
    let layout2 = {
      title: 'Percentage of Wildfires by Month',
      height: 500,
      width: 500
    };
    Plotly.newPlot('myDiv', data2, layout2);
}
  function createMap(inp_data) {
    // STEP 1: CREATE THE BASE LAYERS
    // Create the base layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }); 
   

    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });

    let googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
    });

    // watercolor 
    let watercolor = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
	  attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	  subdomains: 'abcd',
	  minZoom: 1,
	  maxZoom: 16,
	  ext: 'jpg'
    });





    
    // STEP 2: CREATE THE OVERLAY LAYERS
    // Create an overlays object.
    let markers = L.markerClusterGroup();
    let coords = [];
    for (let i = 0; i < inp_data.length; i++){
      let wildfire = inp_data[i];
      let coord = [wildfire.latitude, wildfire.longitude];
      let marker = L.marker(coord).bindPopup(`${wildfire.fire_name}<hr>Cause: ${wildfire.stat_cause_descr}, Date: ${wildfire.disc_clean_date}`);
      markers.addLayer(marker);
      coords.push(coord);
    }
    // create heatmap layer
    let heatLayer = L.heatLayer(coords, {
      radius: 8, 
      minOpacity: 70, 
      max: 1000,
      gradient: {1: 'red', 0.7: 'orange', 0.5: 'yellow'}
      
    });
    // STEP 3: Build the Layer Controls
    // Create a baseMaps object.
    let baseMaps = {
      "Street Map": street,
      "Topographic Map": topo,
      "Google Satellite": googleSat, 
      "Water Color":watercolor,
    };
    let overlayMaps = {
      "wildfires": markers,
      "Heat Map": heatLayer,
    };
    // STEP 4: Init the Map
    // Create a new map.
    // Edit the code to add the wildfire data to the layers.
    let myMap = L.map("map", {
      center: [38, -100],
      zoom: 5,
      layers: [street, markers, heatLayer]
    });
    // STEP 5: Add the Layer Controls/Legend to the map
    // Create a layer control that contains our baseMaps.
    // Be sure to add an overlay Layer that contains the wildfire GeoJSON.
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
  }
  // on page load
  clickListener();
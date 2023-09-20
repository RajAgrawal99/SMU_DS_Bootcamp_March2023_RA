function makeBarPlot(regions, show) {
    let region_values = regions.map(x => x.counts)
  
    // Create an array of category labels
    let labels = regions.map(x => x.region);

    // @ADD YOUR CODE HERE
    let trace = {
      x: labels,
      y: region_values,
      type: 'bar',
      marker: {color: "tropic"}
    };
    
    let data = [trace];
    
    let layout = {
      title: `Anthony Bourdain Regions for ${show}`
    };
    
    Plotly.newPlot('bar', data, layout);
  };

function makePiePlot(seasons, show) {
    let season_values = seasons.map(x => x.counts)

    // Create an array of category labels
    let labels = seasons.map(x => x.season);


    // @ADD YOUR CODE HERE
    let trace = {
        values: season_values,
        labels: labels,
        hole: .4,
        type: 'pie',
        
    };

    let data = [trace];

    let layout = {
        title: `Anthony Bourdain Seasons for ${show}`
    };

    Plotly.newPlot('pie', data, layout);
};

function createMap(data) {
  
    // STEP 1: CREATE THE BASE LAYERS
  
    // Create the base layers.
    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })
  
    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });
  
    // STEP 2: CREATE THE OVERLAY LAYERS
  
    // Create an overlays object.
    let markers = L.markerClusterGroup();
    let coords = [];
    for (let i = 0; i < data.length; i++){
        let row = data[i];
  
     
        let coord = [row.Latitude, row.Longitude];
        let marker = L.marker(coord).bindPopup(`${row.Show}<hr>${row.Title}`);
        markers.addLayer(marker);

        coords.push(coord);
     
    }
  
    // create heatmap layer
    let heatLayer = L.heatLayer(coords, {
      radius: 20,
      blur: 1
    });
  
   
  
    // STEP 3: Build the Layer Controls
  
    // Create a baseMaps object.
    let baseMaps = {
      "Street Map": street,
      "Topographic Map": topo
    };
  
    let overlayMaps = {
      "Locations": markers,
      "Heat Map": heatLayer
    };
  
    // STEP 4: Init the Map
  
    // Create a new map.
    // Edit the code to add the earthquake data to the layers.
    let myMap = L.map("map", {
      center: [0, 0],
      zoom: 3,
      layers: [street, markers]
    });
  
    // STEP 5: Add the Layer Controls/Legend to the map
    // Create a layer control that contains our baseMaps.
    // Be sure to add an overlay Layer that contains the earthquake GeoJSON.
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
  }

function doWork() {
    let show = document.getElementById('show_dropdown').value;
    let url = `/api/v1.0/dashboard_data/${show}`;
    
    // nuke map
    d3.select("#map_container").html("");
    d3.select("#map_container").html("<div id='map'></div>");
  



    // make request
    d3.json(url).then(function (data) {
        console.log(data);
        makePiePlot(data.seasons,show);
        makeBarPlot(data.regions,show);
        createMap(data.raw_data);
    });
  }

doWork();
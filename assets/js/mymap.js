// // replace "toner" here with "terrain" or "watercolor"
// var layer = new L.StamenTileLayer("toner-lite");
// var map = new L.Map('map', {
//     center: new L.LatLng(52.004713, 4.370334),
//     zoom: 16
// });
// map.addLayer(layer);




// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([52.004713, 4.370334], 16);

// add an OpenStreetMap tile layer
L.tileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="//openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// // add an OpenStreetMap tile layer
// L.tileLayer('//stamen-tiles-{s}.a.ssl.fastly.net/{z}/{x}/{y}.jpg', {
//     attribution: '&copy; <a href="//openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(map);

var marker = L.marker([52.004713,4.370334]).addTo(map);
marker.bindPopup("<b>Faculty of Architecture & the Built Environment<br>Julianalaan 134, 2628BL Delft</b><br>(my office is roughly where the arrow is, on the ground floor)").openPopup();
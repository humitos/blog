$(document).ready(function (){
    // check if the map id exists before executing the code
    if ($('#map').length) {
	$.getJSON("/assets/js/point.json", function(data){
	    var map = L.map('map').setView(data, 11);

	    // create the tile layer with correct attribution
	    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	    var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
	    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 14, attribution: osmAttrib});
	    map.addLayer(osm);

	    var marker = L.marker(data).addTo(map);
	    marker.bindPopup("<b><em>humitos</em></b> está <em>por</em> aquí!").openPopup();
	});
    }
});

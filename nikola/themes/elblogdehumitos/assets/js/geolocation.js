$(document).ready(function (){
    // check if the map id exists before executing the code
    if ($('#map').length) {
	$.getJSON("/assets/js/point.json", function(data){
	    var icon = L.icon({
		iconUrl: '/assets/img/marker.png',
		shadowUrl: '/assets/img/marker-shadow.png',

		iconSize:     [64, 36], // size of the icon
		shadowSize:   [82, 49], // size of the shadow
		iconAnchor:   [32, 0],   // point of the icon which will correspond to marker's location
		shadowAnchor: [28, 10],   // the same for the shadow
		popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
	    });

	    var map = L.map('map').setView(data, 11);

	    // create the tile layer with correct attribution
	    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	    var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
	    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 14, attribution: osmAttrib});
	    map.addLayer(osm);

	    var marker = L.marker(data, {icon: icon}).addTo(map);
	    marker.bindPopup("<b><em>humitos</em></b> está <em>por</em> aquí!").openPopup();
	});
    }
});

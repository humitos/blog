$(document).ready(function (){
    // check if the map id exists before executing the code
    if ($('#map').length) {
	$.getJSON("/assets/js/points.json", function(points){
	    var icon = L.icon({
		iconUrl: '/assets/img/marker.png',
		shadowUrl: '/assets/img/marker-shadow.png',

		iconSize:     [64, 36], // size of the icon
		shadowSize:   [82, 49], // size of the shadow
		iconAnchor:   [32, 0],   // point of the icon which will correspond to marker's location
		shadowAnchor: [28, 10],   // the same for the shadow
		popupAnchor:  [0, 0] // point from which the popup should open relative to the iconAnchor
	    });

	    var current_position = points[0]
	    var map = L.map('map').setView(current_position, 11);

	    // create the tile layer with correct attribution
	    var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	    var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
	    var osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 14, attribution: osmAttrib});
	    map.addLayer(osm);

	    var marker = L.marker([current_position.lat, current_position.lng], {icon: icon}).addTo(map);
	    marker.bindPopup("<b><em>humitos</em></b> está <em>por</em> aquí!").openPopup();

	    // create route
	    if(points.length > 1) {
		router = L.Routing.osrm();
		waypoints = [];
		$.each(points, function(i, point) {
		    waypoints.push({latLng: L.latLng(point.lat, point.lng)});
		});

		router.route(waypoints, function(err, routes) {
		    if (err) {
			console.warn(err.message);
		    } else {
			line = L.Routing.line(routes[0]).addTo(map);
		    }
		});
	    }
	});
    }
});

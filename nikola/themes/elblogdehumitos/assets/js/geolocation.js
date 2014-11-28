var map;
var osmLayer;

$(document).ready(function (){
    // check if the map id exists before executing the code
    if ($('#map').length) {

        map = L.map(
            'map',
            {fullscreenControl: true}
        );

        // create the tile layer with correct attribution
        var osmUrl='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        var osmAttrib='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
        osmLayer = new L.TileLayer(osmUrl, {minZoom: 4, maxZoom: 14, attribution: osmAttrib});
        map.addLayer(osmLayer);

	// http://osrm.at/acF
	var gpxUrl = '/assets/data/segunda-etapa.gpx';
	gpxLayer = new L.GPX(gpxUrl, {
	    async: true,
	    marker_options: {
		startIconUrl: '/assets/img/no-icon.png',
		endIconUrl: '/assets/img/no-icon.png',
		shadowUrl: '/assets/img/no-icon.png'
	    }
	}).on('loaded', function(e) {
	    gpxlayer.bindPopup("Ruta realizada en la <em>Segunda Etapa</em>");
	    // map.addLayer(e.target);
	});



        $.getJSON('/assets/data/cities.json', function(data) {
            var layers = {};
            var redIcon = new L.Icon({
                iconUrl: '/assets/img/marker-icon-red.png',
                shadowUrl: '/assets/img/marker-icon-shadow.png',
                iconSize:     [25, 41], // size of the icon
                shadowSize:   [41, 41], // size of the shadow
                iconAnchor:   [12, 41],  // point of the icon which will correspond to marker's location
                shadowAnchor: [12, 41], // the same for the shadow
                popupAnchor:  [0, -50]    // point from which the popup should open relative to the iconAnchor
            });

	    var greenIcon = new L.Icon({
		iconUrl: '/assets/img/marker-icon-green.png',
		shadowUrl: '/assets/img/marker-icon-shadow.png',
		iconSize:     [25, 41], // size of the icon
		shadowSize:   [41, 41], // size of the shadow
		iconAnchor:   [12, 41],  // point of the icon which will correspond to marker's location
		shadowAnchor: [12, 41], // the same for the shadow
		popupAnchor:  [0, -50]    // point from which the popup should open relative to the iconAnchor
	    });

	    $.each(['previous', 'next'], function(i, when) {
		var markers = [];
		$.each(data[when], function(i, city) {
		    var point = [city.lat, city.lng];
		    if (when == 'next') icon = redIcon
		    else icon = greenIcon
		    var city_name = city.address.split(', ')[0];
		    markers.push(L.marker(point, {icon: icon}).bindPopup(city_name + ', ' + city.state));
		});
		layers[when] = L.layerGroup(markers);
	    });

	    // var baseMaps = {
	    // 	'Map': osmLayer
	    // };

	    var overlayMaps = {
		"<img src='/assets/img/marker-icon-red.png' /> <span>Próximas ciudades</span>": layers['next'],
		"<img src='/assets/img/marker-icon-green.png' /> <span>Ciudades Visitadas</span>": layers['previous'],
		"<img src='/assets/img/blue-line.png' /> <span>Ruta <em>Segunda Etapa</em></span>": gpxLayer
	    };

	    L.control.layers(null, overlayMaps).addTo(map);
	});

	$.getJSON("/assets/data/my-position.json", function(point){
	    var icon = L.icon({
		iconUrl: '/assets/img/marker-car.png',
		shadowUrl: '/assets/img/marker-car-shadow.png',

		iconSize:     [64, 36], // size of the icon
		shadowSize:   [82, 49], // size of the shadow
		iconAnchor:   [32, 0],   // point of the icon which will correspond to marker's location
		shadowAnchor: [28, 10],   // the same for the shadow
		popupAnchor:  [0, -10] // point from which the popup should open relative to the iconAnchor
	    });

	    // center the map in my position
	    map.setView(point, 11);

	    var marker = L.marker(point, {icon: icon}).addTo(map);
	    marker.bindPopup("<b><em>humitos</em></b> está <em>por</em> aquí!").openPopup();
	});

    }
});







// console.log("Rachel js is loaded")
// var json_data 
var phu_data

// d3.json("/confirmed_positive_cases.json").then(function(data) {
//     console.log(data);
//     json_data = data

    d3.json("/PHU_borders").then(function(data) {
        //console.log(data);
        phu_data = data
   
   

    var myMap = L.map("map", {
      center: [43.6532, -79.3832],
      zoom: 6
    });


    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(myMap);



L.geoJson(phu_data).addTo(myMap);

function getColor(d) {
    return d == 2263 ? '#FED976' :
            d == 2226 ? '#FED976' :
            d == 2247 ? '#FEB24C' :
            d == 2257 ? '#FEB24C' :
            d == 2249 ? '#FD8D3C' :
            d == 2238 ? '#FD8D3C' :
            d == 2241 ? '#FD8D3C' :
            d == 2255 ? '#FD8D3C' :
            d == 2243 ? '#FD8D3C' :
            d == 2240 ? '#FD8D3C' :
            d == 5183 ? '#E31A1C' :
            d == 2256 ? '#E31A1C' :
            d == 2233 ? '#E31A1C' :
            d == 2261 ? '#E31A1C' :
            d == 2235 ? '#E31A1C' :
            d == 2234 ? '#E31A1C' :
            d == 2262 ? '#E31A1C' :
            d == 2242 ? '#E31A1C' :
            d == 2227 ? '#E31A1C' :
            d == 4913 ? '#E31A1C' :
            d == 2258 ? '#E31A1C' :
            d == 2266 ? '#E31A1C' :
            d == 2260 ? '#BD0026' :
            d == 2244 ? '#BD0026' :
            d == 2246 ? '#BD0026' :
            d == 2268 ? '#BD0026' :
            d == 2236 ? '#BD0026' :
            d == 2265 ? '#BD0026' :
            d == 2237 ? '#800026' :
            d == 2230 ? '#800026' :
            d == 2251 ? '#800026' :
            d == 2270 ? '#800026' :
            d == 2253 ? '#800026' :
            d == 3895 ? '#800026' :
                        '#FFEDA0';

}
    function style(feature) {
    return {
        fillColor: getColor(feature.properties.PHU_ID),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}

L.geoJson(phu_data, {style: style}).addTo(myMap);

var geojson;
function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    
info.update(layer.feature.properties);
    }
}

function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: zoomToFeature
    });
}

geojson = L.geoJson(phu_data, {
    style: style,
    onEachFeature: onEachFeature
}).addTo(myMap);


var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
    this._div.innerHTML = '<h4>COVID-19 Cases by Public Health Unit</h4>' +  (props ?
        '<b>' + props.NAME_ENG + '</b><br />' + ' ID: <sup></sup>' + props.PHU_ID 
        : 'Hover over to view more');
};

info.addTo(myMap);



// var legend = L.control({position: 'bottomleft'});

// legend.onAdd = function (map) {

//     var div = L.DomUtil.create('div', 'info legend'),
//         grades = [0, 10, 20, 50, 100, 200, 500, 1000],
//         labels = [];

//     // loop through our density intervals and generate a label with a colored square for each interval
//     for (var i = 0; i < grades.length; i++) {
//         div.innerHTML +=
//             '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
//             grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
//     }

//     return div;
// };

// legend.addTo(map);

    });





 
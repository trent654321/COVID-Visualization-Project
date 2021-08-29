console.log("Rachel js is loaded")
var json_data 
var phu_data

d3.json("/confirmed_positive_cases.json").then(function(data) {
    console.log(data);
    json_data = data

    d3.json("/PHU_borders").then(function(data) {
        console.log(data);
        phu_data = data
     
    //code here reference functions


    });
}); 

//def functions here 

// //create map object
// var myMap = L.map("map", {
//   center: [43.6532, -79.3832],
//   zoom: 8
// });


// // Adding the tile layer
// L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//     attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
// }).addTo(myMap);

// // //want to add layer with PHU boundary PHU_ID and reporting_phu_id

// //count each time a PHU_ID is mentioned and display the count on the chunk of map

// //filter by day?? have drop down menu to choose which day to display heatmap for??
// //filter by month?? year??
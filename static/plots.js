console.log("Rachel js is loaded")
var json_data 
var phu_data

d3.json("/confirmed_positive_cases.json").then(function(data) {
    console.log(data);
    json_data = data


});
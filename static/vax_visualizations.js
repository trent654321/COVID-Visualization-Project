var labels = ['Full','Partial','None','Unknown']
d3.json("http://127.0.0.1:5000/vac_status_hosp_icu.json").then(function(data) {
    var sumFull = 0;
    var sumPartial = 0;
    var sumNone = 0;
    var sumUnkown = 0;
    Object.keys(data).forEach(key => {
        sumFull += parseInt(data[key]['hospitalnonicu_full_vac']);
        sumPartial += parseInt(data[key]['hospitalnonicu_partial_vac']);
        sumNone += parseInt(data[key]['hospitalnonicu_unvac']);
    });
    values = [sumFull,sumPartial,sumNone,sumUnkown]
    makePie("hospitalizations_pie_chart",values,labels,"Hospitalizations by vaccination status")
    sumFull = 0;
    sumPartial = 0;
    sumNone = 0;
    sumUnkown = 0;
    
    Object.keys(data).forEach(key => {
        sumFull += parseInt(data[key]['icu_full_vac']);
        sumPartial += parseInt(data[key]['icu_partial_vac']);
        sumNone += parseInt(data[key]['icu_unvac']);
    });
    values = [sumFull,sumPartial,sumNone,sumUnkown]
    makePie("icu_pie_chart",values,labels,"ICU patients by vaccination status")

    
});

d3.json("http://127.0.0.1:5000/cases_by_vac_status.json").then(function(data) {
    var sumFull = 0;
    var sumPartial = 0;
    var sumNone = 0;
    var sumUnkown = 0;
    Object.keys(data).forEach(key => {
        sumFull += parseInt(data[key]['covid19_cases_full_vac']);
        sumPartial += parseInt(data[key]['covid19_cases_partial_vac']);
        sumNone += parseInt(data[key]['covid19_cases_unvac']);
        sumUnkown += parseInt(data[key]['covid19_cases_vac_unknown']);
    });
    values = [sumFull,sumPartial,sumNone,sumUnkown]
    makePie("total_cases_pie_chart",values,labels,"Total Cases by vaccination status")
});

function makePie(divID,values,labels,title){
    var div = document.getElementById(divID);
    var traceA = {
        type: "pie",
        values: values,
        labels: labels
    };
    var data = [traceA];
    var layout = {
        title: title
    };
    Plotly.plot(div, data, layout);

};

 


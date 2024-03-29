from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import database_URI
from sqlalchemy.ext.automap import automap_base
from datetime import datetime 
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Vac_status_hosp_icu = Base.classes.vac_status_hosp_icu
Cases_by_vac_status = Base.classes.cases_by_vac_status
Vaccine_doses = Base.classes.vaccine_doses
Confirmed_positive_cases = Base.classes.confirmed_positive_cases
Vaccines_by_age_phu = Base.classes.vaccines_by_age_phu
Vaccines_by_age = Base.classes.vaccines_by_age

@app.route('/')
def index():
    title = "COVID 19 Visualizations"
    paragraph = "Welcome to the homepage of our COVID-19 Visualizations. The visuals you see displayed are the result of data transformation, storage and manipulation. The data is presented using JavaScript, Leaflet and Plot.ly. Our data was downloaded from the official Ontario website and stored in an SQL database. Below are links to out data and other helpful COVID-19 Resources:"
    return render_template('index.html',title=title,paragraph=paragraph)

@app.route('/vac_status_hosp_icu.json')
def vac_status_hosp_icu_json():
    results =db.session.query(Vac_status_hosp_icu).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['date']
        date = date.strftime('%x')
        entry['date'] = date
        output[date] = entry
    return output

@app.route('/cases_by_vac_status.json')
def cases_by_vac_status_json():
    results =db.session.query(Cases_by_vac_status).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['date']
        date = date.strftime('%x')
        entry['date'] = date
        output[date] = entry
    return output

@app.route('/vaccine_doses.json')
def vaccine_doses_json():
    results =db.session.query(Vaccine_doses).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['report_date']
        date = date.strftime('%x')
        entry['report_date'] = date
        output[date] = entry
    return output

@app.route('/confirmed_positive_cases.json')
def confirmed_positive_cases_json():
    results =db.session.query(Confirmed_positive_cases).limit(100).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        id = entry['id']
        entry['reporting_phu_latitude'] = str(entry['reporting_phu_latitude'])
        entry['reporting_phu_longitude'] = str(entry['reporting_phu_longitude'])
        output[id] = entry
    return output


@app.route('/vaccines_by_age_phu.json')
def vaccines_by_age_phu_json():
    results =db.session.query(Vaccines_by_age_phu).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['date']
        date = date.strftime('%x')
        entry['date'] = date
        output[date] = entry
    return output

@app.route('/vaccines_by_age.json')
def vaccines_by_age_json():
    results =db.session.query(Vaccines_by_age).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['date']
        date = date.strftime('%x')
        entry['date'] = date
        output[date] = entry
    return output

@app.route('/vax_visualizations')
def vax_visualizations():
    title = "Effects of Vaccination on COVID Outcomes"
    paragraph = "The visualizations on this page show the percentage of the population that is vaccinated, the percentage of covid cases where the subjects are vaccinated, the percentage of COVID hospitalizaions where the subject is vaccinated and the percentage of COVID patients in the ICU who are vaccinated."
    return render_template('vax_visualizations.html',title=title,paragraph=paragraph)


@app.route('/map_visualization')
def map_visualization():
    title = "COVID-19 Cases in Ontario by Health Unit"
    paragraph = "Total COVID-19 Cases Reported by each PHU (Dec 2020 - Aug 2021)"
    return render_template('map_visuals.html',title=title,paragraph=paragraph)

@app.route('/PHU_borders')
def PHU_borders():
    return requests.get("https://opendata.arcgis.com/datasets/c2fa5249b0c2404ea8132c051d934224_0.geojson").json()

@app.route('/gender')
def gender():
    title ="Covid 19 Cases by Gender"
    paragraph = "How covid is spread in relation to gender"
    src="/static/images/Covid19_cases_by_gender.png"
    alt="Gender Graph"
    figcaption="This information is cumulative – numbers are the total of all cases since January 15, 2020.."
    return render_template('from_image.html',title=title, paragraph=paragraph,src=src,alt=alt,figcaption=figcaption)

@app.route('/age')
def age():
    title ="COVID 19 cases by Age"
    paragraph = "How covid is spread in relation to age"
    src="/static/images/COVID-19_Case_Age_Group.png"
    alt="Age Graph"
    figcaption="This information is cumulative – numbers are the total of all cases since January 15, 2020.."
    return render_template('from_image.html',title=title, paragraph=paragraph,src=src,alt=alt,figcaption=figcaption)

@app.route('/deaths')
def deaths():
    title ="Visualization of COVID Deaths"
    paragraph = "Estimate of the number of fatalities caused by covid 19 by city"
    src="/static/images/Covid19_Deaths.png"
    alt="Deaths Graph"
    figcaption="This information is cumulative – numbers are the total of all cases since January 15, 2020.."
    return render_template('from_image.html',title=title, paragraph=paragraph,src=src,alt=alt,figcaption=figcaption)

@app.route('/aquisition')
def aquisition():
    title ="Aquisition of COVID 19"
    paragraph = "Different methods of COVID aquisition"
    src="/static/images/Covid-19_Acquisition.png"
    alt="Aqusistion Graph"
    figcaption="This information is cumulative – numbers are the total of all cases since January 15, 2020.."
    return render_template('from_image.html',title=title, paragraph=paragraph,src=src,alt=alt,figcaption=figcaption)


if __name__ == '__main__':
    app.run(debug=True)

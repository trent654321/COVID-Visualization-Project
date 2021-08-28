from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import database_URI
from sqlalchemy.ext.automap import automap_base
from datetime import datetime

app = Flask(__name__)
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
    return "Hello World!"

@app.route('/vac_status_hosp_icu')
def vac_status_hosp_icu_route():
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

@app.route('/cases_by_vac_status')
def cases_by_vac_status_route():
    results =db.session.query(Cases_by_vac_status).all()
    print(results)
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = entry['date']
        date = date.strftime('%x')
        entry['date'] = date
        output[date] = entry
    return output

@app.route('/vaccine_doses')
def vaccine_doses_route():
    results =db.session.query(Vaccine_doses).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        date = str(entry['report_date'])
        date = date.strftime('%x')
        entry['report_date'] = date
        output[date] = entry
    return output

@app.route('/confirmed_positive_cases')
def confirmed_positive_cases_route():
    results =db.session.query(Confirmed_positive_cases).all()
    output = {}
    for result in results:
        entry = result.__dict__
        entry.pop('_sa_instance_state',None)
        id = entry['id']
        lat = 'rp'
        output[id] = entry
    return output


@app.route('/vaccines_by_age_phu')
def vaccines_by_age_phu_route():
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

@app.route('/vaccines_by_age')
def vaccines_by_age_route():
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



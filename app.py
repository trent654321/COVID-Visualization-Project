from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import database_URI
from sqlalchemy.ext.automap import automap_base
from datetime import datetime
from flask import render_template
from flask_cors import CORS

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
    return render_template('index.html')

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
    results =db.session.query(Confirmed_positive_cases).all()
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



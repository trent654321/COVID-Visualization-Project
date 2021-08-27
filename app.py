from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import database_URI
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Vac_status_hosp_icu = Base.classes.vac_status_hosp_icu

@app.route('/')
def index():
    return "Hello World!"

@app.route('/vac_status_hosp_icu')
def vac_status_hosp_icu_route():
    results =db.session.query(Vac_status_hosp_icu).all()
    for result in results:
        print(result.date)
    return("test")


import sqlalchemy
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class vac_status_hosp_icu(Base):
    __tablename__ = 'vac_status_hosp_icu'
    date = Column(Date(), primary_key=True)
    icu_unvac = Column(Integer())
    icu_partial_vac = Column(Integer())
    icu_full_vac = Column(Integer())
    hospitalnonicu_unvac = Column(Integer())
    hospitalnonicu_partial_vac = Column(Integer())
    hospitalnonicu_full_vac = Column(Integer())

class cases_by_vac_status(Base):
    __tablename__ = 'cases_by_vac_status'
    date = Column(Date(), primary_key=True)
    covid19_cases_unvac = Column(Integer())
    covid19_cases_partial_vac = Column(Integer())
    covid19_cases_full_vac = Column(Integer())
    covid19_cases_vac_unknown = Column(Integer())

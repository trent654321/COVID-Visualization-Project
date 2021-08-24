import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, Numeric, DateTime
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

class vaccine_doses(Base):
    __tablename__ = 'vaccine_doses'
    report_date = Column(Date(), primary_key=True)
    previous_day_total_doses_administered = Column(Integer())
    previous_day_at_least_one = Column(Integer())
    previous_day_fully_vaccinated = Column(Integer())
    total_doses_administered = Column(Integer())
    total_individuals_at_least_one = Column(Integer())
    total_doses_in_fully_vaccinated_individuals = Column(Integer())
    total_individuals_fully_vaccinated = Column(Integer())

class confirmed_positive_cases(Base):
    __tablename__ = 'confirmed_positive_cases'
    id = Column(Integer(), primary_key=True)
    row_id = Column(Integer())
    accurate_episode_date = Column(DateTime())
    case_reported_date = Column(DateTime())
    test_reported_date = Column(DateTime()) 
    specimen_date = Column(DateTime())
    age_group = Column(String())
    client_gender = Column(String())
    case_acquisition_info = Column(String())
    outcome1 = Column(String())
    outbreak_related = Column(String())
    reporting_phu_id = Column(Integer())
    reporting_phu = Column(String())
    reporting_phu_address = Column(String())
    reporting_phu_city = Column(String())
    reporting_phu_postal_code = Column(String())
    reporting_phu_website = Column(String())
    reporting_phu_latitude = Column(Numeric())
    reporting_phu_longitude = Column(Numeric())

class vaccines_by_age_phu(Base):
    __tablename__ = 'vaccines_by_age_phu'
    date = Column(Date(),primary_key=True)
    phu_id = Column(Integer(),primary_key=True)
    phu_name = Column(String())
    age_group = Column(String(),primary_key=True)
    at_least_one_dose_cumulative = Column(Integer())
    second_dose_cumulative = Column(Integer())
    total_population = Column(Integer())
    percent_at_least_one_dose = Column(Numeric())
    percent_fully_vaccinated = Column(Numeric())


class vaccines_by_age(Base):
    __tablename__ = 'vaccines_by_age'
    date = Column(Date(),primary_key=True)
    age_group = Column(String(),primary_key=True)
    at_least_one_dose_cumulative = Column(Integer())
    second_dose_cumulative = Column(Integer())
    total_population = Column(Integer())
    percent_at_least_one_dose = Column(Numeric())
    percent_fully_vaccinated = Column(Numeric())
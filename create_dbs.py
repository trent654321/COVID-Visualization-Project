from config import database_URI
from models import Base
from sqlalchemy import create_engine

engine = create_engine(database_URI,echo=True)
Base.metadata.create_all(engine)

csv_file_path = "./data/vac_status_hosp_icu.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY vac_status_hosp_icu(date,icu_unvac,icu_partial_vac,icu_full_vac,hospitalnonicu_unvac,hospitalnonicu_partial_vac,hospitalnonicu_full_vac) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()

csv_file_path = "./data/cases_by_vac_status.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY cases_by_vac_status(date,covid19_cases_unvac,covid19_cases_partial_vac,covid19_cases_full_vac,covid19_cases_vac_unknown) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()

csv_file_path = "./data/vaccine_doses.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY vaccine_doses(report_date,previous_day_total_doses_administered,previous_day_at_least_one,previous_day_fully_vaccinated,total_doses_administered,total_individuals_at_least_one,total_doses_in_fully_vaccinated_individuals,total_individuals_fully_vaccinated) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()


csv_file_path = "./data/confirmed_positive_cases.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY confirmed_positive_cases(id,row_id,accurate_episode_date,case_reported_date,test_reported_date,specimen_date,age_group,client_gender,case_acquisition_info,outcome1,outbreak_related,reporting_phu_id,reporting_phu,reporting_phu_address,reporting_phu_city,reporting_phu_postal_code,reporting_phu_website,reporting_phu_latitude,reporting_phu_longitude) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()


csv_file_path = "./data/vaccines_by_age_phu.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY vaccines_by_age_phu(date,phu_id,phu_name,age_group,at_least_one_dose_cumulative,second_dose_cumulative,total_population,percent_at_least_one_dose,percent_fully_vaccinated) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()

csv_file_path = "./data/vaccines_by_age.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY vaccines_by_age(date,age_group,at_least_one_dose_cumulative,second_dose_cumulative,total_population,percent_at_least_one_dose,percent_fully_vaccinated) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()

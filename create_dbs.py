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
from config import database_URI
from models import Base
from sqlalchemy import create_engine

engine = create_engine(database_URI,echo=True)
Base.metadata.create_all(engine)

csv_file_path = "./data/test.csv"
with open(csv_file_path,'r') as file:
    conn = engine.raw_connection()
    cursor = conn.cursor()
    command = 'COPY test(id,field) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    cursor.copy_expert(command,file)
    conn.commit()
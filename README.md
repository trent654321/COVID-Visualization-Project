# COVID-Visualization-Project

To run, this project needs:
a /data/ folder that conains the CSV files shared in the following location in the following location:
https://drive.google.com/drive/folders/1JESe5xOGczc7Pe56AI5ObkAY_AsfsEwL?usp=sharing

A config.py file that contains a variable called "database_URI" to configure SQLAlchemy, such as:
database_URI = "postgresql://postgres:postgres@localhost:5432/Project3"

This project contains:
app.py          a file that contains the flask app
create_dbs.py   a file that contains the code that creates the database tables and populates them with the daata from the csv files
models.py       a file that contains the schema information that is used to create the tables.
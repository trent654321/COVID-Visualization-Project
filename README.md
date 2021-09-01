# COVID-Visualization-Project

To run, this project needs:
a /data/ folder that conains the CSV files shared in the following location in the following location:
https://drive.google.com/drive/folders/1JESe5xOGczc7Pe56AI5ObkAY_AsfsEwL?usp=sharing

A config.py file that contains a variable called "database_URI" to configure SQLAlchemy, such as:
database_URI = "postgresql://postgres:postgres@localhost:5432/Project3"

In addtion,this project contains:
README.md       contains information about the project
app.py          the flask app and routes
create_dbs.py   contains the code that creates the database tables and populates them with the daata from the csv files
models.py       contains the schema information that is used to create the tables.
modify_date-format.py   modifies the date format of one of the downloaded CSV files.
/templates/     contains layout.hmtl that contains the navbar and various templates that extend layout.html
/static/        contains js files that load the visualizations
/static/images  some png files of visualations that are loaded
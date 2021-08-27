#modifies the date field of the given CSV file from MM/DD/YYYY to YYYY-MM-DD
import pandas as pd
csv_file_path = "./data/cases_by_vac_status.csv"
df = pd.read_csv(csv_file_path)
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
df['covid19_cases_vac_unknown'] = df['covid19_cases_vac_unknown'].fillna(0)
df['covid19_cases_vac_unknown'] = df['covid19_cases_vac_unknown'].astype(int)

print(df.head())
df.to_csv(csv_file_path,index=False)
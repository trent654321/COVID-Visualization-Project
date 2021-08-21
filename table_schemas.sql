DROP TABLE covid_cases;

CREATE TABLE covid_cases(
Row_ID                INT PRIMARY KEY,
Accurate_Episode_Date DATE,
Case_Reported_Date    VARCHAR(255),	
Test_Reported_Date    VARCHAR(255), 
Specimen_Date	      VARCHAR(255),
Age_Group             VARCHAR(255),
Client_Gender	      VARCHAR(255),
Case_AcquisitionInfo  VARCHAR(255),
Outcome1	          VARCHAR(255),
Outbreak_Related	  VARCHAR(255),
Reporting_PHU_ID	  INT,
Reporting_PHU         VARCHAR(255),
Reporting_PHU_Address VARCHAR(255),
Reporting_PHU_City    VARCHAR(255),
Reporting_PHU_Postal_Code  VARCHAR(255),
Reporting_PHU_Website	   VARCHAR(255),
Reporting_PHU_Latitude     NUMERIC,
Reporting_PHU_Longitude    NUMERIC
	);

SELECT * 
FROM 
covid_cases;
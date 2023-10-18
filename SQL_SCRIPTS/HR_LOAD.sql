CREATE TABLE DM_HR_CLG (
    CLG_NAME VARCHAR(255),
    RATING DECIMAL(3, 1),
    FEES INT,
    PKG INT,
    STATE VARCHAR(10),
    CLG_ID VARCHAR(10) 
);

COPY DM_HR_CLG(CLG_NAME, RATING, FEES, PKG, STATE, CLG_ID)
FROM 

'/Users/Shriram/Desktop/clg_project/DATA_OUT/HR_CLG/part-00000-eb9ac347-9a42-4162-a055-f75c8acb356f-c000.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE DM_HR_CLG
ADD COLUMN ID SERIAL PRIMARY KEY;


CREATE TABLE DM_KL_CLG (
    CLG_NAME VARCHAR(255),
    RATING DECIMAL(3, 1),
    FEES INT,
    PKG INT,
    STATE VARCHAR(10),
    CLG_ID VARCHAR(10) 
);

COPY DM_KL_CLG(CLG_NAME, RATING, FEES, PKG, STATE, CLG_ID)
FROM 

'/Users/Shriram/Desktop/clg_project/DATA_OUT/KL_CLG/part-00000-3d0b57f0-f3e7-4bcf-ba0d-d6b958833aa9-c000.csv'

DELIMITER ',' CSV HEADER;

ALTER TABLE DM_KL_CLG
ADD COLUMN ID SERIAL PRIMARY KEY;


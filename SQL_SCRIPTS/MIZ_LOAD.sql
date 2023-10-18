CREATE TABLE DM_MIZ_CLG (
    CLG_NAME VARCHAR(255),
    RATING DECIMAL(3, 1),
    FEES INT,
    PKG INT,
    STATE VARCHAR(10),
    CLG_ID VARCHAR(10) 
);

COPY DM_MIZ_CLG(CLG_NAME, RATING, FEES, PKG, STATE, CLG_ID)
FROM 


'/Users/Shriram/Desktop/clg_project/DATA_OUT/MIZ_CLG/part-00000-26a594b5-c053-4fd3-8b69-346061884b74-c000.csv'
DELIMITER ',' CSV HEADER;

ALTER TABLE DM_MIZ_CLG
ADD COLUMN ID SERIAL PRIMARY KEY;

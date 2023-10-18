CREATE TABLE DM_JK_CLG (
    CLG_NAME VARCHAR(255),
    RATING DECIMAL(3, 1),
    FEES INT,
    PKG INT,
    STATE VARCHAR(10),
    CLG_ID VARCHAR(10) 
);

COPY DM_JK_CLG(CLG_NAME, RATING, FEES, PKG, STATE, CLG_ID)
FROM 

'/Users/Shriram/Desktop/clg_project/DATA_OUT/JK_CLG/part-00000-57699efa-9e52-42b0-881b-691d3df45f3a-c000.csv'
DELIMITER ',' CSV HEADER;

ALTER TABLE DM_JK_CLG
ADD COLUMN ID SERIAL PRIMARY KEY;

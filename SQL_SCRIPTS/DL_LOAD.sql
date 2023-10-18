CREATE TABLE DM_DL_CLG (
    CLG_NAME VARCHAR(255),
    RATING DECIMAL(3, 1),
    FEES INT,
    PKG INT,
    STATE VARCHAR(10),
    CLG_ID VARCHAR(10) 
);

COPY DM_DL_CLG(CLG_NAME, RATING, FEES, PKG, STATE, CLG_ID)
FROM 
'/Users/Shriram/Desktop/clg_project/DATA_OUT/DL_CLG/part-00000-cdd245c3-688e-4957-b98e-0ca5119474f9-c000.csv' DELIMITER ',' CSV HEADER;

ALTER TABLE DM_DL_CLG
ADD COLUMN ID SERIAL PRIMARY KEY;

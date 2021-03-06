CREATE WAREHOUSE CUST_WH WAREHOUSE_SIZE =SMALL AUTO_SUSPEND =300 AUTO_RESUME =TRUE;
USE WAREHOUSE CUST_WH;
CREATE DATABASE DE_DB;
CREATE SCHEMA TDW_DW;
CREATE STAGE PUBLIC.DE_STAGE;
USE WAREHOUSE CUST_WH;
USE DE_DB.TDW_DW;
CREATE TABLE CUSTOMER (
CUSTOMER_ID INTEGER, 
GENDER STRING,
AGE INTEGER,
ANNUAL_INCOME DECIMAL,
SPENDING_SCORE  DECIMAL,
INS_TS TIMESTAMP_LTZ,
UPD_TS TIMESTAMP_LTZ
);

CREATE or REPLACE file format CUSTFORMAT
  type = 'CSV'
  field_delimiter = ','
  skip_header = 1;
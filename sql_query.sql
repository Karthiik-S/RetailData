create database RetailSalesData;
use RetailSalesData;

create table Sales_Data_Transictions (
customer_id varchar(255),
trans_date varchar(255),
tran_amount int);

drop table Sales_Data_Transictions

create table Sales_Data_Response (
customer_id varchar(255) primary key,
response int);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Retail_Data_Transactions.csv'
INTO TABLE Sales_Data_Transictions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from Sales_Data_Transictions limit 10;

explain select * from Sales_Data_Transictions where customer_id='CS5295';

Create index idx_id on Sales_Data_Transictions(customer_id);
explain select * from Sales_Data_Transictions where customer_id='CS5295';


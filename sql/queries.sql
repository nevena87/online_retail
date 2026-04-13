create database online_retail;
use online_retail;

CREATE TABLE online_retail (
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate VARCHAR(30),   
    UnitPrice DECIMAL(10,2),
    CustomerID VARCHAR(20),
    Country VARCHAR(50)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/online_retail.csv'
INTO TABLE online_retail
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

ALTER TABLE online_retail ADD CustomerID_clean INT;
UPDATE online_retail
SET CustomerID_clean = NULLIF(CustomerID, '');

ALTER TABLE online_retail ADD InvoiceDate_clean DATETIME;
UPDATE online_retail
SET InvoiceDate_clean = STR_TO_DATE(InvoiceDate, '%m/%d/%Y %H:%i');

SET SQL_SAFE_UPDATES = 0;

DELETE FROM online_retail
WHERE Quantity <= 0
   OR UnitPrice <= 0;

DELETE FROM online_retail
WHERE CustomerID IS NULL;

ALTER TABLE online_retail ADD TotalPrice DECIMAL(10,2);
UPDATE online_retail
SET TotalPrice = Quantity * UnitPrice;

/*1. Ukupan prihod*/
SELECT SUM(TotalPrice) AS total_revenue
FROM online_retail;

/*2. prihod po zemlji*/
SELECT Country, SUM(TotalPrice) AS revenue
FROM online_retail
GROUP BY Country
ORDER BY revenue DESC;

/*3. top proizvodi*/
SELECT Description, SUM(Quantity) AS units_sold
FROM online_retail
GROUP BY Description
ORDER BY units_sold DESC
LIMIT 10;

/*4. top kupci*/
SELECT CustomerID, SUM(TotalPrice) AS lifetime_value
FROM online_retail
GROUP BY CustomerID
ORDER BY lifetime_value DESC
LIMIT 10;

/*5. mesečni trend*/
SELECT 
    DATE_FORMAT(InvoiceDate_clean, '%Y-%m') AS month,
    SUM(TotalPrice) AS revenue
FROM online_retail
GROUP BY month
ORDER BY month;
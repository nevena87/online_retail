-- =========================================
-- 1. BROJ JEDINSTVENIH KUPACA
-- =========================================
-- Koliko ukupno različitih kupaca postoji u sistemu

SELECT 
    COUNT(DISTINCT CustomerID) AS NumberOfCustomers
FROM online_retail;

-- =========================================
-- 2. AVERAGE ORDER VALUE (AOV)
-- =========================================
-- Prosečna vrednost jedne narudžbine (invoice)

SELECT 
    SUM(TotalPrice) / COUNT(DISTINCT InvoiceNo) AS AverageOrderValue
FROM online_retail;

-- =========================================
-- 3. MESEČNI PRIHOD (MONTHLY REVENUE)
-- =========================================
-- Prikazuje ukupnu prodaju po mesecima

SELECT 
    DATE_FORMAT(InvoiceDate_clean, '%Y-%m') AS Month,
    SUM(TotalPrice) AS MonthlyRevenue
FROM online_retail
GROUP BY Month
ORDER BY Month;

-- =========================================
-- 4. CUSTOMER RANKING (RANK WINDOW FUNCTION)
-- =========================================
-- Rangira kupce po ukupnoj potrošnji (Lifetime Value)

SELECT 
    CustomerID,
    SUM(TotalPrice) AS LifetimeValue,
    RANK() OVER (ORDER BY SUM(TotalPrice) DESC) AS CustomerRank
FROM online_retail
GROUP BY CustomerID
ORDER BY LifetimeValue DESC;

-- =========================================
-- 5. TOP 5 KUPACA
-- =========================================
-- Prikazuje 5 najvrednijih kupaca po potrošnji

SELECT 
    CustomerID,
    SUM(TotalPrice) AS LifetimeValue
FROM online_retail
GROUP BY CustomerID
ORDER BY LifetimeValue DESC
LIMIT 5;

-- =========================================
-- 6. UDEO PRIHODA PO KUPCIMA (% CONTRIBUTION)
-- =========================================
-- Koliki procenat ukupnog prihoda donosi svaki kupac

SELECT 
    CustomerID,
    SUM(TotalPrice) AS CustomerRevenue,
    ROUND(
        SUM(TotalPrice) / (SELECT SUM(TotalPrice) FROM online_retail) * 100, 2
    ) AS RevenueSharePercent
FROM online_retail
GROUP BY CustomerID
ORDER BY CustomerRevenue DESC;

-- =========================================
-- 7. KUMULATIVNI PRIHOD (RUNNING TOTAL)
-- =========================================
-- Prikazuje kako se prihod akumulira kroz vreme

SELECT 
    month,
    revenue,
    SUM(revenue) OVER (ORDER BY month) AS cumulative_revenue
FROM (
    SELECT 
        DATE_FORMAT(InvoiceDate_clean, '%Y-%m') AS month,
        SUM(TotalPrice) AS revenue
    FROM online_retail
    GROUP BY month
) t
ORDER BY month;

-- =========================================
-- 8. PERCENT RANK KUPACA
-- =========================================
-- Prikazuje relativnu poziciju kupaca (top %, mid %, low %)

SELECT 
    CustomerID,
    SUM(TotalPrice) AS LifetimeValue,
    RANK() OVER (ORDER BY SUM(TotalPrice) DESC) AS rnk,
    PERCENT_RANK() OVER (ORDER BY SUM(TotalPrice)) AS percentile_rank
FROM online_retail
GROUP BY CustomerID;

-- =========================================
-- 9. MESEČNI RAST (MONTHLY GROWTH)
-- =========================================
-- Poredi mesečni prihod sa prethodnim mesecom

SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
    revenue - LAG(revenue) OVER (ORDER BY month) AS monthly_growth
FROM (
    SELECT 
        DATE_FORMAT(InvoiceDate_clean, '%Y-%m') AS month,
        SUM(TotalPrice) AS revenue
    FROM online_retail
    GROUP BY month
) t;

-- =========================================
-- 10. RANK PO ZEMLJI (PARTITION BY)
-- =========================================
-- Rangira kupce unutar svake države posebno

SELECT 
    Country,
    CustomerID,
    SUM(TotalPrice) AS Revenue,
    RANK() OVER (
        PARTITION BY Country 
        ORDER BY SUM(TotalPrice) DESC
    ) AS CountryRank
FROM online_retail
GROUP BY Country, CustomerID;
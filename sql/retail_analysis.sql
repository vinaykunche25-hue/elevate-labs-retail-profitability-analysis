-- MySQL 8: load cleaned CSV into table retail_transactions first.
SELECT ROUND(SUM(sales),2) total_sales, ROUND(SUM(profit),2) total_profit,
 ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) profit_margin_pct,
 COUNT(DISTINCT order_id) total_orders, COUNT(DISTINCT customer_id) unique_customers
FROM retail_transactions;

SELECT category, sub_category, ROUND(SUM(sales),2) sales, ROUND(SUM(profit),2) profit,
 ROUND(SUM(profit)/NULLIF(SUM(sales),0)*100,2) profit_margin_pct
FROM retail_transactions GROUP BY category,sub_category ORDER BY profit;

SELECT region, SUM(sales) sales, SUM(profit) profit FROM retail_transactions
GROUP BY region ORDER BY sales DESC;

SELECT CASE WHEN discount_pct<.10 THEN '0-9%' WHEN discount_pct<.20 THEN '10-19%'
 WHEN discount_pct<.30 THEN '20-29%' ELSE '30%+' END discount_band,
 COUNT(*) line_items, AVG(profit) avg_profit, SUM(profit) total_profit
FROM retail_transactions GROUP BY discount_band ORDER BY discount_band;

SELECT product_name,category,AVG(inventory_days) avg_inventory_days,SUM(profit) total_profit
FROM retail_transactions GROUP BY product_name,category
HAVING AVG(inventory_days)>=60 ORDER BY avg_inventory_days DESC;

SELECT DATE_FORMAT(order_date,'%Y-%m') month,SUM(sales) sales,SUM(profit) profit
FROM retail_transactions GROUP BY DATE_FORMAT(order_date,'%Y-%m') ORDER BY month;

CREATE OR REPLACE VIEW vw_category_profitability AS
SELECT category,sub_category,SUM(sales) sales,SUM(profit) profit,
 SUM(profit)/NULLIF(SUM(sales),0)*100 profit_margin_pct
FROM retail_transactions GROUP BY category,sub_category;

CREATE INDEX idx_retail_order_date ON retail_transactions(order_date);
CREATE INDEX idx_retail_category_region ON retail_transactions(category,region);

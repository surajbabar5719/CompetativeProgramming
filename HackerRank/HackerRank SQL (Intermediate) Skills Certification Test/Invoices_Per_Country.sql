
/*
    Enter your query below and follow these instructions:
    1. Please append a semicolon ";" at the end of the query
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
*/
SELECT COUNTRY_NAME , CNT , CAST(AVG_TOTAL_PRICE AS DECIMAL(10,6) ) TOTAL 
 FROM (
   SELECT COUNTRY_NAME,COUNT(INVOICE.ID) AS CNT,AVG(TOTAL_PRICE)  AVG_TOTAL_PRICE
   FROM
   COUNTRY
   LEFT JOIN CITY ON ( COUNTRY.ID = CITY.COUNTRY_ID )
   LEFT JOIN CUSTOMER ON ( CITY.ID = CUSTOMER.CITY_ID)
   LEFT JOIN INVOICE  ON ( CUSTOMER.ID = INVOICE.CUSTOMER_ID)
   GROUP BY COUNTRY_NAME ),(SELECT AVG(TOTAL_PRICE) AVG_TOTAL
   FROM INVOICE ) WHERE AVG_TOTAL_PRICE > AVG_TOTAL;

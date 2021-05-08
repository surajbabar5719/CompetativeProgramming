
/*
    Enter your query below and follow these instructions:
    1. Please append a semicolon ";" at the end of the query
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
*/
        select SKU,PRODUCT_NAME from PRODUCT P
        LEFT JOIN INVOICE_ITEM I ON 
        (P.ID = I.PRODUCT_ID) WHERE I.INVOICE_ID IS NULL
        ORDER BY SKU;

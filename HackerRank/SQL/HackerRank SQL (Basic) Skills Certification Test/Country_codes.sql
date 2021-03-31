select customer_id,name, '+'||country_code||phone_number
from customers
inner join country_codes
on customers.country=country_codes.country
order by customer_id;

SELECT customerName, phone, city, country FROM it_step.customers limit 10;
select * from it_step.customers where postalCode > 1370 and salesRepEmployeeNumber > 150 limit 10;
select * from it_step.customers where customerName like '%mini%' limit 10;
select * from it_step.customers where state in ('CA', 'NY') limit 10;
select * from it_step.customers where creditLimit > 10000 limit 10;
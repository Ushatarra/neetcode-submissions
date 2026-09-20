-- Write your query below

select c.name 
From customers c
left join orders t
on c.id=t.customer_id 
where t.customer_id Is Null;
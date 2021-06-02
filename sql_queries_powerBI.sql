-- Top customers

select top 10 c.customerID as customerID, sum(p.price) as total_revenue_per_customer
from customers as c
left join orders as o on c.customerID = o.customerID
left join orderDetails as od on o.orderID = od.orderID
left join products as p on od.productID = p.productID
group by c.customerID
order by total_revenue_per_customer desc


-- Top cities

select top 10 cast(c.city as nvarchar(100)) as city, sum(p.price) as total_revenue_per_city
from customers as c
left join orders as o on c.customerID = o.customerID
left join orderDetails as od on o.orderID = od.orderID
left join products as p on od.productID = p.productID
group by cast(c.city as nvarchar(100))
order by total_revenue_per_city desc

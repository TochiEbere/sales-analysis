# Top customers

select top 10 c.customerID as customerID, sum(p.price) as total_revenue_per_customer
from customers as c
left join orders as o on c.customerID = o.customerID
left join orderDetails as od on o.orderID = od.orderID
left join products as p on od.productID = p.productID
group by c.customerID
order by total_revenue_per_customer desc

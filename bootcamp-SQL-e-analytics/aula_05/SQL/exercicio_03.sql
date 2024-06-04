-- 03.Calcular o valor total que cada cliente pagou até agora, listando os clientes por ordem decrescente de valor total pago.
CREATE VIEW view_total_revenues_per_customer AS
WITH CustomerOrders AS (
    SELECT
        c.company_name,
        od.unit_price,
        od.quantity,
        od.discount
    FROM
        customers c
    INNER JOIN
        orders o ON c.customer_id = o.customer_id
    INNER JOIN
        order_details od ON od.order_id = o.order_id
)
SELECT
    company_name,
    SUM(unit_price * quantity * (1.0 - discount)) AS total
FROM
    CustomerOrders
GROUP BY
    company_name
ORDER BY
    total DESC;

select * from view_total_revenues_per_customer;

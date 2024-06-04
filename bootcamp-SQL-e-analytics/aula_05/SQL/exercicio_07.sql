-- 07. Quais clientes do Reino Unido pagaram mais de 1000 dólares?
CREATE VIEW uk_clients_who_pay_more_than_1000 AS
WITH customer_order_details AS (
    SELECT
        c.contact_name,
        od.unit_price,
        od.quantity,
        od.discount
    FROM
        customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_details od ON od.order_id = o.order_id
    WHERE LOWER(c.country) = 'uk'
)
SELECT
    contact_name,
    ROUND(SUM(unit_price * quantity * (1.0 - discount)), 2) AS payments
FROM
    customer_order_details
GROUP BY
    contact_name
HAVING
    SUM(unit_price * quantity * (1.0 - discount)) > 1000;

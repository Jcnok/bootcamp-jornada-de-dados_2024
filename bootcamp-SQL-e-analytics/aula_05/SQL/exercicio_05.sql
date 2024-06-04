-- 05.Selecionar os clientes dos grupos 3, 4 e 5, ordenados pelo valor total pago
CREATE VIEW clients_to_marketing AS
WITH cliente_order_details AS (
    SELECT
        c.company_name,
        od.unit_price,
        od.quantity,
        od.discount
    FROM
        customers c
    INNER JOIN orders o ON c.customer_id = o.customer_id
    INNER JOIN order_details od ON od.order_id = o.order_id
),
revenue_per_customer AS (
    SELECT
        company_name,
        SUM(unit_price * quantity * (1.0 - discount)) AS total,
        NTILE(5) OVER (ORDER BY SUM(unit_price * quantity * (1.0 - discount)) DESC) AS group_number
    FROM
        cliente_order_details
    GROUP BY
        company_name
)
SELECT
    company_name,
    total,
    group_number
FROM
    revenue_per_customer
WHERE
    group_number >= 3
ORDER BY
    total DESC;

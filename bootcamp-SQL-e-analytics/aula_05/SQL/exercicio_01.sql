-- 01.Qual foi o total de receitas no ano de 1997?
--query 01
EXPLAIN
ANALYZE
SELECT
	SUM(
		(OD.QUANTITY * OD.UNIT_PRICE) * (1.0 - OD.DISCOUNT)
	) AS TOTALREVENUE
FROM
	ORDER_DETAILS AS OD
	JOIN ORDERS AS O ON OD.ORDER_ID = O.ORDER_ID
WHERE
	EXTRACT(
		YEAR
		FROM
			O.ORDER_DATE
	) = 1997;

-- query 02:
SELECT
	SUM(
		(OD.QUANTITY * OD.UNIT_PRICE) * (1.0 - OD.DISCOUNT)
	) TOTAL
FROM
	ORDER_DETAILS AS OD
	INNER JOIN (
		SELECT
			ORDER_ID
		FROM
			ORDERS
		WHERE
			EXTRACT(
				YEAR
				FROM
					ORDER_DATE
			) = '1997'
	) AS O ON O.ORDER_ID = OD.ORDER_ID;

-- Algumas melhorias :
-- Utilizar CTE(common table expression) para melhorar a legibilidade
-- Utilize índices para acelerar as consultas;
-- index
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_order_id ON order_details(order_id);
-- CTE
WITH
	FILTEREDORDERS AS (
		SELECT
			ORDER_ID
		FROM
			ORDERS
		WHERE
			EXTRACT(
				YEAR
				FROM
					ORDER_DATE
			) = 1997
	)

SELECT
	SUM(
		(OD.QUANTITY * OD.UNIT_PRICE) * (1.0 - OD.DISCOUNT)
	) AS Total
FROM
	ORDER_DETAILS AS OD
	inner join FILTEREDORDERS as FO on od.order_id = FO.order_id;

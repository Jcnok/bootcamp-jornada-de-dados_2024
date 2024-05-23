-- Seleciona todos os clientes do México
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY = 'Mexico';

-- Seleciona clientes com ID específico
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CUSTOMER_ID = 'ANATR';

-- Utiliza AND para múltiplos critérios
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY = 'Germany'
	AND CITY = 'Berlin';

-- Utiliza OR para mais de uma cidade
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CITY = 'Berlin'
	OR CITY = 'Aachen';

-- Utiliza NOT para excluir a Alemanha
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY <> 'Germany';

-- Combina AND, OR e NOT
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY = 'Germany'
	AND (
		CITY = 'Berlin'
		OR CITY = 'Aachen'
	);

-- Exclui clientes da Alemanha e EUA
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY <> 'Germany'
	AND COUNTRY <> 'USA';

-- Seleciona todos os produtos com preço menor que 20
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE < 20;

-- Operador > (Maior que)
-- Seleciona todos os produtos com preço maior que 100
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE > 100;

-- Operador <= (Menor ou igual a)
-- Seleciona todos os produtos com preço menor ou igual a 50
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE <= 50;

-- Operador >= (Maior ou igual a)
-- Seleciona todos os produtos com quantidade em estoque maior ou igual a 10
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNITS_IN_STOCK >= 10;

-- Operador <> (Diferente de)
-- Seleciona todos os produtos cujo preço não é 30
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE <> 30;

-- Seleciona todos os produtos com preço entre 50 e 100 (exclusive)
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE >= 50
	AND UNIT_PRICE < 100;

-- Seleciona todos os produtos com preço fora do intervalo 20 a 40
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE < 20
	OR UNIT_PRICE > 40;

-- Nome do cliente começando com "a":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME LIKE 'a%';

-- Nome do cliente terminando com "a":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME ILIKE '%a';

-- Nome do cliente que possui "or" em qualquer posição:
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME ILIKE '%or%';

-- Nome do cliente com "r" na segunda posição:
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME ILIKE '_r%';

-- Nome do cliente que começa com "A" e tem pelo menos 3 caracteres de comprimento:
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME ILIKE 'A_%_%';

-- Nome do contato que começa com "A" e termina com "o":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME ILIKE 'A%o';

-- Nome do cliente que NÃO começa com "a":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CONTACT_NAME NOT ILIKE 'A%';

-- Usando o curinga [charlist] (SQL server)
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CITY ILIKE '[BSP]%';

-- Usando o curinga Similar To (Postgres)
SELECT
	*
FROM
	CUSTOMERS
WHERE
	CITY SIMILAR TO '(B|S|P)%';

-- Usando o MySQL (coitado, tem nada)
SELECT
	*
FROM
	CUSTOMERS
WHERE
	(
		CITY LIKE 'B%'
		OR CITY LIKE 'S%'
		OR CITY LIKE 'P%'
	);

-- ADMINOperador IN
-- localizado na "Alemanha", "França" ou "Reino Unido":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY IN ('Germany', 'France', 'UK');

-- NÃO localizado na "Alemanha", "França" ou "Reino Unido":
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY NOT IN ('Germany', 'France', 'UK');

-- Só para dar um gostinho de uma subqueyr... Seleciona todos os clientes que são dos mesmos países que os fornecedores:
SELECT
	*
FROM
	CUSTOMERS
WHERE
	COUNTRY IN (
		SELECT
			COUNTRY
		FROM
			SUPPLIERS
	);

-- Exemplo com BETWEEN
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE BETWEEN 10 AND 20;

-- Exemplo com NOT BETWEEN
SELECT
	*
FROM
	PRODUCTS
WHERE
	UNIT_PRICE NOT BETWEEN 10 AND 20;

-- Seleciona todos os produtos com preço ENTRE 10 e 20. Adicionalmente, não mostra produtos com CategoryID de 1, 2 ou 3:
SELECT
	*
FROM
	PRODUCTS
WHERE
	(UNIT_PRICE BETWEEN 10 AND 20)
	AND CATEGORY_ID NOT IN (1, 2, 3);

--selects todos os produtos entre 'Carnarvon Tigers' e 'Mozzarella di Giovanni':
SELECT
	*
FROM
	PRODUCTS
WHERE
	PRODUCT_NAME BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'
ORDER BY
	PRODUCT_NAME;

--Selecione todas as ordens BETWEEN '04-July-1996' e '09-July-1996':
SELECT
	*
FROM
	ORDERS
WHERE
	ORDER_DATE BETWEEN '07/04/1996' AND '07/09/1996';

-- Exemplo de MIN()
SELECT
	MIN(UNIT_PRICE) AS PRECO_MINIMO
FROM
	PRODUCTS;

-- Exemplo de MAX()
SELECT
	MAX(UNIT_PRICE) AS PRECO_MAXIMO
FROM
	PRODUCTS;

-- Exemplo de COUNT()
SELECT
	COUNT(*) AS TOTAL_DE_PRODUTOS
FROM
	PRODUCTS;

-- Exemplo de AVG()
SELECT
	AVG(UNIT_PRICE) AS PRECO_MEDIO
FROM
	PRODUCTS;

-- Exemplo de SUM()
SELECT
	SUM(QUANTITY) AS QUANTIDADE_TOTAL_DE_ORDER_DETAILS
FROM
	ORDER_DETAILS;

-- Exemplo de MIN() com GROUP BY
-- Calcula o menor preço unitário de produtos em cada categoria
SELECT
	CATEGORY_ID,
	MIN(UNIT_PRICE) AS PRECO_MINIMO
FROM
	PRODUCTS
GROUP BY
	CATEGORY_ID;

-- Exemplo de MAX() com GROUP BY
-- Calcula o maior preço unitário de produtos em cada categoria
SELECT
	CATEGORY_ID,
	MAX(UNIT_PRICE) AS PRECO_MAXIMO
FROM
	PRODUCTS
GROUP BY
	CATEGORY_ID;

-- Exemplo de COUNT() com GROUP BY
-- Conta o número total de produtos em cada categoria
SELECT
	CATEGORY_ID,
	COUNT(*) AS TOTAL_DE_PRODUTOS
FROM
	PRODUCTS
GROUP BY
	CATEGORY_ID;

-- Exemplo de AVG() com GROUP BY
-- Calcula o preço médio unitário de produtos em cada categoria
SELECT
	CATEGORY_ID,
	AVG(UNIT_PRICE) AS PRECO_MEDIO
FROM
	PRODUCTS
GROUP BY
	CATEGORY_ID;

-- Exemplo de SUM() com GROUP BY
-- Calcula a quantidade total de produtos pedidos por pedido
SELECT
	ORDER_ID,
	SUM(QUANTITY) AS QUANTIDADE_TOTAL_POR_PEDIDO
FROM
	ORDER_DETAILS
GROUP BY
	ORDER_ID;

-- Desafio
-- Obter todas as colunas das tabelas Clientes, Pedidos e Fornecedores
SELECT
	*
FROM
	CUSTOMERS;

SELECT
	*
FROM
	ORDERS;

SELECT
	*
FROM
	SUPPLIERS;

-- Obter todos os Clientes em ordem alfabética por país e nome
SELECT
	*
FROM
	CUSTOMERS
ORDER BY
	COUNTRY,
	CONTACT_NAME;

-- Obter os 5 pedidos mais antigos
SELECT
	*
FROM
	ORDERS
ORDER BY
	ORDER_DATE
LIMIT
	5;

-- Obter a contagem de todos os Pedidos feitos durante 1997
SELECT
	COUNT(*) AS "Number of Orders During 1997"
FROM
	ORDERS
WHERE
	ORDER_DATE BETWEEN '1997-1-1' AND '1997-12-31';

-- Obter os nomes de todas as pessoas de contato onde a pessoa é um gerente, em ordem alfabética
SELECT
	CONTACT_NAME
FROM
	CUSTOMERS
WHERE
	CONTACT_TITLE LIKE '%Manager%'
ORDER BY
	CONTACT_NAME;

-- Obter todos os pedidos feitos em 19 de maio de 1997
SELECT
	*
FROM
	ORDERS
WHERE
	ORDER_DATE = '1997-05-19';

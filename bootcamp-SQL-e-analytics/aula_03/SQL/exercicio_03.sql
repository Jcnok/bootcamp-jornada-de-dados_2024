-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT c.city AS cidade,
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes,
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios
FROM employees e
RIGHT JOIN customers c ON e.city = c.city
GROUP BY c.city
ORDER BY cidade;

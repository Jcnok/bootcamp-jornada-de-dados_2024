-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT e.city AS cidade,
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios,
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e
LEFT JOIN customers c ON e.city = c.city
GROUP BY e.city
ORDER BY cidade;

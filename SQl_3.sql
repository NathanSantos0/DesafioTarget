SELECT MIN(valor) AS menor_faturamento
FROM faturamento
WHERE valor > 0;

SELECT MAX(valor) AS maior_faturamento
FROM faturamento
WHERE valor > 0;

	
SELECT COUNT(*) AS dias_acima_media
FROM faturamento
WHERE valor > 
(SELECT AVG(valor)
 FROM faturamento
 WHERE valor >0)

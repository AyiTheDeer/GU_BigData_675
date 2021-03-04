-- Операторы
-- Task 3
SELECT * FROM storehouses_products
ORDER BY case `value` WHEN 0 THEN 0 
ELSE 1 END DESC, id DESC;
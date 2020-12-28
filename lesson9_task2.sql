/*
Создайте представление, которое выводит название name товарной позиции из таблицы products
и соответствующее название каталога name из таблицы catalogs.
*/

Create view task2 as
SELECT
	p.name as product_name,
    c.name as catalog_name
FROM shop.products p
left join shop.catalogs c on p.catalog_id = c.id;
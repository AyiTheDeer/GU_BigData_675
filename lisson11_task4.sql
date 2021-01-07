/*
Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.
*/
use products
db.products.insert({
"name": "proc",
"description": "processor",
"price": "1000.00",
"catalog_id": "Процессоры",
"created_at": new Date(),
"updated_at": new Date()
})

use catalogs
db.catalogs.insertMany([
{"name": "Процессоры"},
{"name": "Мат.платы"},
{"name": "Видеокарты"}
])
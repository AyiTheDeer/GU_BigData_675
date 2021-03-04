select
p.name, c.name
from
catalogs as c
join
products as p
on
c.id = p.catalog_id;
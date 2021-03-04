/*
Представление на основе запроса
*/

CREATE VIEW popular_categories AS
SELECT
	u.`id`,
    p.`nickname`,
    p.`gender`,
    
    (YEAR(CURRENT_DATE)-YEAR(p.`birthday`))-(RIGHT(CURRENT_DATE,5)<RIGHT(p.`birthday`,5)) AS `age`,
  
  (SELECT c.`name`
	FROM ph.`views` as vw
	LEFT JOIN
		ph.`video` as v ON vw.`video_id` = v.id
	LEFT JOIN
		ph.`categories` as c ON v.`categories_id` = c.`id`
	WHERE vw.`users_id` = u.`id`
	Group by c.`name`
	order by count(c.`name`) desc
	limit 1) as `most_popular_category`
    
FROM ph.`users` as u
LEFT JOIN
	ph.`user_types` as ut ON u.`user_types_id` = ut.`id`
LEFT JOIN
	ph.`profiles` as p ON u.`id` = p.`users_id`;
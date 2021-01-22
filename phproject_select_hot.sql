/*
Селект, который возвращает топ-горячих видео. По задумке был за последние 3 дня, но автозаполненные данные этого не позволяют сделать, поэтому пример на последних 3 годах.
*/

SELECT
	vd.`id`, 
    vd.`name`,
    vd.`categories_id`,
    vd.`duration` as `video_duration`,
    SEC_TO_TIME(SUM(TIME_TO_SEC(vw.`duration`))) as `sum_views_duration`,
    (
    ((SELECT count(*) FROM ph.`likes` where `video_id` = vd.`id`)
    +
    (SELECT count(*) FROM ph.`comments` where `video_id` = vd.`id`))
    /
    count(vd.`id`)
    ) as `rate`
FROM
	ph.`video` as vd
LEFT JOIN
	ph.`views` as vw ON vd.`id` = vw.`video_id`
WHERE
	vd.`status` = 1
AND
	`uploaded_at` >= DATE_ADD(CURDATE(), INTERVAL -3 YEAR)
GROUP BY
	vd.`id`
ORDER BY `rate` DESC;
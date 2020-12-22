SELECT `gender`, `total_likes` FROM (
		SELECT "M" AS `gender`, COUNT(*) AS `total_likes` FROM `likes` WHERE `users_id` IN (SELECT `users_id` FROM `profiles` WHERE `gender`='m')
	UNION
		SELECT "F" AS `gender`, COUNT(*) AS `total_likes` FROM `likes` WHERE `users_id` IN (SELECT `users_id` FROM `profiles` WHERE `gender`='f')
	UNION 
        	SELECT "X" AS `gender`, COUNT(*) AS `total_likes` FROM `likes` WHERE `users_id` IN (SELECT `users_id` FROM `profiles` WHERE `gender`='x')
) AS `total`
ORDER BY `total_likes` DESC LIMIT 1;
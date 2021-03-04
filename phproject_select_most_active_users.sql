select
	u.`id`,
    ((l.`likes count` + c.`comments count`) / v.`views count`) as `user score`
from
	ph.`users` u
left join
	(select `users_id`, count(*) as `views count` from ph.`views` group by `users_id`) v ON u.`id` = v.`users_id`
left join
	(select `users_id`, count(*) as `likes count` from ph.`likes` group by `users_id`) l ON u.`id` = l.`users_id`
left join
	(select `users_id`, count(*) as `comments count` from ph.`comments` group by `users_id`) c ON u.`id` = c.`users_id`
order by `user score` desc
;
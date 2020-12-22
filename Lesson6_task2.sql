SELECT
	from_users_id as 'samyi obschitelniy',
	count(from_users_id) as 'N messages'
FROM vk.messages
	where to_users_id = 6
	and (from_users_id in (SELECT from_users_id FROM vk.friend_requests WHERE `status` = 1 AND (from_users_id = to_users_id OR to_users_id = to_users_id))
	or from_users_id in (SELECT to_users_id FROM vk.friend_requests WHERE `status` = 1 AND (from_users_id = to_users_id OR to_users_id = to_users_id)))
group by from_users_id
;
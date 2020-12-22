SELECT
  users_id,
  (
  (select count(*) FROM vk.likes where messages_id in (SELECT id FROM vk.messages where from_users_id = vk.profiles.users_id))
  +
  (select count(*) FROM vk.likes where posts_id in (SELECT id FROM vk.posts where users_id = vk.profiles.users_id))
  +
  (select count(*) FROM vk.likes where media_id in (SELECT id FROM vk.media where users_id = vk.profiles.users_id))
  ) as total_likes
  
FROM `profiles`
  order by TIMESTAMPDIFF(YEAR, birthday, NOW()), total_likes desc
  limit 10
  ;
  
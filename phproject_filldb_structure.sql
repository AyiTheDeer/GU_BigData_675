--
-- Table structure for table `albums`
--

DROP TABLE IF EXISTS `albums`;
CREATE TABLE `albums` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `users_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_albums_users1_idx` (`users_id`),
  CONSTRAINT `fk_albums_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `albums_content`
--

DROP TABLE IF EXISTS `albums_content`;
CREATE TABLE `albums_content` (
  `albums_id` int unsigned NOT NULL,
  `media_id` int unsigned NOT NULL,
  KEY `fk_albums_content_albums1_idx` (`albums_id`),
  KEY `fk_albums_content_media1_idx` (`media_id`),
  CONSTRAINT `fk_albums_content_albums1` FOREIGN KEY (`albums_id`) REFERENCES `albums` (`id`),
  CONSTRAINT `fk_albums_content_media1` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments` (
  `text` text,
  `users_id` int unsigned NOT NULL,
  `video_id` int unsigned DEFAULT NULL,
  `media_id` int unsigned DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`users_id`),
  KEY `fk_comments_video1_idx` (`video_id`),
  KEY `fk_comments_media1_idx` (`media_id`),
  CONSTRAINT `fk_comments_media1` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`),
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_comments_video1` FOREIGN KEY (`video_id`) REFERENCES `video` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
CREATE TABLE `likes` (
  `users_id` int unsigned NOT NULL,
  `video_id` int unsigned DEFAULT NULL,
  `media_id` int unsigned DEFAULT NULL,
  KEY `fk_likes_users1_idx` (`users_id`),
  KEY `fk_likes_video1_idx` (`video_id`),
  KEY `fk_likes_media1_idx` (`media_id`),
  CONSTRAINT `fk_likes_media1` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`),
  CONSTRAINT `fk_likes_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_likes_video1` FOREIGN KEY (`video_id`) REFERENCES `video` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
CREATE TABLE `media` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(45) DEFAULT NULL,
  `name` varchar(45) NOT NULL,
  `size` bigint NOT NULL DEFAULT '0',
  `uploaded_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0 - non active, 1 - active',
  `metadata` longtext,
  `users_id` int unsigned NOT NULL,
  `media_types_id` int unsigned NOT NULL,
  `categories_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_media_users1_idx` (`users_id`),
  KEY `fk_media_media_types1_idx` (`media_types_id`),
  KEY `fk_media_categories1_idx` (`categories_id`),
  CONSTRAINT `fk_media_categories1` FOREIGN KEY (`categories_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_media_media_types1` FOREIGN KEY (`media_types_id`) REFERENCES `media_types` (`id`),
  CONSTRAINT `fk_media_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `media_types`
--

DROP TABLE IF EXISTS `media_types`;
CREATE TABLE `media_types` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `playlists`
--

DROP TABLE IF EXISTS `playlists`;
CREATE TABLE `playlists` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0 - private, 1 - public',
  `name` varchar(45) NOT NULL,
  `users_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_playlists_users1_idx` (`users_id`),
  CONSTRAINT `fk_playlists_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `playlists_content`
--

DROP TABLE IF EXISTS `playlists_content`;
CREATE TABLE `playlists_content` (
  `video_id` int unsigned NOT NULL,
  `playlists_id` int unsigned NOT NULL,
  KEY `fk_playlists_content_video1_idx` (`video_id`),
  KEY `fk_playlists_content_playlists1_idx` (`playlists_id`),
  CONSTRAINT `fk_playlists_content_playlists1` FOREIGN KEY (`playlists_id`) REFERENCES `playlists` (`id`),
  CONSTRAINT `fk_playlists_content_video1` FOREIGN KEY (`video_id`) REFERENCES `video` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
CREATE TABLE `profiles` (
  `nickname` varchar(45) NOT NULL,
  `url` varchar(45) DEFAULT NULL,
  `gender` enum('m','f','x') NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `birthday` date NOT NULL,
  `users_id` int unsigned NOT NULL,
  `avatar` int unsigned NOT NULL,
  PRIMARY KEY (`users_id`),
  KEY `fk_profiles_users1_idx` (`users_id`) /*!80000 INVISIBLE */,
  KEY `fk_profiles_media1_idx` (`avatar`),
  CONSTRAINT `fk_profiles_media1` FOREIGN KEY (`avatar`) REFERENCES `media` (`id`),
  CONSTRAINT `fk_profiles_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `user_types`
--

DROP TABLE IF EXISTS `user_types`;
CREATE TABLE `user_types` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(90) NOT NULL,
  `lastname` varchar(90) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password_hash` char(65) DEFAULT NULL,
  `user_types_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_users_user_types1_idx` (`user_types_id`),
  CONSTRAINT `fk_users_user_types1` FOREIGN KEY (`user_types_id`) REFERENCES `user_types` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `video`
--

DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `duration` time NOT NULL,
  `uploaded_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0 - non active, 1 - active',
  `url` varchar(45) DEFAULT NULL,
  `size` bigint NOT NULL DEFAULT '0',
  `metadata` longtext,
  `categories_id` int unsigned NOT NULL,
  `users_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_video_categories_idx` (`categories_id`),
  KEY `fk_video_users1_idx` (`users_id`),
  CONSTRAINT `fk_video_categories` FOREIGN KEY (`categories_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_video_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB;

--
-- Table structure for table `views`
--

DROP TABLE IF EXISTS `views`;
CREATE TABLE `views` (
  `duration` time DEFAULT NULL,
  `users_id` int unsigned DEFAULT NULL,
  `video_id` int unsigned DEFAULT NULL,
  `media_id` int unsigned DEFAULT NULL,
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `fk_views_users1_idx` (`users_id`),
  KEY `fk_views_video1_idx` (`video_id`),
  KEY `fk_views_media1_idx` (`media_id`),
  CONSTRAINT `fk_views_media1` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`),
  CONSTRAINT `fk_views_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_views_video1` FOREIGN KEY (`video_id`) REFERENCES `video` (`id`)
) ENGINE=InnoDB;

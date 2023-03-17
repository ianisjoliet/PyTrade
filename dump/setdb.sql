CREATE DATABASE IF NOT EXISTS `platform` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `platform`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `public_key` varchar(64) DEFAULT NULL,
    `private_key` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `trades`;
CREATE TABLE `trades` (
    `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `symbol` varchar(64) DEFAULT NULL,
    `createdTime` varchar(255) DEFAULT NULL,
    `closedPnl` varchar(64) DEFAULT NULL,
    `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE trades
ADD CONSTRAINT FK_user_id
FOREIGN KEY (userId) REFERENCES users(id)
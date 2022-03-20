-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        8.0.18 - MySQL Community Server - GPL
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 help_system 的数据库结构
CREATE
DATABASE IF NOT EXISTS `help_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE
`help_system`;

-- 导出  表 help_system.chat_data 结构
CREATE TABLE IF NOT EXISTS `chat_data`
(
    `chat_id` int
(
    11
) NOT NULL AUTO_INCREMENT,
    `chat_hash` varchar
(
    50
) NOT NULL COMMENT '两个id的哈希值',
    `chat_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '消息发送时间',
    `chat_content` varchar
(
    500
) NOT NULL COMMENT '消息内容',
    `chat_state` int
(
    11
) NOT NULL DEFAULT '0' COMMENT '消息类型',
    PRIMARY KEY
(
    `chat_id`
)
    ) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE =utf8mb4_0900_ai_ci;

-- 正在导出表  help_system.chat_data 的数据：~8 rows (大约)
DELETE
FROM `chat_data`;
/*!40000 ALTER TABLE `chat_data` DISABLE KEYS */;
INSERT INTO `chat_data` (`chat_id`, `chat_hash`, `chat_date`, `chat_content`, `chat_state`)
VALUES (1, '309382104222466745', '2020-11-25 14:49:02', '开始聊天吧 请文明交流', 0),
       (2, '-1197975917502471657', '2020-11-25 14:51:16', '开始聊天吧 请文明交流', 0),
       (3, '1254098884734335344', '2020-11-25 14:53:00', '开始聊天吧 请文明交流', 0),
       (4, '7463010604242136000', '2020-11-25 14:53:20', '开始聊天吧 请文明交流', 0),
       (5, '7463010604242136000', '2020-11-25 14:54:04', '开始聊天吧 请文明交流', 0),
       (6, '-7939842951811972479', '2020-11-25 14:54:21', '开始聊天吧 请文明交流', 0),
       (7, '7463010604242136000', '2020-11-25 14:58:49', '开始聊天吧 请文明交流', 0),
       (8, '7463010604242136000', '2020-11-25 17:21:32', '开始聊天吧 请文明交流', 0),
       (9, '4318044751380913723', '2020-11-29 21:39:50', '开始聊天吧 请文明交流', 0),
       (10, '6584134058751984560', '2021-02-06 14:03:41', '开始聊天吧 请文明交流', 0),
       (11, '4799502730327522132', '2021-02-06 17:54:36', '开始聊天吧 请文明交流', 0),
       (12, '-5375388338832924572', '2021-02-08 11:49:41', '开始聊天吧 请文明交流', 0);
/*!40000 ALTER TABLE `chat_data` ENABLE KEYS */;

-- 导出  表 help_system.info_data 结构
CREATE TABLE IF NOT EXISTS `info_data`
(
    `indo_id` int
(
    11
) NOT NULL AUTO_INCREMENT,
    `info_title` varchar
(
    100
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
    `info_content` varchar
(
    1000
) NOT NULL,
    `info_image` varchar
(
    100
) NOT NULL,
    `info_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `info_state` int
(
    11
) NOT NULL DEFAULT '0',
    `info_user_id` int
(
    11
) DEFAULT NULL,
    PRIMARY KEY
(
    `indo_id`
)
    ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE =utf8mb4_0900_ai_ci;

-- 正在导出表  help_system.info_data 的数据：~8 rows (大约)
DELETE
FROM `info_data`;
/*!40000 ALTER TABLE `info_data` DISABLE KEYS */;
INSERT INTO `info_data` (`indo_id`, `info_title`, `info_content`, `info_image`, `info_date`, `info_state`,
                         `info_user_id`)
VALUES (1, '找小姐姐', '找一个小姐姐',
        'https://dss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=29365196,3995193101&fm=26&gp=0.jpg',
        '2020-11-23 14:12:30', 0, 1),
       (2, '卖一个热水壶', '我有一个热水壶，现在不想要了，有人要的话私聊我',
        'https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2950500849,3824539074&fm=26&gp=0.jpg',
        '2020-11-23 15:13:57', 0, 1),
       (3, '出一本《马原》', '我有一本闲置的《马原》书籍，我想处理了，十块钱',
        'https://dss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2551009082,4089355882&fm=111&gp=0.jpg',
        '2020-11-23 15:31:49', 0, 2),
       (4, '交个朋友啦', '我是XX，我来自XX，我想认识大家',
        'https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1274453940,1450729366&fm=26&gp=0.jpg',
        '2020-11-23 15:31:49', 0, 3),
       (5, '出售', '壁纸', 'static/user_images/2021020617194409.JPG', '2021-02-06 17:19:45', 0, 2),
       (6, '测试贴', '测试帖子', 'static/user_images/20210206172055010.JPG', '2021-02-06 17:20:56', 0, 2),
       (7, '超级管理员', '测试贴', 'static/user_images/2021020617231703.jpg', '2021-02-06 17:23:18', 0, 1888),
       (8, '超级管理员', '测试', '../static/user_images/2021020617511745.jpg', '2021-02-06 17:51:17', 0, 1888),
       (9, '走过山河，看遍星河', '走过无数山河，\r\n看遍万千星河', '../static/user_images/2021020617542525.png', '2021-02-06 17:54:25', 0,
        1888),
       (10, '我所谓的重视在你眼中一文不值', '原来，我以为的只是我以为\r\n我所谓的重视在你眼中是那么的不堪，那么的一文不值！', '../static/user_images/2021020811474332.png',
        '2021-02-08 11:47:43', 0, 1888);
/*!40000 ALTER TABLE `info_data` ENABLE KEYS */;

-- 导出  表 help_system.users_data 结构
CREATE TABLE IF NOT EXISTS `users_data`
(
    `user_id` int
(
    11
) NOT NULL AUTO_INCREMENT,
    `user_name` varchar
(
    100
) NOT NULL,
    `user_reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_head_image` varchar
(
    100
) NOT NULL,
    PRIMARY KEY
(
    `user_id`
)
    ) ENGINE=InnoDB AUTO_INCREMENT=1889 DEFAULT CHARSET=utf8mb4 COLLATE =utf8mb4_0900_ai_ci;

-- 正在导出表  help_system.users_data 的数据：~2 rows (大约)
DELETE
FROM `users_data`;
/*!40000 ALTER TABLE `users_data` DISABLE KEYS */;
INSERT INTO `users_data` (`user_id`, `user_name`, `user_reg_date`, `user_head_image`)
VALUES (1, '开心每一刻', '2020-11-23 14:24:17',
        'https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3767892414,3870870638&fm=26&gp=0.jpg'),
       (2, '信管三骚', '2020-11-23 15:32:30',
        'https://dss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2069542074,3354686813&fm=26&gp=0.jpg'),
       (3, '小宝', '2020-11-23 16:32:07',
        'https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1274453940,1450729366&fm=26&gp=0.jpg'),
       (1888, '超级管理员', '2021-02-06 17:22:47', '../static/images/index_user.png');
/*!40000 ALTER TABLE `users_data` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

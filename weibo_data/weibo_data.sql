-- MySQL dump 10.19  Distrib 10.3.34-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: weibo_data
-- ------------------------------------------------------
-- Server version	10.3.34-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `hot_search_all`
--

DROP TABLE IF EXISTS `hot_search_all`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hot_search_all` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flag_desc` varchar(20) DEFAULT NULL COMMENT '标记描述',
  `realpos` int(11) DEFAULT NULL COMMENT '排序位置',
  `word` varchar(200) DEFAULT NULL COMMENT '热搜词',
  `subject_querys` varchar(50) DEFAULT NULL COMMENT '主题分类',
  `extension` int(11) DEFAULT NULL COMMENT '推广标志',
  `fun_word` int(11) DEFAULT NULL COMMENT '字数限制',
  `label_name` varchar(10) DEFAULT NULL COMMENT '标签名称',
  `onboard_time` bigint(20) DEFAULT NULL COMMENT '上榜时间',
  `expand` int(11) DEFAULT NULL COMMENT '是否展开',
  `star_word` int(11) DEFAULT NULL COMMENT '是否星标',
  `small_icon_desc` varchar(10) DEFAULT NULL COMMENT '小图标描述',
  `topic_flag` int(11) DEFAULT NULL COMMENT '话题标志',
  `num` bigint(20) DEFAULT NULL COMMENT '搜索次数',
  `word_scheme` varchar(255) DEFAULT NULL COMMENT '热搜词链接',
  `emoticon` varchar(10) DEFAULT NULL COMMENT '表情符号',
  `flag` int(11) DEFAULT NULL COMMENT '标记',
  `star_name` varchar(255) DEFAULT NULL COMMENT '明星名字',
  `raw_hot` bigint(20) DEFAULT NULL COMMENT '原始搜索次数',
  `is_hot` int(11) DEFAULT NULL COMMENT '是否热门',
  `channel_type` varchar(20) DEFAULT NULL COMMENT '频道类型',
  `category` varchar(20) DEFAULT NULL COMMENT '分类名称',
  `subject_label` varchar(255) DEFAULT NULL COMMENT '主题标签',
  `ad_info` text DEFAULT NULL COMMENT '广告信息',
  `note` varchar(255) DEFAULT NULL COMMENT '备注',
  `icon_desc_color` varchar(10) DEFAULT NULL COMMENT '图标描述颜色',
  `icon_desc` varchar(10) DEFAULT NULL COMMENT '图标描述',
  `small_icon_desc_color` varchar(10) DEFAULT NULL COMMENT '小图标描述颜色',
  `rank` int(11) DEFAULT NULL COMMENT '热搜排名',
  `create_time` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `hot_search_all_word_IDX` (`word`) USING BTREE,
  KEY `hot_search_all_word_IDX1` (`category`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=780757 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='热门搜索表';
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-21 10:08:09

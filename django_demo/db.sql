CREATE TABLE `t_student_info`(
  `c_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `c_name` varchar(128) NOT NULL,
  `c_score` int(10) NOT NULL,
  `c_modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `c_create_time` datetime NOT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `name` (`c_name`),
  KEY `modify_time` (`c_modify_time`),
  KEY `create_time` (`c_create_time`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
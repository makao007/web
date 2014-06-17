create table item (
	id int primary key auto_increment,
	title varchar(256),
	image varchar(1024),
	summary varchar(1024),
	content text,
	url varchar(1024),
	show_time varchar(100),
	fetch_time datetime,
	update_time datetime
) default character set utf8;
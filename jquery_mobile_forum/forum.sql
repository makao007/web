

database schema

create table f_category ( 
	id int primary key,
	name varchar(200) not null,
	order int default 1,
	create_date datetime,
	update_date datetime,
	is_delete char(1) default 0
)

// sort by order,create_date desc


create table f_article ( 
	id int primary key,
	title varchar(1024) not null,
	content text,
	author_id varchar(200),
	author_name varchar(200),
	create_date datetime,
	update_date datetime,
	update_author varchar(200),
	
	like_amount int,
	reply_amount int,
	
	is_top char(1) default 0,

	is_delete char(1) default 0
)


create table f_reply (
	id int primary key,
	author_id varchar(200),
	author_name varchar(200),
	content varchar(8000),
	parent_replay_id int,
	create_date datetime,
	update_date datetime,
	update_author varchar(200),
	
	is_delete char(1) default 0
)
	




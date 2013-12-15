

create table projects (id int primary key auto-increment, name char(100) not null, parent_id id not null foreign key, create_date timestamp default now());



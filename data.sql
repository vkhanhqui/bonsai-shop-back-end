create database bonsai_db;

drop database bonsai_db;

use bonsai_db;

insert into roles(role_name) values('Admin');
insert into roles(role_name) values('Staff');
insert into roles(role_name) values('Customer');
select * from roles;

insert into users(username, hashed_password, email, birthday, first_name, last_name, role_id, created_at)
	values('string', '$2b$12$nEVAr6aZjD4zOmx98e.2FOY4EAZCPgM2OGkwsK6jt8Uy9OrdTtCUa',
		'user@example.com', '2022-02-27', 'string', 'string', 2, '2022-02-27 09:23:39');
select * from users;


insert into categories(category_name, created_at)
	values('string', '2022-02-27 09:23:39');
select * from categories;

insert into products(product_name, product_price, category_id, created_at)
	values('string', 1, 1, '2022-02-27 09:23:39');
select * from products;

insert into addresses(city, district, full_address, user_id, created_at)
	values('string', 'string', 'string', 1, '2022-02-27 09:23:39');
select * from addresses;

insert into bills(customer_id, address_id, bill_status, created_at)
	values(1, 1, 'new', '2022-02-27 09:23:39');
select * from bills;

insert into billmanagements(product_id, bill_id, number_product, created_at)
	values(1, 1, 10, '2022-02-27 09:23:39');
select * from billmanagements;

create database bonsai_db;

drop database bonsai_db;

use bonsai_db;


-- role
insert into roles(role_name) values('Admin');
insert into roles(role_name) values('Staff');
insert into roles(role_name) values('Customer');

-- user
insert into users(username, hashed_password, email, birthday, first_name, last_name, role_id, created_at)
	values('string', '$2b$12$nEVAr6aZjD4zOmx98e.2FOY4EAZCPgM2OGkwsK6jt8Uy9OrdTtCUa',
		'user@example.com', '2022-02-27', 'string', 'string', 1, '2022-02-27 09:23:39');

-- category
insert into categories(category_name, created_at)
	values('string', '2022-02-27 09:23:39');

-- product
insert into products(product_name, product_price, category_id, created_at)
	values('string', 1, 1, '2022-02-27 09:23:39');

-- images
insert into images(image_path, product_id, created_at)
	values('media/products/1/images/25wpvBXVCrN2Pb8bcjN4gaQ5GTy.jpeg', 1, '2022-02-27 09:23:39');
insert into images(image_path, product_id, created_at)
	values('media/products/1/images/25wpv4MihEa0ktjoXVe010Hmg1O.jpeg', 1, '2022-02-27 09:23:39');

-- addresses
insert into addresses(city, district, full_address, phone_number, user_id, created_at)
	values('string', 'string', 'string', 'string', 1, '2022-02-27 09:23:39');

-- queries
select * from billmanagements;
select * from addresses;
select * from users;
select * from categories;
select * from bills;
select * from images;
select * from roles;
select * from products;

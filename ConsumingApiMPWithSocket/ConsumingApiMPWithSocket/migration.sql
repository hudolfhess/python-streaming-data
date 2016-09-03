create table customers (
	`id` INT(11) AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(55) not null,
	`email` VARCHAR(55) not null,
	`last_update` DATETIME not null,
	`created` DATETIME not null
);

create table products (
	`id` INT(11) AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(55) not null,
	`description` TEXT not null,
	`price` DECIMAL(10, 2) not null,
	`last_update` DATETIME not null,
	`created` DATETIME not null
);

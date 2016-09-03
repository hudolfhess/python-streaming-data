# Project Name

TODO: Write a project description

## Installation

TODO: Describe the installation process

## Usage

### Example database

```sql
create database streaming_test;

use streaming_test;

drop table products;

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

insert into customers values (null, 'Fulano', 'fulano@email', NOW(), NOW());
insert into customers values (null, 'Ciclano', 'ciclano@email', NOW(), NOW());
insert into customers values (null, 'Joao', 'joao@email', NOW(), NOW());
insert into customers values (null, 'Jose', 'jose@email', NOW(), NOW());
insert into customers values (null, 'Maria', 'maria@email', NOW(), NOW());
insert into customers values (null, 'Joana', 'joana@email', NOW(), NOW());

insert into products values (null, 'Soap', 'Its a soap', 10.32, NOW(), NOW());
insert into products values (null, 'TV', 'Its a TV', 1023.32, NOW(), NOW());
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license

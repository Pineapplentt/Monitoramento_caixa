create database databaseKashPlus;
use databaseKashPlus;

create table usuario (
	idUsuario int auto_increment primary key,
    email varchar(100),
    senha varchar(100)
);
insert into usuario values (null, 'vinicius@gmail.com', '1234');

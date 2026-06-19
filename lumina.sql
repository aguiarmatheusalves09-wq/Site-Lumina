create database lumina;
use lumina;

create table usuario(senha varchar(100) not null Primary key,
					 email varchar(100) not null,
                     nome varchar(100) not null,
                     data_nasc date not null);
create database lumina;
use lumina;

create table usuario(email varchar(100) not null Primary key,
					 senha varchar(100) not null ,
                     nome varchar(100) not null,
                     data_nasc date not null),
                     nickName varchar(100)not null);s
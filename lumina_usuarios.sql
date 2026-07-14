create database lumina;
use lumina;

create table usuario(email varchar(100) not null Primary key,
					 senha varchar(100) not null ,
                     nome varchar(100) not null,
                     data_nasc date not null) ,
                     nickName varchar(100)not null);
create table atividades(gabarito varchar(200) not null,
						codigoATIV varchar(100) not null primary key,
                        emailUSUARIO varchar(100) not null ,
                        respostaUSU varchar(100) not null,
                        FOREIGN KEY (emailUSU) REFERENCES usuario(email);
		
                        
	
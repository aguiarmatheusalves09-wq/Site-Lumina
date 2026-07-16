create database Lumina;
use Lumina;

create table usuario(email varchar(100) not null Primary key,
					 senha varchar(100) not null ,
                     nome varchar(100) not null,
                     data_nasc date not null ,
                     nickName varchar(100)not null);
                     
create table atividades(gabarito varchar(200) not null,
						codigoATIV varchar(100) not null primary key,
                        emailUSU varchar(100) not null ,
                        respostaUSU varchar(100) not null,
                        FOREIGN KEY (emailUSU) REFERENCES usuario(email));
                        
--codigo feito pelo caio guloso

create table videoaula(codigoVIDEO int auto_increment primary key,
					titulo varchar(150) not null,
					descricao text,
					urlVideo varchar(255) not null,
					duracao time,
					dataPublicacao date,
					materia int not null,
					foreign key (materia)references materia(codigoMAT)
);

--codigo feito pelo zaio cabeludo

create table artigo(codigoARTIGO int auto_increment primary key,
					titulo varchar(150)not null,
                    resumo text,
                    conteudo longtext not null,
                    dataPublicacao date,
                    materia int not null,
                    foreign key (materia) references materia(codigoMAT)
):
                    
                    
                        
	
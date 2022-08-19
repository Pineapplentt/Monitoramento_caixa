create database databaseKashPlus;
use databaseKashPlus;


CREATE TABLE Banco(
idBanco INT PRIMARY KEY AUTO_INCREMENT
,nomeEmpresarial VARCHAR(100)
,cnpj VARCHAR(20)
);

CREATE TABLE Usuario(
idUsuario INT PRIMARY KEY AUTO_INCREMENT
,nome VARCHAR(100)
,cpf VARCHAR(20)
,email VARCHAR(100)
,senha VARCHAR(100)
,cargo CHAR(3)
,fkBanco INT, FOREIGN KEY(fkBanco) REFERENCES banco(idBanco)
);

CREATE TABLE Regiao(
idRegiao INT PRIMARY KEY AUTO_INCREMENT
,nomeRegiao VARCHAR(200)
);

CREATE TABLE CaixaEletronico(
idCaixasEletronico INT PRIMARY KEY AUTO_INCREMENT
,localizacao VARCHAR(300)
,fkBanco INT, FOREIGN KEY(fkBanco) REFERENCES banco(idBanco)
,fkRegiao INT, FOREIGN KEY(fkRegiao) REFERENCES Regiao(fkReiao)
);

CREATE TABLE Registro(
idRegistro INT PRIMARY KEY AUTO_INCREMENT
,fkCaixaEletronico INT, FOREIGN KEY(fkCaixaEletronico) REFERENCES CaixaEletronico(idCaixaEletronico)
,dataHorario DATETIME
,consumoCPU DECIMAL(5,2)
,temperaturaCPU DECIMAL(5,2)
,consumoRAM DECIMAL(5,2)
,consumoREDE DECIMAL(5,2)
);

/* insert into usuario values (null, 'vinicius@gmail.com', '1234'); */
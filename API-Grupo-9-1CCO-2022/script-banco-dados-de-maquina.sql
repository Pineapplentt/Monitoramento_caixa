create database dados_de_maquina;
use dados_de_maquina;

create table registros_de_hardware (
	idRegistro int primary key auto_increment,
    dataHorario datetime,
    consumoCPU_Percent decimal(5,2),
    consumoRAM_Percent decimal(5,2)
);

select * from registros_de_hardware order by idRegistro desc;

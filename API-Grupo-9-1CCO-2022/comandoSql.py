
def insere_dadosHardware (con, dadosHardware):
    cursor = con.cursor()
    sql = "INSERT INTO registros_de_hardware (dataHorario, consumoCPU_Percent, consumoRAM_Percent) values (now(),"+ dadosHardware
    cursor.execute(sql)
    cursor.close()


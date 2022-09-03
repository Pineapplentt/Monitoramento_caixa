#Importanto a biblioteca responável por capturar dados de máquina
import psutil

#Importanto as bibliotecas responsáveis por gerar os gráficos
import matplotlib.pyplot as plt # Definindo um "apelido" para a biblioteca
from matplotlib.animation import FuncAnimation

#Importanto as funções responsáveis para conectar ao banco e fazer os inserts
from conexao import criar_conexao
from comandoSql import insere_dadosHardware

# Variável de conexão com  o banco, altere as informações necessárias como: host, usuario, senha e nome do banco para ficar de acordo com o Banco Criado na sua máquina
con = criar_conexao("localhost", "root", "Vini_0507", "dados_de_maquina")

dispositivos = psutil.disk_partitions();

# o def é a forma que você define uma função em python, com uma sequência de instruções que podem ser solicitadas mais de uma vez sem a necessidade de repetição de cód
def definirGraficos(frame):
    
    consumoRAM.append(psutil.virtual_memory()[2]) # adicionando os valores capturados pelo psutil na lista valores
    consumoRAM.remove(consumoRAM[0]) # remove o primeiro valor da lista
    consumoCPU.append(psutil.cpu_percent(interval=None))# adicionando os valores capturados pelo psutil na lista valores
    consumoCPU.remove(consumoCPU[0]) # remove o primeiro valor da lista

    graficosRAM.cla() # limpa os eixos
    graficosRAM.plot(consumoRAM, color='#b449de') # plota o gráfico
    graficosRAM.scatter(len(consumoRAM) - 1, consumoRAM[-1], color='#b449de') # marcador (bolinha) na posição atual do gráfico
    graficosRAM.title.set_text(f'Consumo de RAM - {consumoRAM[-1]}%') # título do gráfico
    graficosRAM.set_ylim(0, 100) # limite do eixo y
    
    graficosCPU.cla() # limpa os eixos
    graficosCPU.plot(consumoCPU, color='#49a7de') # plota o gráfico
    graficosCPU.scatter(len(consumoCPU) - 1, consumoCPU[-1], color='#49a7de') # marcador (bolinha) na posição atual do gráfico
    graficosCPU.title.set_text(f'Consumo de CPU - {consumoCPU[-1]}%') # título do gráfico
    graficosCPU.set_ylim(0, 100) # limite do eixo y

    #Criando um sistema que detecata quantas unidades de armazenamento tem na sua máquina e gerando um gráfico do tipo Pie = Torta/Pizza com a % de disco espaço e de espaço disponível
    i = 3
    cores = '#a5a8a8','#55cfed' # setando as cores que serão utilizadas no gráfico para ficarem estáticas.
    for dispositivo in dispositivos:
        armzTotalDisco = round((psutil.disk_usage(f'{dispositivo.device}')[0]) / (10**9),2); # Capturando a capacidade total de armazenamento do disco
        espacoUsadoDisco = round((psutil.disk_usage(f'{dispositivo.device}')[1]) / (10**9),2); # Capturando o espaço usado do disco
        espacoLivreDisco = round((psutil.disk_usage(f'{dispositivo.device}')[2]) / (10**9),2); # Capturando o espaço disponível do disco

        labels = f'Espaço Usado - {espacoUsadoDisco} Gb', f'Espaço Disponível - {espacoLivreDisco} Gb' # Definindo as lavels (Textos) da legenda
        sizes = [((espacoUsadoDisco/armzTotalDisco)*100), ((espacoLivreDisco/armzTotalDisco)*100)] # Definindo os tamanhos do gráfico de pizza em %
        
        graficosUnidArmz = plt.subplot(2,2,i) # Plotando o gráfico de pizza nas posições corretas da janela de gráficos
        graficosUnidArmz.pie(sizes, autopct='%1.1f%%', startangle=0, colors = cores) # Setando as configurações do gráfico, como as medidas com arredondamento de 1 casa decimal, o ângulo de inicio do gráfico e suas cores.
        graficosUnidArmz.title.set_text(f'Unidade - {dispositivo.device}') # título do gráfico
        graficosUnidArmz.legend(labels, loc="best", bbox_to_anchor=((0.55, -0.5, 0.5, 0.5))) # Setando as configurações da legenda, como os títulos e sua posição.
        graficosUnidArmz.axis('equal')  # Definindo a proporção de forma do gráficos para que as unidades de dados sejam as mesmas em todas as direções.
        
        i = i+1
    conRAM = consumoRAM[-1] # Armazenando em uma variavel o último valor inserido no vetor de consumoRAM
    conCPU = consumoCPU[-1] # Armazenando em uma variavel o último valor inserido no vetor de consumoCPU
    dadosHardware = str(conCPU) + ',' + str(conRAM) + ');' # Criando uma varivel do tipo strig para passar como parâmetro para a função de inserir dados no banco. (aqui é para complementar o insert do arquivo comandosSql.py)
    insere_dadosHardware(con, dadosHardware)

# cria uma lista com 10 zeros, esta lista será utilizada no eixo y gráfico
consumoRAM = [0] * 10 
consumoCPU = [0] * 10

# propriedades dos gráficos
telaPrincipal = plt.figure(figsize=(7, 6), facecolor='#EEE') # cria a janela com o tamanho e a cor
# criando os gráficos de CPU e RAM dentro da janela
graficosRAM = plt.subplot(321)
graficosCPU = plt.subplot(322)

graficosRAM.axes.get_xaxis().set_visible(False) # tira a visualização dos dados do eixo x
graficosRAM.set_facecolor('#DDD') # define a cor do gráfico

graficosCPU.axes.get_xaxis().set_visible(False) # tira a visualização dos dados do eixo x
graficosCPU.set_facecolor('#DDD') # define a cor do gráfico

# função para chamar em loop a função definirGraficos em um intervalo de 1s ou 1000ms (milissegundos)
animacaoGeral = FuncAnimation(telaPrincipal, definirGraficos, interval=1000)

# exibe a tela principal com os gráficos
plt.show()
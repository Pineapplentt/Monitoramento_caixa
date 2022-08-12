import os
import time

from time import time
from tokenize import String
nome=input('Qual seu nome? ')

resultado=float(input('Olá '+nome+' Seja bem vindo! \n Insira 1 para calcular seu IMC \n Insira 2 para sair do programa: '))
if resultado!=1 and resultado!=2:
    print('Insira uma das opções possiveis')
if resultado==2:
        print('Obrigado por usar nosso programa!')
        time.sleep(3)
        os.system('cls')
if resultado==1:
    peso=float(input('Quanto você pesa em Kg? (kg) '))
    altura=float(input('Quanto você mede em altura? (m)'))
    IMC = peso/(altura**2)
    print(nome+' o seu IMC é de {:.2f}'.format(IMC))
    
    if IMC < 18.5:
        print('Diagnóstico: Abaixo do peso normal')
    elif IMC >=18.5 and IMC <25:
        print('Diagnóstico: peso normal')
    elif IMC >=25 and IMC <30:
        print('Diagnóstico: sobrepeso')
    elif IMC >=30 and IMC <40:
        print('Diagnóstico: obeso')
    elif IMC >=40:
        print('Diagnóstico: obesidade mórbida')
    satisfeito=(input('Está satisfeito com o resultado?'))
    if satisfeito== 'sim'| satisfeito== 's' | satisfeito== 'SIM':
        print('Ficamos felizes por você')
    elif satisfeito== 'nao'| satisfeito== 'NAO'|satisfeito== 'n':
        print('Veja como melhorar  seu estilo de vida.')

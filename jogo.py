#Feito por Guilherme Saoncella da Silva
#email: guisaoncella@gmail.com
#github: guisaoncella
#https://www.linkedin.com/in/guilherme-saoncella/
#discord: puwer#9470

import JogoDaVelha as v
from time import sleep
import os

jogo = v.JogoDaVelha()

vencedor = 0
jogador = 1
while vencedor == 0:
    os.system('cls||clear')
    jogo.exibirTabuleiro() 
    print(f'\nJogador {jogador} escolha uma casa: ', end="")
    
    try:
        casa = int(input())
    except:
        print('Posição inválida tente novamente...')
        sleep(1)
        continue    

    casa -= 1
    #linha
    i = casa // 3
    #coluna
    j = casa % 3
    
    if not jogo.gravarCasa(i, j, jogador):
        print('Posição inválida tente novamente...')
        sleep(1)
        continue
    
    vencedor = jogo.verificarVencedor()
    
    jogador = (2 if jogador == 1 else 1)

if jogo.vencedor == 66:
    vencedor = 1
else:
    vencedor = 2

os.system('cls||clear')
print(f'JOGO FINALIZADO, O JOGADOR {vencedor} VENCEU!!!\n')
jogo.exibirTabuleiro()  

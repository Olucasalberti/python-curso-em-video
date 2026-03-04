#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar
#acertar qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import time
from time import sleep
from random import randint

num = randint(0,5)

print('_'*53)
print('Irei pensar em um número e você deve tentar acertar!')
print('_'*53)

tent = int(input('Escolha um número inteiro entre 0 e 5: '))

print('PROCESSANDO...')
time.sleep(3)

if num == tent:
    print('PARABÉNS! Você venceu!')

else:
    print('Você perdeu, o número era {} e não {}'.format(num,tent))

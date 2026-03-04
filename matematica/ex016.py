#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#EX: Digite um número: \n O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}'.format(num, trunc(num)))

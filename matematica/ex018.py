#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse ângulo

from math import sin, radians, cos,tan

an = float(input('Digite um ângulo para a conversão: '))

ra = radians(an)

s = sin(ra)
c = cos(ra)
t = tan(ra)

print('Seno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(s, c, t))




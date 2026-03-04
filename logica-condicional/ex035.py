#desenvolva um programa que leia o comprimento de 3 rotas e diga ao usuario se elas podem ou não formar um triângulo

from time import sleep

print('\033[0;36m_\033[m'*63)
print('\033[1;34mVamos descobrir se as 3 rotas juntas, podem formar 1 triângulo!\033[m')
print('\033[0;36m_\033[m'*63)

r1 =  int(input('\n\033[34mDigite o tamanho da rota 1: '))
r2 = int(input('Digite o tamanho da rota 2: '))
r3 = int(input('Digite o tamanho da rota 3: \033[m'))

print('\n\033[34mPROCESSANDO...\033[m\n')
sleep(1.25)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\033[1;32mO comprimento de todas as suas 3 rotas podem formar um triângulo!\033[m')
else:
    print('\033[1;31mO comprimento das suas 3 rotas não podem formar um triângulo!\033[m')
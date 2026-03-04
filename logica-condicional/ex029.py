#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

from time import sleep

print('_'*50)
print('ALERTA RADAR A FRENTE!!!\nLIMITE DA VIA 80km/h')
print('_'*50)

vel = int(input('A velocidade do carro foi de quantos km/h? '))

valor = (vel - 80)*7

print('REGISTRANDO VALOCIDADE...')
sleep(2)

if vel > 80:
    print('\nVocê foi multado!\nSua velocidade foi de {}km/h\nO valor da multa é de R${:.2f}'.format(vel,valor))

else:
    print('\nParabéns! Você respeitou os limites de velocidade!')
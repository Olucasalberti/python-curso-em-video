#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1,00 = R$3,27

d = float(input('Digite quanto dinheiro você possui na carteira: R$'))

print('Com seu saldo atual de R${:.2f} você consegue comprar US${:.2f}'.format(d, d/3.27))
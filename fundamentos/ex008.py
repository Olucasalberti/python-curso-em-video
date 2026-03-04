#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = float(input('Quantos metros você deseja converter?'))

print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m/1000,m/100,m/10,m*10,m*100,m*1000))
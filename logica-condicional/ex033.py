#faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

num1 = float(input('\033[33mdigite o primeiro número:'))

num2 = float(input('segundo número:'))

num3 = float(input('terceiro número:\033[35m',))

#MAIOR
if num1 > num2 and num1 > num3:
    print('Seu maior número é {:.0f}'.format(num1))
if num2 > num1 and num2 > num3:
    print('Seu maior número é {:.0f}'.format(num2))
if num3 > num1 and num3 > num2:
    print('Seu maior número é {:.0f}'.format(num3))

#MENOR
if num1 < num2 and num1 < num3:
    print('E seu menor número é {:.0f}'.format(num1))
if num2 < num1 and num2 < num3:
    print('E seu menor número é {:.0f}'.format(num2))
if num3 < num1 and num3 < num2:
    print('E seu menor número é {:.0f}'.format(num3))
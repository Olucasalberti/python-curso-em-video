#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#em que posição ela aparece a primeira vez
#em que posição ela aparece pela última vez

frase = input('Escreva uma frase:').strip()

print('A letra (A) aparece {} vezes na sua frase'.format(frase.upper().count('A')))

print('ela aparce pela primeira vez na posição {}'.format(frase.upper().find('A')+1))

print('e ela aparece pela última vez na posição {}'.format(frase.upper().rfind('A')+1))
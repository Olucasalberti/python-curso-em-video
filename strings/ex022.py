#crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras mnaiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo sem considerar espaços
#Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo:')

todo = nome.split()

print('Analisando seu nome...\nmaiúsculo', nome.upper())
print('minúsculo:', nome.lower())
print('seu nome todo tem {} letras'.format(len(''.join(todo))))
print('seu primeiro nome tem {} letras'.format(len(todo[0])))

#print('seu primeiro noem tem {} letras'.format(nome.find(' ')))
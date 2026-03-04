#desenvolva um programa que calcule as 2 notas de um aluno e mostre a sua média

aluno = input('Escreva o nome do Aluno:')

n1 = float(input('Digite a nota do primeiro semestre:'))
n2 = float(input('Digite a nota do segundo semestre:'))

print('A média final do/a {} é {:.1f}'.format(aluno, (n1+n2) / 2))
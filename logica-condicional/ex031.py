#desenvolva um programa que pergunte a distância de uma viagem em km.
#calcule o preço da passagem, cobrando R$0,50 por km para viagens ate 200km e
# cobrando R$0,45 para viagens mais longas

viagem = float(input('\033[34mSua viagem deu quantos km?\033[m'))

curta = viagem*0.50
longa = viagem*0.45

if viagem <= 200:
    print('\033[36mSua viagem de {:.0f}km deu um valor final de {:.2f}R$'.format(viagem, curta))
else:
    print('\033[36Sua viagem de {:.0f}km deu um valor final de {:.2f}R$'.format(viagem,longa))
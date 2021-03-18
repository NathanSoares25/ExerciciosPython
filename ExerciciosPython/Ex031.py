# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Digite a distância da sua viagem: '))
abaixo = km * 0.50
acima = km * 0.45
if km <= 200:
    print('A passagem custará R${:.2f}'.format(abaixo))
else:
    print('Sua distância ultrapassou os 200Km de distância, logo, ela custará R${:.2f}'.format(acima))

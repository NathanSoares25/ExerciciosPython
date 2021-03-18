# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Quantos reais você tem na carteira? '))
dolar = real * 5.39
print('R${} vale US${:.2f} na cotação de hoje.'.format(real, dolar))

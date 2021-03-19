# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
print('=' * 15)
print('LIQUIDAÇÃO')
print('=' * 15)
preco = float(input('Digite o preço do produto: R$'))
desc = preco * 5 / 100
novo = preco - desc
print('O produto vale R${:.2f} e com o desconto de 5% irá valer R${:.2f}'.format(preco, novo))

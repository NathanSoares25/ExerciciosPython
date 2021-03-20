# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros
from time import sleep
# Início do programa
print('\033[1:30m-\033[m' * 15)
print('\033[1:30mLOJAS SOARES\033[m')
print('\033[1:30m-\033[m' * 15)
# Programa interage com o usuário
produto = float(input('\033[1mDigite o valor do produto: R$\033[m'))
print('\033[1;30mAGUARDE POR FAVOR...\033[m')
sleep(2)
print('\033[1:36mEscolha sua melhor forma de pagamento:\033[m')
print('Caso pague à vista em dinheiro ou em cheque, você ganha 10% de desconto. \033[4:31mDigite [1] para esta opção\033[m')
print('Caso pague à vista no cartão, você ganha 5% de desconto. \033[4:31mDigite [2] para esta opção\033[m')
print('Caso parcele em 2x no cartão, você pagará o preço normal. \033[4:31mDigite [3] para esta opção\033[m')
print('Caso parcele em até 3x ou mais, terá um juros de 20%. \033[4:31mDigite [4] para esta opção\033[m')
opcao = int(input('Digite a opção desejada por favor: '))
# Programa realizando as funções
if opcao == 1:
    desconto = produto - (produto * 10 / 100)
    print('O produto que custa R${}, com 10% de desconto passará a custar R${}.'.format(produto, desconto))
elif opcao == 2:
    desconto = produto - (produto * 5 / 100)
    print('O produto que custa R${}, com 5% de desconto passará a custar R${}.'.format(produto, desconto))
elif opcao == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
    print('Como você irá parcelar em 2x, o produto será o mesmo valor sem nenhum desconto ou acréscimo de juros.')
elif opcao == 4:
    opcao1 = int(input('Em quantas parcelas deseja pagar? '))
    parcela = produto + (produto * 20 / 100)
    valor2 = parcela / opcao1
    print('Sua compra será parcelada em {}x de R${:.2f} \033[4;31mCOM JUROS\033[m'.format(opcao1, valor2))
    print('Sua compra de R${:.2f} vai custar \033[4;31mR${:.2f}\033[m no final.'.format(produto, parcela))

else:
    print('OPÇÃO INVÁLIDA!')

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#-----------------------------FIZ CERTO-------------------------------------------
'''func = input('Digite o nome do funcionário: ')
salario = float(input('Digite quanto o funcionário recebe: '))
aumento = 15 / 100 * salario
novo = aumento + salario
print('O funcionário {} que recebe R${:.2f}, ganhou um aumento de 15% e passará a receber R${:.2f}.'.format(func, salario, novo))'''

# ------------------------------------APROVETEI E CRIEI OUTRO ALGORITIMO----------------------
prod = float(input('Digite o valor do produto: R$'))
vista = prod - (prod * 15 / 100)
parcelado = prod + (prod * 10 / 100)
print('Se o produto for pago á vista terá um desconto de 15% e o valor será de R${}.'.format(vista))
print('Se o produto for pago em parcelas terá um acrescimo de 10% e o valor será de R${}.'.format(parcelado))

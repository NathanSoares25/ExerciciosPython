# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
nome = str(input('Olá! Digite seu nome: '))
salario = float(input('Digite seu salário por favor: R$'))
aumento10 = salario + (salario * 10 / 100)
aumento15 = salario + (salario * 15 / 100)
if salario > 1250.00:
    print('Você recebe acima de R$1250.00, logo, seu aumento será de 10% e você passará a receber R${:.2f}'.format(aumento10))
if salario < 1250.00:
    print('Você recebe menos que 1250.00, logo, seu aumento será de 15% e você passará a receber R${:.2f}'.format(aumento15))

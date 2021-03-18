# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida
# Iniciando o programa
print('\033[1;30m¬\033[m' * 40)
print('\033[4;34mCALCULO DE IMC (INDÍCE DE MASSA CORPORAL)\033[m')
print('\033[1;30m¬\033[m' * 40)
# Usuário interagindo com o programa
peso = float(input('Digite seu peso por favor: (Kg) '))
altura = float(input('Digite sua altura por favor: (m) '))
# Realizando os calculos das funções
imc = peso / (altura ** 2)
# Programa respondendo ao usuário
if imc <= 18.5:
    print('Seu Indíce de Massa Corporal é de {:.1f}. Portanto, você está \033[4;34mABAIXO DO PESO!\033[m'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu Indíce de Massa Corporal é de {:.1f}. Portanto, você está no \033[4;32mPESO IDEAL!!\033[m'.format(imc))
elif 25 <= imc < 30:
    print('Seu Indíce de Massa Corporal é de {:.1f}. Portanto, você está no \033[4;33mSOBREPESO!\033[m'.format(imc))
elif 30 <= imc < 40:
    print('Seu Indíce de Massa Corporal é de {:.1f}. Portanto, você está \033[4;31mOBESO! CUIDE-SE!\033[m'.format(imc))
else:
    print('Seu Indíce de Massa Corporal é de {:.1f}. Você está em \033[4;31mOBESIDADE MÓRBIDA! CUIDE-SE!\033[m'.format(imc))

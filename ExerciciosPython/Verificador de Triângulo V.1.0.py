# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#EXERCICIOS ERRADO
print('*' * 20)
print('VERIFICADOR TRIÂNGULOS V1.0')
print('*' * 20)
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
print('VERIFICANDO...')
if b - c < a < b + c is a - c < b < a + c is a - b < c < a + b:
    print('Estes valores PODEM formar um triângulo!')
else:
    print('Estes valores NÃO PODEM formar um triângulo!')

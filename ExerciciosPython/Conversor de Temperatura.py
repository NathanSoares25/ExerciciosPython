# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print('-' * 30)
print('CONVERSOR DE TEMPERATURA V1.0')
print('-' * 30)
temp = float(input('Digite a temperatura em Celsius: '))
fh = temp * 1.8 + 32
print('A temperatura de {}°C, corresponde à {}°F!'.format(temp, fh))

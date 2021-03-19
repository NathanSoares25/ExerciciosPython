# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em letras maiúsculas?', n.isupper())
print('Está em letras minúsculas?', n.islower())
print('Está capitalizada?', bool(n))


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hi))

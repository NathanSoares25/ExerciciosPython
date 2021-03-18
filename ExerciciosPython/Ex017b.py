# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#-----------------------ALGORITIMOS DIFERENTES DO EX017------------------------
import math
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))

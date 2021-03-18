# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite um ângulo: '))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, math.sin(math.radians(ang))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, math.cos(math.radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, math.tan(math.radians(ang))))

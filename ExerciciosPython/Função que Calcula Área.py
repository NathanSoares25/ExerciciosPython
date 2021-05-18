# Faça um programa que tenha uma função area(), que receba as dimensões de um terreno retangular (largura e comprimento)
# E mostre a area do terreno.

def área(larg, comp):
    m = larg * comp
    print(f'O terreno de dimensão {l}x{c} tem a área de {m}m². ')


print('Controle de terrenos')
print()
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
área(l, c)

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# ---------------------------FIZ ERRADO-------------------------------
'''larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
parede = larg * alt
tinta = parede * 2
print('Esta parede contém {} metros quadrados e precisará de {} litros de tinta.'.format(parede, tinta))'''
# ------------------------CORREÇÃO------------------------------------
larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))
parede = larg * alt
tinta = parede / 2
print('Esta parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, parede))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))

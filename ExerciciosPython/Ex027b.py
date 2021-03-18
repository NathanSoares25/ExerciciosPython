# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('Gostei de brincar e agora irei descobrir seu segundo nome ;)')
nome = str(input('Digite seu nome completo ai rapa: '))
segundo = nome.upper().strip().split()[1]
print('Se segundo nome é {}.'.format(segundo))

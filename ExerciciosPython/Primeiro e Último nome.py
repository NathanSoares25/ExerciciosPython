# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('Agora irei descobrir seu primeiro e o ultimo nome :D.')
nome = str(input('Digite seu nome completo: '))
primeiro = nome.upper().strip().split()[0]
ultimo = nome.upper().rstrip().rsplit()[-1]
print('O seu primeiro nome é {} e o ultimo nome é {}'.format(primeiro, ultimo))

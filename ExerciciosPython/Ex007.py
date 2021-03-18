# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nome = str(input('Olá! Digite o nome do aluno por favor: '))
med1 = float(input('Digite a nota do primeiro bimestre: '))
med2 = float(input('Digite a nota do segundo bimestre: '))
res = (med1 + med2) / 2
print('A média entre {} e {} do aluno {} é {:.1f}'.format(med1, med2, nome, res))

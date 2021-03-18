# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um valor: '))
d = n1 * 2
t = n1 * 3
rz = n1 ** (1/2)
print('O dobro desse valor é: {}\n O triplo desse valor é: {}\n E a raiz quadrada desse valor é: {:.2f}'.format(d, t, rz))

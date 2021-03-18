#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# Inciando o programa
print('\033[1;30m*\033[m' * 20)
print('\033[1;32mTABUADA V2.0\033[m')
print('\033[1;30m*\033[m' * 20)
num = int(input('Digite um número para saber sua tabuada: '))
for c in range(0, 10+1):
    print('{} x'.format(num), c, '=', c * num)

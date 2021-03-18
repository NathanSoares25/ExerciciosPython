# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# Inicio do Programa
print('\033[1;30m=\033[m' * 25)
print('\033[1;35m10 PRIMEIROS TERMOS DE PA\033[m')
print('\033[1;30m=\033[m' * 25)
# Programa Interage com o Usuário
num = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = num + (10 - 1) * r
for c in range(num, decimo + r, r):
    print(c, end= ' → ') # RESPOSTA DO PROGRAMA
print('FIM')
# FIM DO PROGRAMA
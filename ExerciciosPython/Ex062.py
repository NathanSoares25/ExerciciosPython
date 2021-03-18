# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('\033[1;30m=\033[m' * 25)
print('\033[1;35mTERMOS DE PA V3.0\033[m')
print('\033[1;30m=\033[m' * 25)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quer continuar? Digite quantos termos quer mostrar a mais: '))
print('Esta progressão foi finalizada com {} temos.'.format(total))
print('Fim')

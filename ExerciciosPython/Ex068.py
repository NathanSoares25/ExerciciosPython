# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
venceu = 0
while True:
    escolha = int(input('Digite um valor: '))
    pc = randint(1, 10)
    resultado = escolha + pc
    opção = ' '
    while opção not in 'PI':
       opção = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {escolha} e o computador jogou {pc}. O total deu {resultado}')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR')
    if opção == 'P':
        if resultado % 2 == 0:
            print('VOCÊ VENCEU!!!')
            venceu += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif opção == 'I':
        if resultado % 2 == 1:
            print('VOCÊ GANHOU')
            venceu += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar de novo...')
print('GAME OVER! Fim do programa.')

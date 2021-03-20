# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
# Início do programa
print('\033[1;30m-\033[m' * 30)
print('\033[1;32mALISTAMENTO MILITAR OBRIGATÓRIO\033[m')
print('\033[1;30m-\033[m' * 30)
# Programa pergunta ao usuário
nome = str(input('Olá! Digite seu nome completo por favor: '))
nascimento = int(input('Digite o ano do seu nascimento por favor: '))
# Progama realizando as funções
hoje = datetime.date.today().year
idade = hoje - nascimento
# Programa respondendo o usuário
if idade == 18:
    print('Você deverá se alistar este ano!')
elif idade > 18:
    print('Você já passou do tempo de alistamento. Seu alistamento aconteceu há {} anos'.format(hoje - nascimento - 18))
elif idade < 18:
    print('Você ainda não está na idade para o alistamento! Falta {} ano(s) para você se alistar.'.format(18 - idade))

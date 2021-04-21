# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionario .
# No final, mostre o conteudo da estrutura na tela.

dicionario = dict()
lista = list()

# Criando a interação com o usuário
dicionario['Nome'] = str(input('Digite o nome do aluno: '))
dicionario['Média'] = float(input('Digita a média: '))

# Copiando o dicionario para a lista
lista.append(dicionario.copy())

# Para cada dados na lista
for d in lista:
    for n, m in d.items():
        print(f'{n} é igual a {m}')

if dicionario['Média'] >= 7:
    print('A situação do aluno é APROVADO!')
else:
    print('A siutação do aluno(a) é REPROVADO!')

# CORREÇÃO DO GUANABARA

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
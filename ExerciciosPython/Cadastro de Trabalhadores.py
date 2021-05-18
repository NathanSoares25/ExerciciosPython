# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Importando o datetime
from datetime import datetime

# Dicionario com os dados do usuário
dados = dict()

# Colocando os dados dentro do dicionario
dados['Nome'] = str(input('Digite seu nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['Carteira'] = int(input('Digite o número da carteira de trabalho (caso não tenha, digite 0): '))

# Se o usuário tiver carteira
if dados['Carteira'] != 0: # Se a carteira for difente de 0, irá mostrar as outras opções abaixo
    dados['Contratado'] = int(input('Digite o ano da sua contratação: '))
    dados['Salário'] = float(input('Digite o seu salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratado'] + 35) - datetime.now().year)
print()
print('-' * 20)
for k, v in dados.items():
    print(f'{k} tem valor {v}.')
print('-' * 20)


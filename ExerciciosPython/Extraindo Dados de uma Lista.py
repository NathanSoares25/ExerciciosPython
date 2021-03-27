# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# Quantos números foram digitados.
# A lista de valores em ordem decrescente
# Se o valor 5 foi digitado e está ou não na lista

'''lista = list() # lista criada
cont = 0 # contador

while True:
    num = int(input('Digite um valor: ')) # valores que será adicionado na lista
    cont += 1 # conta os números que forem adicionados
    lista.append(num)
    print('Valor adicionado com sucesso!')
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if opção == 'N':
        break

print('=' * 50)

print(f'Você digitou os números {lista}.') # Mostra os números digitados
print(f'Você inseriu {cont} números na lista.') # Quantos números existem na lista

if 5 in lista: # verifica se o número 5 foi digitado
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado na lista.')

lista.sort(reverse=True) # Reverte a ordem dos números
print(f'Os números em ordem reversa fica assim: {lista}')

print('=' * 50)'''

# CORREÇÃO DO GUANABARA

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(f'Você digitou os números {len(valores)}')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O número 5 foi inserido na lista')
else:
    print('Não existe o número 5 na lista')

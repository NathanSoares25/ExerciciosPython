# Faça um programa que leia 5 valores e guarde-os em uma lista, no final mostre qual é o maior e o menor valor e qual
# A sua posição na lista

'''valores = list() # cria uma lista

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: '))) # inserindo os números dentro da lista

print(f'Os valores digitadores foram {valores}') # lista com os números inseridos

print(f'O maior valor digitado foi {max(valores)} na posição: ', end='') # maior valor e a posição do mesmo
for posição in range(0, 5):
    if valores[posição] == max(valores):
        print(posição, end=', ')

print(f'\nO menor valor digitado foi {min(valores)} na posição: ', end='') # menor valor e a posição do mesmo
for posição in range(0, 5):
    if valores[posição] == min(valores):
        print(posição, end=', ')'''

                                               # RESOLUÇÃO DO EXERCÍCIO

lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i},', end='')
print()
print(f'O menor valor digitado foi {menor} na posição: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i},', end='')
print()

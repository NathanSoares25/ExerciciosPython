# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão apenas conter os valores pares e impares digitados
# Ao final, mostre as três listas geradas

lista = list() # Lista criada
lista_par = list() # Lista de números pares criada
lista_impar = list() # Lista de números impares criada

while True:
    n = int(input('Digite um número: ')) # Programa pede para o usuário digitar um valor
    lista.append(n) # Os números digitados pelo usuário será colocado na lista

    if n % 2 == 0: # Se o número for par, coloca o número na lista de pares
        lista_par.append(n)
    else: # Se não for par, colocar os números na lista de impares
        lista_impar.append(n)
    print('Número adicionado com sucesso!')
    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0] # Opção para o usuário continuar ou não, com as letras maiúsculas e com o strip para remover os espaços

    while opção not in 'SN': # Enquanto o usuário não digitar 'S' ou 'N' o programa continuará perguntando
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N': # Se a opção for 'N' o programa irá encerrar e mostrar os dados digitados
        break


print('=-' * 30)
print('Fim do programa')
print(f'Você digitou os números {lista}.')
print(f'Os núemeros pares digitados foram {lista_par}')
print(f'Os números impares digitados foram {lista_impar}')

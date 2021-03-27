# Crie um programa onde o usuário possa digitar vários valores numéricos e cadatre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final serão exibidos todos os valores únicos digitados, em ordem crescente

lista = list() # criei uma lista

while True:
    valor = int(input('Digite um valor: ')) # valor digitado pelo usuário que vai ser inserido na lista

    if valor not in lista:      # IF para verificar se há número repetidos na lista
        lista.append(valor)
        print('Valor adicionado com Sucesso!')
    else:
        print('Valor já adicionado! Tente outro número.')

    opção = str(input('Quer continuar? [S/N]: ')).upper().strip()  # Opção de escolha para continuar ou para o programa

    while opção not in 'SN':  # Enquanto a opção for diferente de sim ou não, o programa continuará perguntando
        opção = str(input('Quer continuar? [S/N]: ')).upper().strip()

    if opção == 'N': # Se o usuário digitar 'N' o programa encerra
        break

lista.sort() # Coloca os números em ordem crescente
print(f'Os números digitados foram: {lista}')

# CORREÇÃO DO GUANABARA

lista = list() # criar lista
p = 0 # posição

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista.')
    else:
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
            print(f'Número adicionado na posição {p} da lista')
            break
            p += 1

print(f'Os valores adicionados a lista foram {lista}')



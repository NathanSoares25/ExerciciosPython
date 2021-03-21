# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('CPU', 150,
            'Mouse', 89.90,
            'Monitor', 1200,
            'Teclado', 154.68,
            'Placa de Vídeo', 2554,
            'Memoria RAM', 180,
            'Placa Mãe', 200)
print('=' * 40)
print('PREÇO DOS PRODUTOS')
print('=' * 40)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:-<30}', end=' ')
    else:
        print(f'R${produtos[i]:.2f}')
print('=' * 40)

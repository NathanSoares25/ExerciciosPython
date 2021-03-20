# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7.00
if vel <= 80:
    print('Você está no limite permitido pela lei. PARABÉNS!')

print('Você ultrapassou o limite de velocidade permitido que é de 80Km e pagará R${} de multa.'.format(multa))

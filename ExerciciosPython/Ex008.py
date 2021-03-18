# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print('='*20)
print('CONVERSOR')
print('='*20)

n1 = float(input('Digite o valor em metros para converter: '))
km = n1 / 1000
hm = n1 / 100
dam = n1 / 10
dm = n1 * 10
cm = n1 * 100
mm = n1 * 1000
print('{}m equivale à: \n{}Km. \n{}hm. \n{}dam. \n{:.0f}dm.'.format(n1, km, hm, dam, dm))
print('{:.0f}cm. \n{:.0f}mm.'.format(cm, mm))

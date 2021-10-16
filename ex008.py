#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

d = float(input('Digite a distancia em metros: '))
print('{} metros equivale a {} centímetros e {} milímetros'.format(d, d*100, d*1000))
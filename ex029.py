'''Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por km acima do limite.'''


v = float(input('Digite a velocidade do veículo: \n'))
m = (v-80)*7
if v>80:
  print('Multado por excesso de velocidade! O valor da multa é de R${:.2f} .'.format(m))
else:
  print('Velocidade dentro do limite permitido !')
print('\n ---FIM ---\n')
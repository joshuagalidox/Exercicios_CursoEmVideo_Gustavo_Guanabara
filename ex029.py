v = float(input('Digite a velocidade do veículo: \n'))
m = (v-80)*7
if v>80:
  print('Multado por excesso de velocidade! O valor da multa é de R${:.2f} .'.format(m))
else:
  print('Velocidade dentro do limite permitido !')
print('\n ---FIM ---\n')
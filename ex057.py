'''### Ex057 - Qual é o sexo?

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
key = "nok"
sex = "a"
while not key == "ok":
  sex = input('Digite o sexo do individuo [M / F]: ').upper().strip()
  if sex == "M" or sex == "F":
    key = "ok"
    print(str(sex))
    print(key)
  else:
    key = "nok"
    print('Parametro incorreto. Digite novamente')
print('Obrigado')
print('FIM')

'''Soluçao alternativa professor
sexo = str(input('Informe seu sexo: [M / F]')).strip().upper() [0]
while sexo not in 'MF':
  sexo = str(input('Dados invalidos. Por favor, informe seu sexo: [M / F]')).strip().upper() [0]
print('Sexo {} registrado com sucesso '. format(sexo))'''
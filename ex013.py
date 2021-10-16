# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario com
# 15% de aumento

s = float(input('Digite seu salário atual: '))
a = 0.15

print('Com o aumento de {}%, seu novo salario será de R$ {:.2f} '. format(a*100, s*(1+a)))

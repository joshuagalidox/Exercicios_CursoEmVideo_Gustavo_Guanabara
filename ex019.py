#Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random as r
a = input('Digite o nome do 1o aluno: ')
b = input('Digite o nome do 2o aluno: ')
c = input('Digite o nome do 3o aluno: ')
d = input('Digite o nome do 4o aluno: ')
lista = [a, b, c, d]

e = r.choice(lista)

print('O escolhido foi {} .'. format(e))

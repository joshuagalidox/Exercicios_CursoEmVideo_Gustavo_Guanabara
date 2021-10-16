'''O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalho dos alunos.
Faca um programa qye leia o nome dos quatro alunos e mostre a ordem sorteada.'''

import random as r

a = input('Digite o nome do 1o aluno: ')
b = input('Digite o nome do 2o aluno: ')
c = input('Digite o nome do 3o aluno: ')
d = input('Digite o nome do 4o aluno: ')

turma = [a, b, c, d]

ordem = r.shuffle(turma)

print ('A ordem de apresentaçao será: ')
print (turma)


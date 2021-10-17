'''027. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente. Ex.: Ana Maria de Souza
                        Primeiro nome = Ana
                        Ultimo nome = Souza'''

"""nome = str(input('Digite seu nome completo: ')).strip()
fn = nome.find(' ')
ln = nome.rfind(' ')
print('Primeiro nome: {}'.format(nome[:fn]))
print('Último nome: {}'.format(nome[ln:]))"""

'''Alternativa'''
n = str(input('Digite seu nome completo: ' )).strip()
nome = n.split() #transforma a string em lista
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {} '.format(nome[len(nome)-1]))

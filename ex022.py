'''022. Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiusculas
    - O nome com todas as letras minusculas
    - Quantas letras ao todo (sem considerar espaços)
    - Quantas letas tem o primeiro nome '''


nome = str(input('Digite seu nome completo: ')).strip()
pnome = nome.find(" ")
liste = nome.split()

print('Seu nome em letras maiusculas: {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len("".join(liste))))
#print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras. '.format(len(nome[:pnome] )))






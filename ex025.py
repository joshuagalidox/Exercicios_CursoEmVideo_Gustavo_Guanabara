
'''025. Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome'''

nome = str(input('Digite seu nome completo: ')).strip()
n = nome.upper()
print('Seu nome tem Silva? ', n.find("SILVA")>0) 

'''alternativa
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))'''
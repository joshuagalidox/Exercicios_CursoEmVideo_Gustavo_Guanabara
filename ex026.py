'''026. Faça um prorama que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra 'A'.
    - Em que posiçao ela aparece pela primeira vez
    - Em que posiçao ela aparece a ultima vez '''

frase = str(input('Digite sua frase: ')).lower().strip()

print('Analisando seu texto... ')
print('A letra aparece {} vezes no seu texto! '.format(frase.count('a')))
print('A letra A aparece pela primeira vez em seu texto no {}o caracter.  '.format(frase.find('a')+1))
print('A letra A aparece pela última vez em seu texto no {}o caracter .'.format(frase.rfind('a')+1))

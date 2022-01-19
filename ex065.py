'''### Ex065 - Quer continuar?

Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao, mostyre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores'''


l = []
avg = 0
n = 0
gatilho = "N"
resposta = "S"
while not resposta == gatilho :
  n = int(input("Digite um número: "))
  l.append(n)
  avg = sum(l) / len(l)
  resposta = str(input("Deseja continuar? (S/N)")).upper().strip()
  if resposta == gatilho:
   print("Voce decidiu encerrar a aplicaçao")
print("Os numeros digitados foram: {}".format(l))
print("A média entre eles é de: {}".format(avg))

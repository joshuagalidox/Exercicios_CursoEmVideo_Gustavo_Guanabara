'''### Ex064 - Flag

Crie um programa que leia varios numeros inteiros pelo teclado. 
O programa só vai parar quando o usuario digitar o valor 999, que é a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando o flag'''


l = []
s = 0
n = 0
print("{}Digite quantos numeros quiser. Caso queira encerrar digite 999. {}".format("\n", "\n"))
while not n == 999 :
  n = int(input("Digite um número: "))
  if n !=999:
    l.append(n)
    s = sum(l)
  else:
    print("Voce decidiu encerrar a aplicaçao")
print("Os numeros digitados foram: {}".format(l))
print ("A soma entre eles corresponde a:  {}".format(s))

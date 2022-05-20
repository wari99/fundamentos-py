#Faça um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma de todos os números compreendidos entre eles. Os valores A e B não devem ser
#considerados no somatório. Caso A seja maior do que B deve ser enviada uma mensagem para o usuário informando que a soma não será realizada

a = b = soma = 0

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))
if(b > a):
  for a in range(a+1,b):
    soma += a
  print("Somatorio igual a ", soma)
else:
  print("A soma nao sera realizada. A nao pode ser maior que B.")

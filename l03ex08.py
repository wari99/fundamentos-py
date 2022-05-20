#Faça um algoritmo que leia 2 números inteiros positivos, A e B, e que calcule a soma de todos os números múltiplos de 4 compreendidos entre eles. Os valores A e B não 
#devem ser considerados no somatório. Caso A seja maior do que B deve ser enviada uma mensagem para o usuário informando que a soma não será realizada.

a = b = soma = somamult = 0

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero: "))

if(b > a):
  for a in range(a+1,b):
    if(a % 4 == 0):
      somamult += a
    soma += a
  print("Somatorio igual a ", soma)
  print("Soma dos multiplos de 4: ", somamult)
  
else:
  print("A soma nao sera realizada. A nao pode ser maior que B.")

#faça um algoritmo de caixa eletrônico que lê a quantidade de dinheiro a ser sacado e imprime a menor quantidade de notas a ser dada ao usuário. Assume-se que existam notas de 50, 20, 10, 5 e 1. Imprimir também a quantidade de cada nota a ser dada ao usuário. O final da leitura é marcado pelo valor 0 que não deve ser calculado. Ex: 98 = 1 de 50, 2 de 20, 1 de 5, 3 de 1.

valor = int(input("Valor a ser sacado: R$"))
q50 = q20 = q10 = q5 = q1 = 0

while(valor != 0):
  while(valor != 0):
    if(valor >= 50):
      valor -= 50
      q50 += 1
    elif(valor >= 20):
      valor -= 20
      q20 += 1
    elif(valor >= 10):
      valor -= 10
      q10 += 1
    elif(valor >= 5):
      valor -= 5
      q5 += 1
    elif(valor >= 1):
      valor -= 1
      q1 += 1
    
  print("Notas de 50: ", q50)
  print("Notas de 20: ", q20)
  print("Notas de 10: ", q10)
  print("Notas de 5: ", q5)
  print("Notas de 1: ", q1)
  
  q50 = q20 = q10 = q5 = q1 = 0
  
  valor = int(input("Valor a ser sacado: R$"))

if(valor == 0):
  print("Fim da Leitura.")

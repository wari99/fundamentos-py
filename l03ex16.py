#Faça uma algoritmo que leia um número N e imprima se ele é perfeito ou não. Um número é perfeito quando a soma dos seus divisores é igual a ele mesmo. Ex: 6 = 3 + 2 + 1

perf = int(input("Verificar se o No e perfeito: "))
soma = 0
i = 1

for i in range(i, perf):
  if(perf % i == 0):
    soma = soma + i

if(soma == perf):
  print("Esse numero e perfeito")
else:
  print("Esse numero nao e perfeito")

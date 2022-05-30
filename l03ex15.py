#Faça um algoritmo que leia um número N e verifique se ele é primo.

N = int(input("Numero N: "))
i = 1
numdivisores = 0

for i in range(i, N+1):
  if(N % i == 0):
    numdivisores += 1

if(numdivisores == 2):
  print("E primo")
else:
  print("Nao e primo")

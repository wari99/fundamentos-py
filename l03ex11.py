#Faça um algoritmo que calcule a soma dos N primeiros números inteiros ímpares e positivos. O valor de N deve ser lido do usuário.
soma = n = 0
i = 0
num = 0

n = int(input("N: "))

for i in range(i, n):
  num = (i * 2) + 1
  soma = soma + num

print("Soma dos %d primeiros numeros impares: " % n, soma)

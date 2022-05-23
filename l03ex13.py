#Faça um programa que calcule a soma dos primeiros 50 números pares. Esse programa não recebe valor do teclado. Os primeiros números pares são: 2,4,6,...

N = 50  
soma = aux = i = 0

for i in range(1,N+1):
  aux = i * 2
  soma = soma + aux

print(soma)

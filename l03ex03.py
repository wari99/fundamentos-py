#Faça um programa que leia uma quantidade não determinada de números inteiros. O programa deve calcular e escrever a quantidade de números pares e ímpares e a média 
#aritmética dos números pares. O leitura sera encerrada quando for lido o número zero, que não deve ser considerado.

num = 1 
qtdpar = -1
somapar = qtdimpar = 0
mediapar = 0.0

while(num != 0):
    num = int(input("Escrever N inteiro: "))

    if(num % 2 == 0):
        qtdpar += 1
        somapar += num
    if(num % 2 == 1):
        qtdimpar += 1

mediapar = somapar / qtdpar

print("Quantidade de numeros pares: ", qtdpar)
print("Quantidade de numeros impares: ", qtdimpar)

print("Media Aritmetica numeros pares: ", mediapar)

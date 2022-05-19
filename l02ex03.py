#Faça um programa que leia um valor inteiro e que informe se este valor é par ou impar

x = int(input("Verificar se o numero e par ou impar: "))
if(x % 2 == 0):
    print(x, "e par")
else:
    print(x, "e impar")

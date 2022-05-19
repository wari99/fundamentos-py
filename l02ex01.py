#Elabore um algoritmo que leia 3 números do usuário e imprima-os em ordem crescente. 

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if(n1 >= n2 and n1 >= n3): 
    if(n2 >= n3):
        print(n3, n2, n1)
    if(n3 >= n2):
        print(n2, n3, n1)

if(n2 >= n1 and n2 >= n3):
    if(n1 >= n3):
        print(n3, n1,n2)
    if(n3 >= n1):
        print(n1, n3, n2)

if(n3 >= n1 and n3 >= n2):
    if(n1 >= n2):
        print(n2, n1, n3)
    if(n2 >= n1):
        print(n1, n2, n3)

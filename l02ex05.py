#Faça um algoritmo que leia a altura e o sexo de uma pessoa e escreva o seu peso ideal, utilizando as seguintes fórmulas:	
#para homens: (72,7 * altura) – 58,0 
#para mulheres: (62,1 * altura) – 44,7

altura = float(input("Altura em x.xx metros: "))
x = input("h (Homem) ou m (Mulher): ")

pesoideal = 0
 
if(x == "h"):
    pesoideal = (72.7 * altura) - 58
if(x == "m"):
    pesoideal = (62.1 * altura) - 44.7

print("Peso ideal em kg: ", pesoideal)
    

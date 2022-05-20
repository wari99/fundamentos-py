#Faça um algoritmo que leia a idade de um nadador e que calcule e mostre a sua categoria seguindo as regras:
#•Categoria Baby: até 4 anos    •Categoria Infantil: 5 – 10 anos  
#•Categoria Juvenil: 11 – 17 anos   •Categoria Máster: A partir de 18 anos

idade = int(input("Idade do nadador: "))

if(idade <= 4):
    print("Categoria Baby")

elif(idade > 4 and idade <= 10):
    print("Categoria Infantil")

elif(idade > 10 and idade <= 17):
    print("Categoria Juvenil")
    
else:
    print("Categoria Master")

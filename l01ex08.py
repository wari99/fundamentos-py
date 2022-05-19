#Faça um algoritmo que leia a base e a altura de um retângulo e escreva o seu perímetro, a sua área e a sua diagonal.
from math import sqrt

base = int(input("Base do retângulo: "))
altura = int(input("Altura do retângulo: "))

perimetro = (base*2) + (altura*2)
area = base * altura
diagonal = sqrt( (base)**2 + (altura)**2 )

print("Perimetro: ", perimetro)
print("Area: ", area)
print("Diagonal: ", diagonal)

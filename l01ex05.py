#14. Faça um programa que, dados pelo usuário os três coeficientes a, b e c de uma equação do 2º  grau, escreve os valores das raízes dessa equação.
from math import sqrt

print("Eq 2 grau: ax^2 + bx + c = 0")

a = int(input("Coeficiente a: "))
b = int(input("Coeficiente b: "))
c = int(input("Coeficiente c: "))

delta = (b)**2 - (4 * a * c)

x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b - sqrt(delta)) / 2 * a

print("Raizes: ", x1, " e ", x2)

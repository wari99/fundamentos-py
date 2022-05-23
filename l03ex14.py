#Faça um programa para calcular a área de um triângulo. Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.
base = altura = 0
area = 0 

base = int(input("Base do triangulo:  "))
altura = int(input("Altura do triangulo:  "))

if(base < 1 or altura < 1):
  print("Nao e possivel calcular. Base ou altura sao menores ou iguais a 0.")
else:
  print("Area do triangulo: ", (base * altura)/2)

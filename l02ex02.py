#Faça um programa que leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Mostrar na tela qual dos 
#professores tem salário total maior.


vprof1 = float(input("R$/h do professor 1: R$"))
vprof2 = float(input("R$/h do professor 2: R$"))

hprof1 = int(input("Horas trabalhadas professor 1: "))
hprof2 = int(input("Horas trabalhadas professor 2: "))

salprof1 = salprof2 = 0

salprof1 = vprof1 * hprof1
salprof2 = vprof2 * hprof2

if(salprof1 > salprof2):
    print("Professor 1 recebe mais que Professor 2.")

if(salprof2 > salprof1):
    print("Professor 1 recebe mais que Professor 1.")

print("Salario professor 1: R$ %.2f" % salprof1)
print("Salario professor 2: R$ %.2f" % salprof2)

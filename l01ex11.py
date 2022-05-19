#Faça um programa que calcule a quantia total dada uma porção de moedas. O programador deve dialogar com o usuário segundo o formato do exemplo abaixo:
#Número de moedas de 1 Real: 3    Número de moedas de 50 centavos: 3
#Número de moedas de 25 centavos: 1   Número de moedas de 10 centavos: 7
#Número de moedas de 5 centavos: 100    Número de moedas de 1 centavo: 13
#Quantia total calculada: R$ 10.58

mreal = int(input("Qtd de Moedas de 1 Real:"))
mcinq = int(input("Qtd de Moedas de 50 Centavos:"))
mvint = int(input("Qtd de Moedas de 25 Centavos:"))
mdez = int(input("Qtd de Moedas de 10 Centavos:"))
mcinco = int(input("Qtd de Moedas de 05 Centavos:"))
mum = int(input("Qtd de Moedas de 01 Centavo:"))

mcinq *= 0.5
mvint *= 0.25
mdez *= 0.1
mcinco *= 0.05
mum *= 0.01
total = 0

total = mreal + mcinq + mvint + mdez + mcinco + mum

print("Quantia total: R$", total)

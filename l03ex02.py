#Faça um programa que escreva os N primeiros termos de uma PA. O primeiro termo e a razão da PA devem ser lidos.

primeirotermo = int(input("1o Termo PA: "))
razao = int(input("Razao da PA: "))
qtdtermos = int(input("Qtd de termos: "))

i = 0

while(i != qtdtermos):
    print(primeirotermo + (razao * i))
    i += 1

#A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus trabalhadores. Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário. Faça um 
#programa que leia estes dados e que escreva ao final:	a média salarial dos homens, a média salarial das mulheres, o maior salário encontrado entre as pessoas abaixo de 30 anos.
#Obs: O final da leitura de dados é marcado por uma idade negativa.

totalh = totalm = 0
mediah = mediam = 0
qtdh = qtdm = 0
maiorsal = 0

idade = int(input("Idade: "))
while(idade > 0):
    sexo = input("Homem (digitar 'h') ou Mulher (digitar 'm'): ")
    if(sexo != 'm' and sexo != 'h'):
        print("Erro de digitacao! Digitar 'm' ou 'h'.")
        break
    salario = float(input("Salario: R$"))
    
    if(sexo == 'h'):
        totalh += salario
        qtdh += 1
    if(sexo == 'm'):
        totalm += salario
        qtdm += 1
    if(idade < 30 and salario > maiorsal):
        maiorsal = salario
    idade = int(input("Idade: "))
    
if(idade < 0):
    print("Final da leitura.")

mediah = totalh / qtdh
mediam = totalm / qtdm


print("Soma Salarios Homens: ", totalh, "Soma Salario Mulheres: ", totalm)
print("Qtd homens: ", qtdh, "Qtd Mulheres: ", qtdm)

print("Maior Salario (Abaixo de 30 anos): R$ %.2f" % maiorsal)
print("Media Salarial (Homens): R$%.2f" % mediah)
print("Media Salarial (Mulheres): R$%.2f" % mediam)

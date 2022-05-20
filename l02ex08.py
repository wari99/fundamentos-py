#A prefeitura da “Terra do Nunca” vai realizar suas eleições em urnas eletrônicas, sendo 3 os candidatos à prefeitura (Capitão Gancho, Peter Pan e Wendy). 
#Elabore um programa que permita ao usuário informar o número de votos de cada um dos candidatos, escrevendo em seguida o resultado da eleição. 
#Sabe-se que, caso um dos candidatos tenha mais de 50% dos votos ele é eleito sem necessidade de segundo turno. Na “Terra do Nunca” não existem votos nulos ou brancos.

a = int(input("Total Votos Capitao Gancho: "))
b = int(input("Total Votos Peter Pan: "))
c = int(input("Total Votos Wendy: "))

totalvotos = a + b + c

pa = (a * 100) / totalvotos
pb = (b * 100) / totalvotos
pc = (c * 100) / totalvotos

if(pa > pb and pa > pc):
    print("Capitao Gancho ganha a eleicao com %.2f%%." % pa)
if(pb > pa and pb > pc):
    print("Peter Pan ganha a eleicao com %.2f%%." % pb)
if(pc > pa and pc > pb):
    print("Wendy ganha a eleicao com %.2f%%." % pc)

if(pa > 50 or pb > 50 or pc > 50):
    print(" Nao ha necessidade de um segundo turno.")

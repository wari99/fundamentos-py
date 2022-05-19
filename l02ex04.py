#Faça um programa que leia o número de eleitores de um município, o número de votos brancos, nulos e validos. Calcule e escreva o percentual que cada um 
#representa em relação ao total de eleitores.

totaleleitores = int(input("Quantidade de eleitores na cidade: "))

vbrancos = int(input("Qtd de votos em branco: "))
vnulos = int(input("Qtd de votos nulos: "))
vvalidos = int(input("Qtd de votos validos: "))

pb = (vbrancos * 100)/ totaleleitores
pn = (vnulos * 100) / totaleleitores
pv = (vvalidos * 100) / totaleleitores

print("%.2f%% dos votos em branco" % pb)
print("%.2f%% dos votos nulos" % pn)
print("%.2f%% dos votos validos" % pv)

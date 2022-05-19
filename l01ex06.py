#Faça um algoritmo que leia os valores de horas, minutos e segundos e transforme tudo para segundo. EX: 3 horas 2 minutos 7 segundos	= 10927 segundos
totalhoras = int(input("Horas: "))
totalminutos = int(input("Minutos: "))
totalsegundos = int(input("Segundos: "))

auxhoras = totalhoras * 60 * 60
auxminutos = totalminutos * 60

totalsegundos += auxhoras + auxminutos

print("Total em segundos: ", totalsegundos)


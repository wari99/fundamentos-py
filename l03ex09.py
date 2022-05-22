#Faça um algoritmo que apure os votos de uma eleição presidencial onde concorreram três candidatos. A cidade possui 20000 eleitores. Os votos podem ser 1, 2, 3 e 4 
#e devem ser contados de acordo com a tabela: 1 – João da Silva  2 – José Ramalho 3 – Maria Mattos 4 – Voto em branco outros – Votos Nulo
#Calcule e escreva o total de votos de cada candidato, o total de votos brancos, o total de votos nulos e o nome do candidato que recebeu mais votos.

totaleleitores = 10
i = 1
voto1 = voto2 = voto3 = votoB = votoX = voto = 0
maisvotado = ''
print("1 – João da Silva\n2 – José Ramalho\n3 – Maria Mattos\n4 – Voto em branco outros\nOutro numero – Voto Nulo\n ")

for i in range(i, totaleleitores+1):
  voto = int(input("Voto eleitor %d: " % i))
  if(voto == 1):
    voto1 += 1
  elif(voto == 2):
    voto2 += 1
  elif(voto == 3):
    voto3 += 1
  elif(voto == 4):
    votoB += 1
  else:
    votoX += 1

if(voto1 > voto2 and voto1 > voto3):
  maisvotado = 'Joao da Silva'
elif(voto2 > voto1 and voto2 > voto3):
  maisvotado = 'Jose Ramalho'
elif(voto3 > voto1 and voto3 > voto2):
  maisvotado = 'Maria Mattos'

print("-----*----- TOTAL DE VOTOS -----*-----")
print("\nJoão da Silva: %d\nJosé Ramalho: %d\nMaria Mattos: %d\nVoto em branco: %d\nVotos Nulos: %d\n" % (voto1, voto2, voto3, votoB, votoX))
print("Candidato que recebeu mais votos: %s" % maisvotado)

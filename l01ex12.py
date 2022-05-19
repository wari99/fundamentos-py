#Faça um algoritmo que, dado o valor de um peso em libras, escreve o valor em gramas desse peso. O programa deve dialogar com o usuário segundo o formato do exemplo abaixo: (1 libra vale 453,59237g)
#Peso (em libras): 4.0
#Resposta: 1814g

pesolibra = int(input("Peso em libras: "))
pesograma = 0

pesograma += pesolibra * 453.59237

print(int(pesograma), " g")

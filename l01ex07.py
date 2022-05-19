#Faça um algoritmo que leia o valores em dias e imprima tudo em ano, meses e dias.

diasinicial = int(input("Total de dias: "))
auxanos = 0
auxmeses = 0

while(diasinicial >= 365):
    diasinicial -= 365
    auxanos += 1
    
while(diasinicial >= 31):
    diasinicial -= 31
    auxmeses += 1

auxdias = diasinicial

print("Anos: ", auxanos)
print("Meses: ", auxmeses)
print("Dias: ", diasinicial)

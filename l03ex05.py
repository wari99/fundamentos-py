#Faça um algoritmo que imprima o peso total que será carregado por um caminhão. Sabe- se que este caminhão carrega 25 caixas.
#O peso de cada caixa será informado pelo usuário.

i = total = caixa = 0

for i in range(i, 25):
  print("CAIXA ", i+1)
  caixa = float(input("Peso em kg:"))
  total += caixa
  
  i += 1

print("Peso total no caminhão, em kg: %.3f" % total)

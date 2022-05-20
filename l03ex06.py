#Faça um algoritmo que leia a quantidade e o preço de 50 produtos que foram comprados por uma empresa. Ao final deve ser escrito o total gasto pela empresa.

i = qtd = 0
preco = total = 0.0

for i in range(50):
  print("PRODUTO", i+1)
  qtd = int(input("Quantidade:"))
  preco = float(input("Preco: R$"))

  preco = preco * qtd
  total = total + preco

print("Total gasto: R$ %.2f" % total)

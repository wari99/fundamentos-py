#Faça um programa que leia os nomes e os preços dos produtos de uma loja e que escreva o nome do produto mais caro. Considere que o final da lista é marcado 
#pelo produto ‘XXX’ e que não existem preços repetidos.

maiscaro = 0
nomemaiscaro = ''

produto = input("Nome produto: ")

while(produto != 'XXX'):
  preco = float(input("Preco desse produto: "))
  
  if(preco >= maiscaro):
    maiscaro = preco
    nomemaiscaro = produto
    
  produto = input("Nome produto: ")
  
if(produto == 'XXX'):
  print("Fim da lista.")
  
print("Produto mais caro: ", nomemaiscaro)
print("Preco do produto mais caro: R$ %.2f" % maiscaro)

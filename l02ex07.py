#Faça um algoritmo que leia o preço de um produto, calcule o seu aumento e mostre a sua classificação.
#•Se o preço for menor ou igual a 50, o produto receberá um aumento de 5%
#•Se o preço for maior do que 50 e menor ou igual a 100, o aumento será de 10% 
#•Se o preço for maior do que 100, o aumento será de 15%
#A classificação do produto deve ser:	
#•Barato: até 80 reais (inclusive) •Normal: entre 80 reais e 120 reais (inclusive) 
#•Caro: entre 120 reais e 200 reais (inclusive) •Muito Caro: maior do que 200 reais

preco = float(input("Preço do produto: R$"))
precoatt = 0

if(preco <= 50):
    precoatt = preco * 1.05

elif(preco > 50 and preco <= 100):
    precoatt = preco * 1.1

else:
    precoatt = preco * 1.15

print("Preco atualizado: R$ %.2f" % precoatt)

if(precoatt <= 80):
    print("Classificacao: Barato")

elif(precoatt > 80 and precoatt <= 120):
    print("Classificacao: Normal")

elif(precoatt > 120 and precoatt <= 200):
    print("Classificacao: Caro")

else:
    print("Classificacao: Muito Caro")

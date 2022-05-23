#Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber se os consumidores estavam satisfeitos, para isso eles deveriam responder sim (S) ou não (N). 
#Faça um programa que leia a resposta de todas pessoas e escreva a porcentagem dos que disseram sim e dos que disseram não.
#Obs: O final da leitura de dados é marcado pela resposta ‘F’.

resposta = input("Esta satisfeito\n[S] ou [N]?")
respsim = respnao = 0
ps = pn = total = 0.0

while(resposta != 'F' and resposta != 'f'):
  if(resposta == 'S' or resposta == 's'):
    respsim += 1
  if(resposta == 'N' or resposta == 'n'):
    respnao += 1
  resposta = input("Esta satisfeito\n[S] ou [N]?")

if(resposta == 'F' or resposta == 'f'):
  print("Fim da leitura.")

print("Quantidade N: % d Quantidade S: % d" % (respsim, respnao))

total = respsim + respnao
ps = (respsim * 100) / total
pn = (respnao * 100) / total

print("Porcentagem S: %.2f%%" % ps)
print("Porcentagem N: %.2f%%" % pn)

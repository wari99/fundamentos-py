#O presidente de um país sul-americano quer investir em saúde, educação, habitação, segurança e
#previdência, que são as cinco metas de seu governo. Assim, o presidente decide criar mais um
#imposto, o ISSS (Imposto Sobre Seu Saldo), que é calculado sobre o saldo médio da contacorrente, segundo a tabela abaixo:
#• Saldo < 100: isento
#• 100 ≤ Saldo < 1000: imposto devido é 1% sobre o saldo
#• 1000 ≤ Saldo < 10000: imposto devido é de 2% sobre o saldo
#• 10000 ≤ Saldo < 100000: imposto devido é de 3% sobre o saldo
#• Saldo ≥ 100000: imposto devido é de 5% sobre o saldo
#Faça um programa que permita ao usuário informar seu saldo bancário e que escreva o ISSS devido. 

saldo = float(input("Informe o saldo bancario: R$"))
imposto = 0

if(saldo < 100):
    print("Esta isento de pagar o ISSS")

elif(saldo >= 100 and saldo < 1000):
    imposto = saldo * 0.01
    print("Com o imposto, deve pagar R$ %.2f de ISSS" % imposto)

elif(saldo >= 1000 and saldo < 10000):
    imposto = saldo * 0.02
    print("Com o imposto, deve pagar R$ %.2f de ISSS" % imposto)

elif(saldo >= 10000 and saldo < 100000):
    imposto = saldo * 0.03
    print("Com o imposto, deve pagar R$ %.2f de ISSS" % imposto)

else:
    imposto = saldo * 0.05
    print("Com o imposto, deve pagar R$ %.2f de ISSS" % imposto)

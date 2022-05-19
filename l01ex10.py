#João recebeu seu salário e precisa pagar duas contas atrasadas. Como as contas estão atrasadas, João deverá pagar uma multa de 2% sobre cada uma. 
#Faça um algoritmo que leia o valor do salário de João e das contas que ele deve pagar, e que mostre quanto restará do seu salário após o pagamento das contas.

saljoao = float(input("Salario do Joao: R$"))

conta1 = float(input("Valor da 1a conta: R$"))
conta2 = float(input("Valor da 2a conta: R$"))

conta1 *= 1.02
conta2 *= 1.02

totalcontas = conta1 + conta2

restosal = saljoao - totalcontas

print("Total contas com 2% de multa cada: R$", totalcontas)
print("Restou do salario do Joao apos o pagamento: R$", restosal)

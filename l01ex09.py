#Um funcionário recebe um salário fixo mais 4% de comissão sobre as suas vendas. Faça um algoritmo que receba o valor do salário
#fixo do funcionário, o valor das suas vendas e que calcule e mostre o salário final do funcionário.

salfixo = float(input("Salario base: R$"))
valorvendas = float(input("Vendas do funcionario: R$"))

comissao = valorvendas * 0.04

salatt = salfixo + comissao

print("O Salario adicionado 4% de comissao e R$", salatt)

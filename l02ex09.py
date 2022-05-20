#Uma loja de bicicletas paga a cada vendedor 2 salários mínimos mensais, mais uma comissão de 5% sobre as vendas das bicicletas, dividida igualmente entre eles. Escreva 
#um programa que leia o número de empregados da loja, o valor do salário mínimo, o valor das vendas do mês e que calcule e escreva: o salário total de cada empregado

fixo = float(input("Salario Minimo: R$"))
qtdfunc = int(input("Qtd funcionarios na loja: "))
totalvendas = float(input("Total vendido em bicicletas: R$"))

fixo = fixo * 2
comissao = (totalvendas * 0.05) / qtdfunc
auxqtdfunc = qtdfunc
salario = 0

while(auxqtdfunc != 0):
    salario = fixo + comissao
    print("Salario Empregado ", auxqtdfunc, ":R$ %.2f" % salario)

    auxqtdfunc -= 1
    salario = 0

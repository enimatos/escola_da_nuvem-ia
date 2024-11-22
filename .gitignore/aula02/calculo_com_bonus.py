nome_vendedor = str(input("Digite o nome do vendedor: "))

salario_fixo = float(input("Digite o salário do vendedor: "))
vendas = float(input("Digite o valor total das Vendas: "))
comissao = float(input("Digite o valor da comissão: "))

total = salario_fixo + (vendas * comissao)
print(f"O valor s receber do colaborador {nome_vendedor} é fr R$ {total:.2f}")
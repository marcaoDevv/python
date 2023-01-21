qtd_vendas_coca = 150
qtd_vendas_pepsi = 130
preco_unit_coca = 1.50
preco_unit_pepsi = 1.50
custo_loja = 2500

# Faturamento de Pepsi da loja
print(qtd_vendas_pepsi * preco_unit_pepsi)

# Faturammento de coca da loja
print(qtd_vendas_coca  * preco_unit_coca)

# Lucro da loja
faturamento = qtd_vendas_coca * preco_unit_coca + qtd_vendas_pepsi * preco_unit_pepsi
lucro = faturamento - custo_loja
print(lucro)

# Margem da loja
print(lucro/faturamento)

vendas_funcionario1 = 1000
vendas_funcionario2 = 700
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
    print('O funcionário 1 ganhou {} de bônus' .format(vendas_funcionario1 * 0.1))

if vendas_funcionario2 >= 1000:
    bonus = vendas_funcionario2 *  0.1
else:
    bonus = 0
print('O funcionário 2 ganhou {} de bônus' .format(bonus))

if vendas_funcionario3 >= 1000:
    bonus = vendas_funcionario3 * 0.1
else:
    bonus = 0
print('O funcionário 3 ganhou {} de bônus' .format(bonus))
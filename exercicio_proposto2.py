"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma
poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho
com juros no período.
"""

deposit = int(input("Qual será o valor do depósito? "))
poupanca = float(input("Qual a taxa de juros da poupança? "))
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

for mes in meses:
    for salario in range(1, 25):
        deposit += deposit * poupanca
    print(f'{mes} = {deposit:.2f}')
    


print(f'Total ganho: {deposit:.2f}')
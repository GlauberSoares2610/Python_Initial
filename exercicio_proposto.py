"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja
realizar . Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão
(/). Exiba o resultado da operação solicitada.
"""
numero_1 = ''
numero_2 = ''
resultado = ''

while True:

    numero_1 = int(input('Digite um numero: '))
    numero_2 = int(input('Digite outro numero: '))
    
    operacao = input('Qual operação deseja realizar +, -, * ou /: ')

    if operacao == '+':
        resultado = numero_1 + numero_2
        print(f'Total: {resultado}')
        break
    
    elif operacao == '-':
         resultado = numero_1 + numero_2
         print(f'Total: {resultado}')
         break
    
    elif operacao == '*':
         resultado = numero_1 + numero_2
         print(f'Total: {resultado}')
         break

    elif operacao == '/':
        resultado = numero_1 + numero_2
        print(f'Total: {resultado}')
        break
    
    else:
        print('Você digitou incorretamente! Tente de novo por favor.')
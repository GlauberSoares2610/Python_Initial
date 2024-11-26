"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

valores = []

while True:
      try:   
         print('Selecione uma opção: ')
         letra = input('[I]nserir, [A]pagar, [L]istar ou [S]air: ')
         
         if letra == 'I':
            valor = input('Valor: ')
            valores.append(valor)
       
         elif letra == 'A':
            valor = input('Valor: ')
            valores.remove(valor)
        
         elif letra == 'L':
            print(valores)
         elif letra == 'S':
            print('Você encerrou o programa, obrigado!')
            break
         else:
            print('Você não digitou as opções corretas! Tente novamente!')
      except:
         ValueError = print('Valor inexistente, tente novamente!')

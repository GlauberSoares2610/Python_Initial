"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome ou idade forem digitados:
.... Exiba:
....... Seu nome é {nome}
....... Seu nome invertido é {nome invertido}
....... Se o nome contém (ou não) espaços
....... Seu nome tem {n} letras
....... A primeira letra do seu nome é {letra}
....... A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
.... Exiba: "Desculpe, você deixou campos vazios."
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome or idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome invertido é {nome[-1:-10:-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome NÃO contém espaços!')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpa, você deixou campos vazios.')

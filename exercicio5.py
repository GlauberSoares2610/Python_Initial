"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
1) Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
2) Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    a) Se a letra digitada estiver na palavra secreta; exiba a letra;
    b) Se a letra digitada não estiver na palavra secreta; exiba *
3) Faça a contagem de tentativas do seu usuário.
"""

import os

palavra_secreta = input('Digite a palavra secreta: ')
letras_acertadas = ''
tentativa = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta    
        else:
            palavra_formada += '*'
    print(palavra_formada)
    tentativa += 1
    print('tentativas: ', tentativa)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'PARABÉNS, Você completou a palavra secreta *{palavra_secreta}* com {tentativa} tentativas')
        break
    


    
    


    """elif letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        print(letras_acertadas)
        tentativa += 1
        print('Tentativas: ', tentativa)

    elif letra_digitada != palavra_secreta:
        letras_acertadas += '*'
        print(letras_acertadas)
        tentativa += 1
        print('Tentativas: ', tentativa)
    
    """
# criasse constantes com letra maiusculas, mas, não existe constante em python
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False # variavel de controle
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', texto)
        
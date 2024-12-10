def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens): # packing
    # <li>{item}</li> - O que irá ser gerado
    # for item in itens - irá obter o valor do argumento passado ao parametro e colocar na variavel item, e irá repetir esse laço de repetição na quantidade de argumentos que foi passado
    lista = ''.join((f'<li>{item}</li>' for item in itens)) # join concatena
    return f'<ul>{lista}</ul>'


 
if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classe', 'info', True))
    print(tag_bloco('inline', inline=True)) # params nomeados troca de posição
    print(tag_bloco(inline=True, conteudo='inline'))
    print(tag_bloco('falhou', classe='error'))
    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
    
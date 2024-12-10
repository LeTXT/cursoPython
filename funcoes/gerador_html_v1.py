def tag_bloco(texto, classe='success'): # classe é um parametro opcional # caso não seja passado nada para o parametro, ela recebe o argumento success
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions) caso o caso seja verdadeiro passo, caso ser falso ele gera um erro
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
    print(tag_bloco('bloco'))
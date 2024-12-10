def todos_params(*args, **kwargs):
    # pega os argumentos/parametros da funcao de uma forma genérica
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    # params posicionais, parou dentro de args
    todos_params('a', 'b', 'c') # gerou uma tupla
    # params posicionais e nomeados, nomeados pararam no kwards
    # gerando um dicionário
    todos_params(1, 2, 3, legal=True, valor=12.99)
    todos_params('Ana', False, [1, 2, 3], tamanho='M', fragil=False)
    # todos_params(primeiro='João', 'Maria') # dá problema
    todos_params(primeiro='João', segundo='Maria')
    todos_params('Maria', primeiro='João')

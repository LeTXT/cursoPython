#0, 1, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(quantidade, sequencia=(0, 1)): 
    #importante: Condição de parada
    # expressão condicional ou operação ternária
    # valor_se_verdadeiro if condicao else valor_se_falso
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))



if __name__ == '__main__':
    # listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)

#0, 1, 1, 2, 3, 5, 8, 13, 21...

# resultado = [0, 1]

#sequencia=(0, 1) é um parametro padrão
def fibonacci(quantidade, sequencia=(0, 1)): # tupla # na primeira chamada vai assumir a sequencia 0 e 1
    #importante: Condição de parada
    
    if len(sequencia) == quantidade:
        return sequencia
    # sequencia concatena a soma gerada pelos dois ultimos numeros # tem que se colocar a virgula # soma de tupla e se cria uma nova tupla # chama-se de sobrecarga de operador
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))



if __name__ == '__main__':
    # listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)

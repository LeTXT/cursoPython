# recursivo chama ele mesmo
def imprimir(maximo, atual):
    # condição de parada
    # if atual < maximo:
    #     print(atual)
    #     imprimir(maximo, atual + 1)
    if atual >= maximo:
        return # não vai retornar nenhum valor
    print(atual)
    # chama-se de novo, mas, passando parametros diferentes
    imprimir(maximo, atual + 1)

# pode se substituir um laço por uma implementação recursiva
imprimir(10, 1)
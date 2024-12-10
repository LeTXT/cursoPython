def fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis com valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    # o mesmo objeto em memória
    print(restart, id(restart))
    # não é interessante colocar objetos mutaveis como parametro padrão
    assert restart == [0, 1, 1]

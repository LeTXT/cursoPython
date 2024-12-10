#0, 1, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < limite:
        # a, b = b, a
        penultimo, ultimo = ultimo, penultimo + ultimo # ele vai fazer a troca sem que faça o penultimo ter o valor igual ao ultimo, antes de terminar a troca
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci(20000)
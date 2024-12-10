def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c

# gera empacotamento # se passo vários argumentos, são criados paramentros de acordo com quantos argumentos foi colocado
# pega todos os atributos, e coloca dentro de uma tupla # PACKING
def soma_n(*numeros):
    print(type(numeros))
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(1, 2))
    print(soma_3(1, 2, 2))
    # PACKING
    print(soma_n(1))
    print(soma_n(1, 1))
    print(soma_n(1, 1, 1, 1, 1, 1, 1))
    # UNPACKING
    #desempacotamento unpacking, vai desempacotar a tupla (pode ser lista), e vai usar os valores como argumentos da função
    tupla_nums = (1, 2, 3)
    print(soma_3(*tupla_nums))

    lista_nums = [4, 5, 6]
    print(soma_3(*lista_nums))

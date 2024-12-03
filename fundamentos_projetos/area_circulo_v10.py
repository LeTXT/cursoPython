from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2
    

if  __name__ == '__main__':
    # usa os argumentos a partir do sys
    # argv[0] nome do script
    # argv[1] parametro passado
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)

from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2
    

if  __name__ == '__main__':
    if len(sys.argv) < 2:
        print('É necessário informar o raio do círculo.')
        # [2:] tira as primeiras duas letras
        print(f'Sintaxe: {sys.argv[0][2:]} <raio>')
            
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)

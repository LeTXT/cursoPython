from math import pi
import sys


# é um algoritmo que segue uma sequência de passos que não rebece nada e não retorna nada # não tem parametro ou return
def help():
    print('É necessário informar o raio do círculo.')
    print(f'Sintaxe: {sys.argv[0][2:]} <raio>')


def circulo(raio):
    return pi * float(raio) ** 2
    

if  __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
            
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)

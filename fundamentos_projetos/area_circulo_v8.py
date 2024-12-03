from math import pi

# palavra reservado para função def = definida
# função é um algoritmo que tem um nome, uma sequencia de passos, um bloco, é comum
# se passa parametros nos parenteses
# imprimir no console não é o mesmo que retornar algo
def circulo(raio):
    print(f'area da circunferência é {pi * float(raio) ** 2}')
    

if  __name__ == '__main__':
    raio = input('digite o valor do raio: ')
    circulo(raio)

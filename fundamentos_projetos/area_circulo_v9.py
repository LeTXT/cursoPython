from math import pi

# agora pode ser usada para calcular outras areas, não apenas imprimir 
def circulo(raio):
    return {pi * float(raio) ** 2}
    

if  __name__ == '__main__':
    raio = input('digite o valor do raio: ')
    area = circulo(raio)
    print('Área do círculo', area)

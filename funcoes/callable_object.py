class Potencia:
    # Calcula uma potência específica 
    # __init__ é um construtor
    def __init__(self, expoente): # metódos que pertencem uma classe pertecem a uma instância atual
        # self é um onjeto que foi criado a partir da classe potência
        self.expoente = expoente

    # objeto que será chamado como uma função
    def __call__(self, base):
        return base ** self.expoente
    

if __name__ == '__main__':
    quadrado = Potencia(2) # não repcisa chamar o self e call será chamado inplicitamente
    cubo= Potencia(3)
    # a função potencia se torna callable por conta da ter a função mágica especial __call__ 
    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'5³ => {quadrado(5)}')
        print(Potencia(4)(2)) # 2 elevado a 4

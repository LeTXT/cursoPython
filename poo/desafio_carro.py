class Carro():
    def __init__(self, max, speed):
        self.max = max
        self.speed = speed

    def acelerar(self, max, increment):
        self.speed += increment if self.speed < max else _
        return self.speed



if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))
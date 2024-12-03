# while True:
#     print('Vai demorar muito')


# gera um valor aleatório entre um valor inicial e final # inteiro
from random import randint 

numero_informado = -1
numero_secreto = randint(0, 9)

# se usa o laço while quando há uma quantidade indeterminada de repetições
# usar quando tem interação com o usuário
while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))

print(f'Número secreto {numero_secreto} foi encontrado')

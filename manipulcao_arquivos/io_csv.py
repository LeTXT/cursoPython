import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        # o modulo quebra as linhas e os atributos separados por vingula
        # * operador de argumentos variados, ele foi interpolado pela string
        print('Nome: {}, Idade: {}'.format(*pessoa))
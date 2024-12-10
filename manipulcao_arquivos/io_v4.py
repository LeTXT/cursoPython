

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))
# nesse caso vai haver a execução do finally e do if sem o except não
# except IndexError:
#     pass # palavra reservada do python para um bloco vázio
finally:
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo já foi fechado!')
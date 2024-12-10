import csv

# with open('desafio-ibge.csv') as ibge:
#     for ibges in csv.reader(ibge):
#         print('{}'.format(*ibge))

from urllib import request
# request abre uma url, não precisa usar o arquivo local

def read(url):
    # ao invés de pegar um arquivo local abre um arquivo por requisição
    # abrindo remotamente
    with request.urlopen(url) as entrada:
        print('Baixando o CSV...')
        # decode lê os arquivos de forma correta
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        # para cada uma das linhas vai ser lido e transformar em uma cidade
        # a partir da cidade conseguira acessar qualquer coluna
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    # o r faz uma interpretação crua do que está entre parenteses
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

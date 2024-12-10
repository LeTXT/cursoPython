
# segundo primeiro params é o nome do arquivo e o segundo é o modo de
# de usar
with open('pessoas.csv') as arquivo:
    # nesse caso w é escrita writing
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # ao inves de escrever dentro do console, vai ser escrito em um arquivo
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)

# foi fechado por conta do bloco with
if arquivo.closed:
    print('Arquivo já foi fechado!')

if saida.closed:
    print('Arquivo de saida já foi fechado!')

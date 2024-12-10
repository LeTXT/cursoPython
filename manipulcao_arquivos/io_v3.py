# mais otimizado
arquivo = open('pessoas.csv')
# strip tira espaços por padrão mas strip('0') tira os 0's da borda
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()

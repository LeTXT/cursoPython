# mais otimizado
arquivo = open('pessoas.csv')
# lê o arquivo sob demanda # streaming # bom para arquivos grandes
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
    
arquivo.close()

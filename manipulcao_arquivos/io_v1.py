# Comma-Separated Values (valores separados por vírgulas)
# * tira de dentro da tupla lista etc na ordem o arquivo não tendo necessida de usar value[0] value[1] como o operador spread do js

arquivo = open('pessoas.csv') # está no builtins
dados = arquivo.read() # pegou o arquivo que vai pra memória do pc
arquivo.close() # fechou o arquivo

for registro in dados.splitlines(): # cada uma das linhas separadas
    print('Nome: {}, Idade: {}'.format(*registro.split(','))) 
    # resultado que será feito na variavel não é diretamente do registro
    # e sim do resultado de registro
    # interpolação
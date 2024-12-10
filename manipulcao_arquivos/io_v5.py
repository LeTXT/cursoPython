
# dentro do bloco arquivo pessoas.csv vai referenciar o arquivo 
# pessoas.csv como arquivo 
# nesse caso é garantido que o recurso que foi realocado do bloco 
# vai fechar
# pode ser usado quando recursos do Sistema operacional está sendo usado
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))

# foi fechado por conta do bloco with
if arquivo.closed:
    print('Arquivo já foi fechado!')

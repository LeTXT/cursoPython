# **kwargs keywords argument # argumentos nomeados
def resultado_f1(**podium):
    for posicao, piloto in podium.items(): # items retorna a chave e o valor # posicao recebe a chave e o piloto recebe o valor
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    # packing pega todos os parametros nomeados, junto dentro de um dicionário, e passa para dentro de uma função
    # os nomes de argumentos são usados como chave arg primeiro a chave também será primeiro
    resultado_f1(primeiro='L. Hamilton',
                 segundo='M. Verstappen',
                 teceiro='S. Vettel')
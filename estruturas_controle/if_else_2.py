def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65): # vai até 64
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'
    

# se tem um módulo que quer importar para outros módulos, e também quer executar quando chamado no módulo principal é importate usar essa condição
if __name__ == '__main__':
    for idade in (17, 35, 87, 113, -2): # tupla
        print(f'{idade}: {faixa_etaria(idade)}') # interpolação # interpretação

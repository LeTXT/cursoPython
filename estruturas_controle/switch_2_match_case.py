# def get_dia_semana(dia):
#     dias = {
#         1: 'Domingo',
#         2: 'Segunda',
#         3: 'Terça',
#         4: 'Quarta',
#         5: 'Quinta',
#         6: 'Sexta',
#         7: 'Sábado',
#     }
#     return dias.get(dia, '** inválido **')

# if __name__ == '__main__':
#     for dia in range(0, 9):
#         if dia in range(2, 7):
#             print(get_dia_semana(dia) + ' dia da semana')
#         elif dia == 1 or dia == 7:
#             print(get_dia_semana(dia) + ' final de semana')
        
#         else:
#             print(get_dia_semana(dia))


# def get_tipo_dia(dia):
#     dias = {
#         1: 'Fim de semana',
#         2: 'Dia de semana', 
#         3: 'Dia de semana', 
#         4: 'Dia de semana', 
#         5: 'Dia de semana', 
#         6: 'Dia de semana', 
#         7: 'Fim de semana',
#     }
#     return dias.get(dia, 'Dia inválido')


# # testa se está em um módulo principal
# if __name__ == '__main__':
#     for dia in range(8): # range(0, 9) mesma coisa
#         print(f'{dia}: {get_tipo_dia(dia)}')


def get_tipo_dia(dia):
    match dia:
        case 2 | 3 | 4 | 5 | 6 :
            return 'Dia de semana'
        case 1 | 7:
            return 'Fim de semana'
        case _:
            return '** inválido **'
            
 
 
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
        
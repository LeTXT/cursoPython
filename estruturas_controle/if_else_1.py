# Conceitos    Notas
# A            De 10 à 9,1
# A-           De 9,0 à 8,1
# B            De 8,0 à 7,1
# B-           De 7,0 à 6,1
# C            De 6,0 à 5,1
# C-           De 5,0 à 4,1
# D            De 4,0 à 3,1
# D-           De 3,0 à 2,1
# E            De 2,0 à 1,1
# E-           De 1,0 à 0,0

# *Para notas maiores de 10 e menores que 0 será impresso 'Nota Inválida'

import sys


def notaPassada(nota):
    if nota == 10 and nota >= 9.1:
        print('A')
        return
        # return 'A'
    if nota == 9 and nota >= 8.1:
        print('A-')
        return
        # return 'A-'
    if nota == 8 and nota >= 7.1:
        print('B')
        return
        # return 'B'
    if nota == 7 and nota >= 6.1:
        print('B-')
        return
        # return 'B-'
    if nota == 6 and nota >= 5.1:
        print('C')
        return
        # return 'C'
    if nota == 5 and nota >= 4.1:
        print('C-')
        return
        # return 'C-'
    if nota == 4 and nota >= 3.1:
        print('D')
        return
        # return 'D'
    if nota == 3 and nota >= 2.1:
        print('D-')
        return
        # return 'D-'
    if nota == 2 and nota >= 1.1:
        print('E')
        return
        # return 'E'
    if nota == 1 and nota >= 0:
        print('E-')
        return
        # return 'E-'
    else:
        print('Nota inválida')


if __name__=="__main__":
    nota = sys.argv[1]
    notaPassada(float(nota))
# usar quando tem uma quantidade determinada
for i in range(1, 11):
    print(f'i = {i}')

for j in range(10): # diz apenas a quantidade de repetição # respeita o indice
    print(f'j = {j}')

for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
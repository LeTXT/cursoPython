# [ expressão for intem in list ]
# concisa
dobros = [i * 2 for i in range(10)]
print(dobros)

# Versão 'normal'
dobros = []
for i in range(10):
    dobros.append(i * 2)
print(dobros)
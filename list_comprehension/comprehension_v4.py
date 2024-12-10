generator = (i ** 2 for i in range(10) if i % 2 == 0)
# forma mais eficiente
# range
# xrange
for numero in generator:
    print(numero)

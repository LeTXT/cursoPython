for x in range(1, 11):
    if x % 2 == 0: # vê se é par
        continue # interrompe a interação e vai pra próxima # interrompe o bloco for, mas, não sai do laço
    print(x)

for x in range(1, 11):
    if x == 5:
        break # quando x for verdadeiro sai do laço
    print(x)
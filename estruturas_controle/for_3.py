produto = {'nome': 'Caneta Chic', 'preco': 14.99, 'importada': True, 'estoque': 793}

# por padrão irá acessar a chave
# pode se acessar produto.keys()
for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')

# os valores continuam disponiveis depois do laço acabar
print(chave, valor)
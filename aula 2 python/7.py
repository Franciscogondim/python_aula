lotes = int(input("Quantidade de lotes: "))
soma = 0
for i in range(lotes):
    item = int(input(f'Quantidade de itens no lote {i+1}: '))
    print(f"Lote {i+1} cadastrado com {item} itens")
    soma += item
print(f'Foram adicionados {soma} itens ao estoque')

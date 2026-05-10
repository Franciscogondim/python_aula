quantidade = int(input('Quantas compras foram feitas?: '))
soma = 0
for i in range(quantidade):
    valor = float(input(f'Digite o Valor do produto {i+1}: '))
    print("Valor cadastrado:", int(valor))   
    soma += valor 
print(f"foi faturado {soma} reais")

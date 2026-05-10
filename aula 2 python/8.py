viagem = int(input('Viagens feitas: '))
soma = 0
for i in range(viagem):
    entregas = int(input(f'Quantidade de entregas na viagem número {i+1} :'))
    soma += entregas 
media = int(soma/viagem)
print(f'A média de entregas por viagem é {media}.')
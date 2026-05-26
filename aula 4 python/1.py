cadastro = []
salario = []
print('cadastrar - opção 1')
print('Ver cadastros - opção 2')
print('Remover cadastro - opção 3')
print('Parar - opção 0')
print('==================================')
opcao = int(input('Opção: '))

while opcao != 0:
    match opcao:
        case 1:
            cadastrado = str(input('Nome: '))
            dinheiro = float(input('Salário: '))
            cadastro.append(cadastrado)
            salario.append(dinheiro)
        case 2:
            for nome, renda in zip(cadastro, salario):
                print(f'Nome:{nome} Salário:{renda}')
        case 3:
            nome_remover = str(input('Nome que deseja remover: '))
            if nome_remover in cadastro:
                indice = cadastro.index(nome_remover)
                cadastro.pop(indice)
                salario.pop(indice)
        case 0:
            break
        case _:
            print('Opção inválida')
    print('==================================')
    print('cadastrar - opção 1')
    print('Ver cadastros - opção 2')
    print('Remover cadastro - opção 3')
    print('Parar - opção 0')
    print('==================================')
    opcao = int(input('Opção: '))



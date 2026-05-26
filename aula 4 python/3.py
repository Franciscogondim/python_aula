cadastro = []
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
            funcionario = {
                'nome': cadastrado,
                'Salário': dinheiro
            }
            cadastro.append(funcionario)
        case 2:
            for funcionario in (cadastro):
                print(cadastro)
        case 3:
            nome_remover = str(input('Nome que deseja remover: '))
            for funcionario in cadastro:
                if funcionario['nome'] == nome_remover:
                    cadastro.remove(funcionario)
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

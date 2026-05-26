produtos = []
print('cadastrar - opção 1')
print('Ver cadastros - opção 2')
print('Remover cadastro - opção 3')
print('Parar - opção 0')
print('==================================')
opcao = int(input('Opção: '))
while opcao != 0:
    match opcao:
        case 1:
            cadastrado = str(input('Produto: '))
            quantidade = int(input('Quantidade: '))
            dinheiro = float(input('Valor: '))
            estoque = {
                'produto': cadastrado,
                'quantidade': quantidade,
                'Valor': dinheiro
            }
            produtos.append(estoque)
            
        case 2:
            for produto in(produtos):
                print(produtos)
        case 3:
            nome_remover = str(input('Produto que deseja remover: '))
            for produto in produtos:
                if produto['produto'] == nome_remover:
                    produtos.remove(produto)
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
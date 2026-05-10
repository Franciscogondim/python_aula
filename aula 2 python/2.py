login = str('admin')
senha = str('1234')
login_input = str(input('Login: '))
senha_input = str(input('Senha: '))
while login_input != login or senha_input != senha:
    print('Senha ou login incorretos!')
    login_input = str(input('Login: '))
    senha_input = str(input('Senha: '))
print('Acesso liberado')
    
pacientes = []
medicos = []
consultas = []
 

qtd_medicos = int(input("Quantidade de médicos: "))
for i in range(qtd_medicos):
    medico = {
        "id": i + 1,
        "nome": input("Nome do médico: "),
        "crm": input("CRM: "),
        "especialidade": input("Especialidade: "),
        "telefone": input("Telefone: "),
        "email": input("Email: ")
    }
    medicos.append(medico)
 

qtd_pacientes = int(input("Quantidade de pacientes: "))
for i in range(qtd_pacientes):
    paciente = {
        "id": i + 1,
        "nome": input("Nome do paciente: "),
        "cpf": input("CPF: "),
        "data_nascimento": input("Data de nascimento (DD/MM/AAAA): "),
        "telefone": input("Telefone: "),
        "email": input("Email: "),
        "endereco": input("Endereço: ")
    }
    pacientes.append(paciente)
 

qtd_consultas = int(input("Quantidade de consultas: "))
for i in range(qtd_consultas):
    print("Pacientes disponíveis:")
    for paciente in pacientes:
        print(paciente["id"], "-", paciente["nome"])
    id_paciente = int(input("Escolha o ID do paciente: "))
 
    print("Médicos disponíveis:")
    for medico in medicos:
        print(medico["id"], "-", medico["nome"], "|", medico["especialidade"])
    id_medico = int(input("Escolha o ID do médico: "))
 
    consulta = {
        "id": i + 1,
        "data": input("Data da consulta (DD/MM/AAAA): "),
        "hora": input("Hora da consulta (HH:MM): "),
        "observacao": input("Observação: "),
        "id_paciente": id_paciente,
        "id_medico": id_medico
    }
    consultas.append(consulta)
 
 

 
print("\n===== RELATÓRIO DE CONSULTAS =====")
for consulta in consultas:
    nome_paciente = ""
    nome_medico = ""
    especialidade_medico = ""
 
    for paciente in pacientes:
        if paciente["id"] == consulta["id_paciente"]:
            nome_paciente = paciente["nome"]
 
    for medico in medicos:
        if medico["id"] == consulta["id_medico"]:
            nome_medico = medico["nome"]
            especialidade_medico = medico["especialidade"]
 
    print("----------------------------------")
    print("Consulta ID:", consulta["id"])
    print("Paciente:", nome_paciente)
    print("Médico:", nome_medico)
    print("Especialidade:", especialidade_medico)
    print("Data:", consulta["data"])
    print("Hora:", consulta["hora"])
    print("Observação:", consulta["observacao"])
print("==================================\n")
 
 

 
id_update = int(input("Digite o ID da consulta para atualizar: "))
for consulta in consultas:
    if consulta["id"] == id_update:
        print("Dados atuais:")
        print("Data:", consulta["data"])
        print("Hora:", consulta["hora"])
        print("Observação:", consulta["observacao"])
        consulta["data"] = input("Nova data (DD/MM/AAAA): ")
        consulta["hora"] = input("Nova hora (HH:MM): ")
        consulta["observacao"] = input("Nova observação: ")
        print("Consulta atualizada!")
 
 

 
id_delete = int(input("Digite o ID da consulta para deletar: "))
encontrado = False
for consulta in consultas:
    if consulta["id"] == id_delete:
        consultas.remove(consulta)
        print("Consulta removida!")
        encontrado = True
        break
if not encontrado:
    print("Consulta não encontrada")
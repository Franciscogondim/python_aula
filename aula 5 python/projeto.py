pacientes = []
medicos = []
consultas = []

while True:

    print("\n===== CLÍNICA =====")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Pacientes")
    print("3 - Atualizar Paciente")
    print("4 - Excluir Paciente")

    print("\n5 - Cadastrar Médico")
    print("6 - Listar Médicos")
    print("7 - Atualizar Médico")
    print("8 - Excluir Médico")

    print("\n9 - Cadastrar Consulta")
    print("10 - Listar Consultas")
    print("11 - Atualizar Consulta")
    print("12 - Excluir Consulta")

    print("\n0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    # CREATE PACIENTE
    if opcao == "1":

        paciente = {
            "id": len(pacientes) + 1,
            "nome": input("Nome: "),
            "cpf": input("CPF: "),
            "telefone": input("Telefone: "),
            "email": input("Email: ")
        }

        pacientes.append(paciente)
        print("Paciente cadastrado!")

    # READ PACIENTE
    elif opcao == "2":

        for paciente in pacientes:
            print("\nID:", paciente["id"])
            print("Nome:", paciente["nome"])
            print("CPF:", paciente["cpf"])
            print("Telefone:", paciente["telefone"])
            print("Email:", paciente["email"])

    # UPDATE PACIENTE
    elif opcao == "3":

        id_update = int(input("ID do paciente: "))

        for paciente in pacientes:
            if paciente["id"] == id_update:

                paciente["telefone"] = input("Novo telefone: ")
                paciente["email"] = input("Novo email: ")

                print("Paciente atualizado!")
                break

    # DELETE PACIENTE
    elif opcao == "4":

        id_delete = int(input("ID do paciente: "))

        for paciente in pacientes:
            if paciente["id"] == id_delete:

                pacientes.remove(paciente)
                print("Paciente removido!")
                break

    # CREATE MEDICO
    elif opcao == "5":

        medico = {
            "id": len(medicos) + 1,
            "nome": input("Nome: "),
            "crm": input("CRM: "),
            "especialidade": input("Especialidade: "),
            "telefone": input("Telefone: ")
        }

        medicos.append(medico)
        print("Médico cadastrado!")

    # READ MEDICO
    elif opcao == "6":

        for medico in medicos:
            print("\nID:", medico["id"])
            print("Nome:", medico["nome"])
            print("CRM:", medico["crm"])
            print("Especialidade:", medico["especialidade"])
            print("Telefone:", medico["telefone"])

    # UPDATE MEDICO
    elif opcao == "7":

        id_update = int(input("ID do médico: "))

        for medico in medicos:
            if medico["id"] == id_update:

                medico["especialidade"] = input("Nova especialidade: ")
                medico["telefone"] = input("Novo telefone: ")

                print("Médico atualizado!")
                break

    # DELETE MEDICO
    elif opcao == "8":

        id_delete = int(input("ID do médico: "))

        for medico in medicos:
            if medico["id"] == id_delete:

                medicos.remove(medico)
                print("Médico removido!")
                break

    # CREATE CONSULTA
    elif opcao == "9":

        print("\nPACIENTES")

        for paciente in pacientes:
            print(paciente["id"], "-", paciente["nome"])

        id_paciente = int(input("ID do paciente: "))

        print("\nMÉDICOS")

        for medico in medicos:
            print(medico["id"], "-", medico["nome"])

        id_medico = int(input("ID do médico: "))

        consulta = {
            "id": len(consultas) + 1,
            "data": input("Data: "),
            "hora": input("Hora: "),
            "observacao": input("Observação: "),
            "paciente_id": id_paciente,
            "medico_id": id_medico
        }

        consultas.append(consulta)

        print("Consulta cadastrada!")

    # READ CONSULTA
    elif opcao == "10":

        for consulta in consultas:

            nome_paciente = ""
            nome_medico = ""

            for paciente in pacientes:
                if paciente["id"] == consulta["paciente_id"]:
                    nome_paciente = paciente["nome"]

            for medico in medicos:
                if medico["id"] == consulta["medico_id"]:
                    nome_medico = medico["nome"]

            print("\nConsulta:", consulta["id"])
            print("Paciente:", nome_paciente)
            print("Médico:", nome_medico)
            print("Data:", consulta["data"])
            print("Hora:", consulta["hora"])
            print("Observação:", consulta["observacao"])

    # UPDATE CONSULTA
    elif opcao == "11":

        id_update = int(input("ID da consulta: "))

        for consulta in consultas:
            if consulta["id"] == id_update:

                consulta["data"] = input("Nova data: ")
                consulta["hora"] = input("Nova hora: ")
                consulta["observacao"] = input("Nova observação: ")

                print("Consulta atualizada!")
                break

    # DELETE CONSULTA
    elif opcao == "12":

        id_delete = int(input("ID da consulta: "))

        for consulta in consultas:
            if consulta["id"] == id_delete:

                consultas.remove(consulta)
                print("Consulta removida!")
                break

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
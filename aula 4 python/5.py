alunos = []
professores = []
disciplinas = []
matriculas = []



qtd_prof = int(input("Quantidade de professores: "))

for i in range(qtd_prof):

    professor = {
        "id": i + 1,
        "nome": input("Nome do professor: "),
        "email": input("Email: "),
        "telefone": input("Telefone: "),
        "formacao": input("Formação: ")
    }

    professores.append(professor)



qtd_disc = int(input("\nQuantidade de disciplinas: "))

for i in range(qtd_disc):

    print("\nProfessores disponíveis:")

    for professor in professores:
        print(professor["id"], "-", professor["nome"])

    id_professor = int(input("Escolha o ID do professor: "))

    disciplina = {
        "id": i + 1,
        "nome": input("Nome da disciplina: "),
        "descricao": input("Descrição: "),
        "professor_id": id_professor
    }

    disciplinas.append(disciplina)



qtd_alunos = int(input("\nQuantidade de alunos: "))

for i in range(qtd_alunos):

    aluno = {
        "id": i + 1,
        "nome": input("Nome do aluno: "),
        "matricula": input("Matrícula: "),
        "email": input("Email: "),
        "telefone": input("Telefone: ")
    }

    alunos.append(aluno)



qtd_matriculas = int(input("\nQuantidade de matrículas: "))

for i in range(qtd_matriculas):

    print("\nAlunos disponíveis:")

    for aluno in alunos:
        print(aluno["id"], "-", aluno["nome"])

    id_aluno = int(input("Escolha o ID do aluno: "))

    print("\nDisciplinas disponíveis:")

    for disciplina in disciplinas:
        print(disciplina["id"], "-", disciplina["nome"])

    id_disciplina = int(input("Escolha o ID da disciplina: "))

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    faltas = int(input("Quantidade de faltas: "))

    matricula = {
        "id": i + 1,
        "aluno_id": id_aluno,
        "disciplina_id": id_disciplina,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "faltas": faltas
    }

    matriculas.append(matricula)



print("\n===== RELATÓRIO =====")

for matricula in matriculas:

    nome_aluno = ""
    nome_disciplina = ""
    nome_professor = ""

    for aluno in alunos:
        if aluno["id"] == matricula["aluno_id"]:
            nome_aluno = aluno["nome"]

    for disciplina in disciplinas:
        if disciplina["id"] == matricula["disciplina_id"]:

            nome_disciplina = disciplina["nome"]
            id_professor = disciplina["professor_id"]

            for professor in professores:
                if professor["id"] == id_professor:
                    nome_professor = professor["nome"]

    print("\nAluno:", nome_aluno)
    print("Disciplina:", nome_disciplina)
    print("Professor:", nome_professor)
    print("Nota 1:", matricula["nota1"])
    print("Nota 2:", matricula["nota2"])
    print("Nota 3:", matricula["nota3"])
    print("Média:", matricula["media"])
    print("Faltas:", matricula["faltas"])



id_update = int(input("\nDigite o ID da matrícula para atualizar: "))

for matricula in matriculas:

    if matricula["id"] == id_update:

        print("\nNotas atuais:")
        print("Nota 1:", matricula["nota1"])
        print("Nota 2:", matricula["nota2"])
        print("Nota 3:", matricula["nota3"])

        matricula["nota1"] = float(input("Nova Nota 1: "))
        matricula["nota2"] = float(input("Nova Nota 2: "))
        matricula["nota3"] = float(input("Nova Nota 3: "))

        matricula["media"] = (
            matricula["nota1"] +
            matricula["nota2"] +
            matricula["nota3"]
        ) / 3

        print("Matrícula atualizada!")


id_delete = int(input("\nDigite o ID da matrícula para deletar: "))

encontrado = False

for matricula in matriculas:

    if matricula["id"] == id_delete:

        matriculas.remove(matricula)

        print("Matrícula removida!")
        encontrado = True
        break

if encontrado == False:
    print("Matrícula não encontrada!")
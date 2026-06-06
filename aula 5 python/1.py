import tkinter as tk
from tkinter import messagebox

def cadastrar():
    aluno = {
        "nome": entry_nome.get(),
        "matricula": entry_matricula.get(),
        "data_nascimento": entry_data.get(),
        "email": entry_email.get(),
        "telefone": entry_telefone.get()
    }

    messagebox.showinfo(
        "Cadastro",
        f"Aluno {aluno['nome']} cadastrado com sucesso!"
    )

janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("500x350")

tk.Label(janela, text="Cadastro de Alunos",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Matrícula").pack()
entry_matricula = tk.Entry(janela, width=40)
entry_matricula.pack()

tk.Label(janela, text="Data de Nascimento").pack()
entry_data = tk.Entry(janela, width=40)
entry_data.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela, width=40)
entry_email.pack()

tk.Label(janela, text="Telefone").pack()
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack()

tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
).pack(pady=15)

janela.mainloop()
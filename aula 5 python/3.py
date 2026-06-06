import tkinter as tk
from tkinter import messagebox

def cadastrar():
    disciplina = {
        "nome": entry_nome.get(),
        "descricao": entry_descricao.get(),
        "professor_id": entry_professor.get()
    }

    messagebox.showinfo(
        "Cadastro",
        f"Disciplina {disciplina['nome']} cadastrada!"
    )

janela = tk.Tk()
janela.title("Cadastro de Disciplinas")
janela.geometry("500x250")

tk.Label(janela, text="Cadastro de Disciplinas",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Descrição").pack()
entry_descricao = tk.Entry(janela, width=40)
entry_descricao.pack()

tk.Label(janela, text="Professor ID").pack()
entry_professor = tk.Entry(janela, width=40)
entry_professor.pack()

tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
).pack(pady=15)

janela.mainloop()
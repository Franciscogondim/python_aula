import tkinter as tk
from tkinter import messagebox

def cadastrar():
    professor = {
        "nome": entry_nome.get(),
        "email": entry_email.get(),
        "telefone": entry_telefone.get(),
        "formacao": entry_formacao.get()
    }

    messagebox.showinfo(
        "Cadastro",
        f"Professor {professor['nome']} cadastrado!"
    )

janela = tk.Tk()
janela.title("Cadastro de Professores")
janela.geometry("500x300")

tk.Label(janela, text="Cadastro de Professores",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Email").pack()
entry_email = tk.Entry(janela, width=40)
entry_email.pack()

tk.Label(janela, text="Telefone").pack()
entry_telefone = tk.Entry(janela, width=40)
entry_telefone.pack()

tk.Label(janela, text="Formação").pack()
entry_formacao = tk.Entry(janela, width=40)
entry_formacao.pack()

tk.Button(
    janela,
    text="Cadastrar",
    command=cadastrar
).pack(pady=15)

janela.mainloop()
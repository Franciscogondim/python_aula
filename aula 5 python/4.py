import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    nota3 = float(entry_nota3.get())

    media = (nota1 + nota2 + nota3) / 3

    messagebox.showinfo(
        "Matrícula",
        f"Média do aluno: {media:.2f}"
    )

janela = tk.Tk()
janela.title("Matrículas")
janela.geometry("500x450")

tk.Label(janela, text="Cadastro de Matrículas",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(janela, text="Aluno ID").pack()
entry_aluno = tk.Entry(janela, width=40)
entry_aluno.pack()

tk.Label(janela, text="Disciplina ID").pack()
entry_disciplina = tk.Entry(janela, width=40)
entry_disciplina.pack()

tk.Label(janela, text="Nota 1").pack()
entry_nota1 = tk.Entry(janela, width=40)
entry_nota1.pack()

tk.Label(janela, text="Nota 2").pack()
entry_nota2 = tk.Entry(janela, width=40)
entry_nota2.pack()

tk.Label(janela, text="Nota 3").pack()
entry_nota3 = tk.Entry(janela, width=40)
entry_nota3.pack()

tk.Label(janela, text="Faltas").pack()
entry_faltas = tk.Entry(janela, width=40)
entry_faltas.pack()

tk.Button(
    janela,
    text="Matricular",
    command=cadastrar
).pack(pady=15)

janela.mainloop()
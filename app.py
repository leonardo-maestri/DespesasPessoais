# app.py
import tkinter as tk
from tkinter import messagebox, ttk
from database import SessionLocal, init_db
from models import Receita, Despesa
from datetime import datetime
from sqlalchemy import func, text

# Inicializa o banco de dados
init_db()
db = SessionLocal()

# Função para adicionar receita
def adicionar_receita():
    descricao = entry_receita_descricao.get()
    valor = float(entry_receita_valor.get())
    categoria = entry_receita_categoria.get()
    data = datetime.now().date()

    nova_receita = Receita(descricao=descricao, valor=valor, categoria=categoria, data=data)
    db.add(nova_receita)
    db.commit()

    messagebox.showinfo("Sucesso", "Receita adicionada com sucesso!")
    limpar_campos_receita()

# Função para adicionar despesa
def adicionar_despesa():
    descricao = entry_despesa_descricao.get()
    valor = float(entry_despesa_valor.get())
    categoria = entry_despesa_categoria.get()
    data = datetime.now().date()

    nova_despesa = Despesa(descricao=descricao, valor=valor, categoria=categoria, data=data)
    db.add(nova_despesa)
    db.commit()

    messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
    limpar_campos_despesa()

# Função pra calcular saldo e gerar um relatório
import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy import text

import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy import text
# Função pra calcular o salário 

import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy import text

def calcular_saldo():
    # Criar uma nova janela para exibir o relatório
    relatorio_window = tk.Toplevel()
    relatorio_window.title("Relatório de Receitas e Despesas")

    # Configurar a Treeview para receitas
    tree_receitas = ttk.Treeview(relatorio_window, columns=("Descricao", "Valor"), show='headings')
    tree_receitas.heading("Descricao", text="Descrição")
    tree_receitas.heading("Valor", text="Valor (R$)")
    tree_receitas.column("Valor", anchor="center")

    # Adiciona as receitas
    receitas_resultado = db.execute(text("SELECT descricao, valor FROM receitas")).fetchall()
    for descricao, valor in receitas_resultado:
        tree_receitas.insert("", "end", values=(descricao, f"{valor:.2f}"))

    # Total de receitas
    total_receitas = db.execute(text("SELECT SUM(valor) FROM receitas")).scalar() or 0
    tree_receitas.insert("", "end", values=("Total Receitas", f"{total_receitas:.2f}"), tags=('total',))

    # Configurar a Treeview para despesas
    tree_despesas = ttk.Treeview(relatorio_window, columns=("Descricao", "Valor"), show='headings')
    tree_despesas.heading("Descricao", text="Descrição")
    tree_despesas.heading("Valor", text="Valor (R$)")
    tree_despesas.column("Valor", anchor="center")

    # Adiciona as despesas
    despesas_resultado = db.execute(text("SELECT descricao, valor FROM despesas")).fetchall()
    for descricao, valor in despesas_resultado:
        tree_despesas.insert("", "end", values=(descricao, f"{valor:.2f}"))

    # Total de despesas
    total_despesas = db.execute(text("SELECT SUM(valor) FROM despesas")).scalar() or 0
    tree_despesas.insert("", "end", values=("Total Despesas", f"{total_despesas:.2f}"), tags=('total',))

    # Labels para as Treeviews
    tree_receitas_label = tk.Label(relatorio_window, text="Receitas", font=("Arial", 14))
    tree_receitas_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 0))

    tree_despesas_label = tk.Label(relatorio_window, text="Despesas", font=("Arial", 14))
    tree_despesas_label.grid(row=0, column=1, padx=(5, 10), pady=(10, 0))

    # Adiciona as Treeviews à janela usando grid
    tree_receitas.grid(row=1, column=0, padx=(10, 5), pady=(0, 10), sticky='nsew')
    tree_despesas.grid(row=1, column=1, padx=(5, 10), pady=(0, 10), sticky='nsew')

    # Configurar o layout
    relatorio_window.grid_rowconfigure(1, weight=1)
    relatorio_window.grid_columnconfigure(0, weight=1)
    relatorio_window.grid_columnconfigure(1, weight=1)

    # Cálculo do saldo
    saldo = total_receitas - total_despesas

    # Exibir o saldo abaixo das tabelas
    saldo_label = tk.Label(relatorio_window, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 14))
    saldo_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

    # Adiciona um botão para fechar a janela
    fechar_button = tk.Button(relatorio_window, text="Fechar", command=relatorio_window.destroy)
    fechar_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Estilo para destacar as linhas de total
    tree_receitas.tag_configure('total', background="#d3d3d3", font=("Arial", 10, "bold"))
    tree_despesas.tag_configure('total', background="#d3d3d3", font=("Arial", 10, "bold"))



# Função para limpar campos de receita
def limpar_campos_receita():
    entry_receita_descricao.delete(0, tk.END)
    entry_receita_valor.delete(0, tk.END)
    entry_receita_categoria.delete(0, tk.END)

# Função para limpar campos de despesa
def limpar_campos_despesa():
    entry_despesa_descricao.delete(0, tk.END)
    entry_despesa_valor.delete(0, tk.END)
    entry_despesa_categoria.delete(0, tk.END)

# Interface do Tkinter
window = tk.Tk()
window.title("Controle Financeiro Pessoal")

# Campos para adicionar receita
tk.Label(window, text="Adicionar Receita").grid(row=0, column=0)
tk.Label(window, text="Descrição:").grid(row=1, column=0)
entry_receita_descricao = tk.Entry(window)
entry_receita_descricao.grid(row=1, column=1)

tk.Label(window, text="Valor:").grid(row=2, column=0)
entry_receita_valor = tk.Entry(window)
entry_receita_valor.grid(row=2, column=1)

tk.Label(window, text="Categoria:").grid(row=3, column=0)
entry_receita_categoria = tk.Entry(window)
entry_receita_categoria.grid(row=3, column=1)

tk.Button(window, text="Adicionar Receita", command=adicionar_receita).grid(row=4, column=0, columnspan=2, pady=10)

# Campos para adicionar despesa
tk.Label(window, text="Adicionar Despesa").grid(row=5, column=0)
tk.Label(window, text="Descrição:").grid(row=6, column=0)
entry_despesa_descricao = tk.Entry(window)
entry_despesa_descricao.grid(row=6, column=1)

tk.Label(window, text="Valor:").grid(row=7, column=0)
entry_despesa_valor = tk.Entry(window)
entry_despesa_valor.grid(row=7, column=1)

tk.Label(window, text="Categoria:").grid(row=8, column=0)
entry_despesa_categoria = tk.Entry(window)
entry_despesa_categoria.grid(row=8, column=1)

tk.Button(window, text="Adicionar Despesa", command=adicionar_despesa).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(window, text="Calcular Saldo", command=calcular_saldo).grid(row=10, column=0, columnspan=2, pady=10)


window.mainloop()

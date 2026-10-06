import tkinter as tk
from tkinter import messagebox


def criar_janela(pai, titulo, bg, dimensao):
    janela = tk.Toplevel(pai)
    janela.title(titulo)
    janela.config(bg=bg)
    janela.geometry(dimensao)
    return janela


def cadastrar_item():
    janela_cadastro_item = criar_janela(janela_principal, "Cadastro de prato", "darkblue", "600x450")
    janela_cadastro_item.resizable(False, False)
    
    quadrado_central = tk.Frame(janela_cadastro_item, background="white", width=550, height=400)
    quadrado_central.pack(anchor='center', padx=15, pady=15)
    
    texto1 = tk.Label(janela_cadastro_item, text="JANELA DE CADASTRO DE PRATOS")
    texto1.config(border=5, borderwidth=5)
    texto1.place(x=200, y=10)
    
    
    tk.Label(janela_cadastro_item, text="ID do prato: ").place(x=30, y=70)
    entrada_id = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
    entrada_id.place(x=30, y=105)
    
    
    tk.Label(janela_cadastro_item, text="Nome do prato: ").place(x=30, y=170)
    entrada_nome = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
    entrada_nome.place(x=30, y=200)
    
    
    tk.Label(janela_cadastro_item, text="Preço do prato: ").place(x=30, y=270)
    entrada_preco = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
    entrada_preco.place(x=30, y=300)
    
    
    def salvar():
        id_item = entrada_id.get().strip()
        nome = entrada_nome.get().strip()
        preco_texto = entrada_preco.get().strip().replace(",", ".")
 
        if not (id_item and nome and preco_texto):
            messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela_cadastro_item)
            return
        try:
            preco = float(preco_texto)
        except ValueError:
            messagebox.showwarning("Atenção", "Preço inválido.", parent=janela_cadastro_item)
            return
 
        adicionar_ao_cardapio(id_item, nome, preco)
        janela_cadastro_item.destroy()
 
    botao_salvar = tk.Button(janela_cadastro_item, text="SALVAR PRATO", width=40, height=2, bg="lightgrey", command=salvar, background="grey80")
    botao_salvar.place(x=150, y=370)
    
    botao_sair = tk.Button(janela_cadastro_item, text="SAIR", width=10, height=5, bg="lightgrey", command=janela_cadastro_item.destroy, background="firebrick1")
    botao_sair.place(x=480, y=30)
 
    return janela_cadastro_item


def adicionar_ao_cardapio(id_item, nome, preco):
    listBox_cardapio.insert(tk.END, f"{id_item}          |          {nome}          |          R$ {preco:.2f}")
    
def excluir_item():
    selecao = listBox_cardapio.curselection()
    if not selecao:
        messagebox.showinfo("Excluir item", "Selecione um item na lista primeiro.")
        return
    listBox_cardapio.delete(selecao[0])


janela_principal = tk.Tk()
janela_principal.title("Cardápio")
janela_principal.config(bg="darkblue")
janela_principal.geometry("800x780")
janela_principal.minsize(800, 500)


quadrado_central = tk.Frame(janela_principal, background="white", width=900, height=650)
quadrado_central.pack(side='bottom', anchor='sw', padx=15, pady=15)

texto_cardapio = tk.Label(janela_principal, text="Cardápio", font=("Arial", 20))
texto_cardapio.config(bg="lightgrey")
texto_cardapio.pack(side='top', anchor='nw', padx=30, pady=60)

listBox_cardapio = tk.Listbox(quadrado_central, selectmode="single", font=("Arial", 14), width=70, height=25)
listBox_cardapio.config(border=5, borderwidth=5)
listBox_cardapio.pack(anchor='center')

botao_cadastro_item = tk.Button(janela_principal, text="Adicionar item", width=35, height=3, bg="green3", command=cadastrar_item, activebackground="grey", activeforeground="black", border=3)
botao_cadastro_item.place(x=205, y=60)

botao_exclusao_item = tk.Button(janela_principal, text="Excluir item", width=35, height=3, bg="red2", command=excluir_item, activebackground="grey", activeforeground="black", border=3)
botao_exclusao_item.place(x=505, y=60)


janela_principal.mainloop()

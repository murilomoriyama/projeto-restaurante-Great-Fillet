import tkinter as tk
from tkinter import messagebox
import pyautogui

lista_itens_cardapio = []


def fixar_centro(janela_principal, largura_janela, altura_janela):
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()
    posicao_x = int(largura_tela / 2 - largura_janela / 2)
    posicao_y = int(altura_tela / 2 - altura_janela / 2)
    janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    janela_principal.resizable(False, False)


def criar_janela(pai, titulo, bg, dimensao):
    janela = tk.Toplevel(pai)
    janela.title(titulo)
    janela.config(bg=bg)
    janela.geometry(dimensao)
    return janela


def funcoes_cardapio():    
    def cadastrar_item():
        janela_cadastro_item = criar_janela(janela_principal, "Cadastro de prato", "darkblue", "600x450")
        fixar_centro(janela_cadastro_item, 600, 450)
        
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

            lista_itens_cardapio.append({'ID': id_item,
                                         'NOME': nome,
                                         'PRECO': preco})
            print(lista_itens_cardapio)
            
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
        index = lista_itens_cardapio[selecao[0]]
        
        if not selecao:
            messagebox.showinfo("Excluir item", "Selecione um item na lista primeiro.")
            return
        
        listBox_cardapio.delete(selecao[0])
        lista_itens_cardapio.remove(index)
    
    janela_principal = tk.Tk()
    janela_principal.title("Cardápio")
    janela_principal.config(bg="darkblue")
    fixar_centro(janela_principal, 800, 780)
    
    
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
    
    
def funcoes_pedidos():
    janela_pedidos = tk.Tk()
    janela_pedidos.title("Pedidos")
    janela_pedidos.config(bg="darkblue")
    fixar_centro(janela_pedidos, 800, 780)
    

    borda = tk.Frame(janela_pedidos, bg="#7A0707", relief="ridge", bd=10)
    borda.pack(side="top", padx=20, pady=40)
    
    tk.Label(borda, text='MENU DE PEDIDOS', font=("arial", 25), bg='grey').pack()
    tk.Label(janela_pedidos, text='Lista de pedidos', font=("arial", 20), background='lightgrey').pack(side='top', anchor='nw', padx=20)
    

    lancar_pedido = tk.Button(janela_pedidos, text="Lançar pedido", font=20, width=12, height=10, command=..., background="grey80")
    lancar_pedido.place(x=625, y=150)
    
    atender_pedido = tk.Button(janela_pedidos, text="Atender pedido", font=20, width=12, height=10, command=..., background="grey80")
    atender_pedido.place(x=625, y=450)
    
    
    quadrado_central = tk.Frame(janela_pedidos, background="white", width=600, height=650)
    quadrado_central.pack(side='left', anchor='center', padx=15, pady=15)
    
    listBox_pedidos = tk.Listbox(quadrado_central, selectmode="single", font=("Arial", 14), width=50, height=25)
    listBox_pedidos.config(border=5, borderwidth=5)
    listBox_pedidos.pack(anchor='w')

    for item in cardapio:
        listBox_cardapio.insert(tk.END,
        f"{item['id']}          |          {item['nome']}          |          R$ {item['preco']:.2f}")
    
    janela_pedidos.mainloop()


def funcoes_historico():
    janela_principal = tk.Tk()
    janela_principal.title("JANELA DE HISTÓRICO")
    janela_principal.config(bg='darkblue')
    fixar_centro(janela_principal, 800, 780)
    
    
    tk.Label(janela_principal, text='Histórico de ações', background='lightgrey', font=("arial", 20)).pack(side='top', anchor='nw', padx=20, pady=40)
    
    
    listBox_historico = tk.Listbox(janela_principal, width=130, height=40)
    listBox_historico.pack(side='bottom', anchor='center', padx=20, pady=5)
    

janela = tk.Tk()
janela.config(bg='darkblue')
fixar_centro(janela, 1125, 500)


tk.Label(janela, text='MENU DO SISTEMA', font=("arial", 25), bg='grey', relief='ridge', bd=5).pack(side='top', anchor='center', pady=15)


botao_cardapio = tk.Button(janela, text="Abrir cardápio", width=30, height=30, command=funcoes_cardapio, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_cardapio.pack(side='left', padx=15, pady=80)

botao_pedido = tk.Button(janela, text="Abrir pedidos", width=30, height=30, command=funcoes_pedidos, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_pedido.pack(side='left', anchor='center', padx=15, pady=80)

botao_historico = tk.Button(janela, text="Visualizar histórico", width=30, height=30, command=funcoes_historico, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_historico.pack(side='right', padx=15, pady=80)


janela.mainloop()

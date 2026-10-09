import tkinter as tk
from tkinter import messagebox
from Pilha import Pilha
from fila import Fila


lista_itens_cardapio = []
fila_cozinha = Fila()
pilha_historico = Pilha()

def caixa_vazia(pai, texto, texto_tamanho, posx, posy):
    caixa = tk.Label(pai, text=texto, font=("arial", texto_tamanho), bg="white")
    caixa.place(x=posx, y=posy)
    return caixa

def fixar_centro(pai, largura_janela, altura_janela):
    largura_tela = pai.winfo_screenwidth()
    altura_tela = pai.winfo_screenheight()
    posicao_x = int(largura_tela / 2 - largura_janela / 2)
    posicao_y = int(altura_tela / 2 - altura_janela / 2)
    pai.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    pai.resizable(False, False)


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

            if preco <= 0:
                messagebox.showwarning("Atenção", "Preço inválido.", parent=janela_cadastro_item)
                return

            for item in lista_itens_cardapio:
                if item["id"] == id_item:
                    messagebox.showwarning("Atenção", "Já existe um prato com esse ID.", parent=janela_cadastro_item)
                    return
                  
            adicionar_ao_cardapio(id_item, nome, preco)
            janela_cadastro_item.destroy()
     

        botao_salvar = tk.Button(janela_cadastro_item, text="SALVAR PRATO", width=40, height=2, bg="lightgrey", command=salvar, background="grey80")
        botao_salvar.place(x=150, y=370)
        
        botao_sair = tk.Button(janela_cadastro_item, text="SAIR", width=10, height=5, bg="lightgrey", command=janela_cadastro_item.destroy, background="firebrick1")
        botao_sair.place(x=480, y=30)
     
        return janela_cadastro_item
    
    
    def adicionar_ao_cardapio(id_item, nome, preco):
        item = {
            "id": id_item,
            "nome": nome,
            "preco": preco
        }
        lista_itens_cardapio.append(item)
        listBox_cardapio.insert(tk.END, f"{id_item}          |          {nome}          |          R$ {preco:.2f}")
        

    def excluir_item():
        selecao = listBox_cardapio.curselection()
        
        if len(lista_itens_cardapio) == 0:
                    messagebox.showwarning("Excluir item", "Nenhum item no cardápio.", parent=janela_principal)
                    return 

        if not selecao:
            messagebox.showwarning("Excluir item", "Selecione um item na lista primeiro.", parent=janela_principal)
            return
            
            
        indice = selecao[0]
        lista_itens_cardapio.pop(indice)
        listBox_cardapio.delete(indice)
    
    
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

    for item in lista_itens_cardapio:
        listBox_cardapio.insert(tk.END,
        f"{item['id']}          |          {item['nome']}          |          R$ {item['preco']:.2f}")
    
    botao_cadastro_item = tk.Button(janela_principal, text="Adicionar item", width=35, height=3, bg="green3", command=cadastrar_item, activebackground="grey", activeforeground="black", border=3)
    botao_cadastro_item.place(x=205, y=60)
    
    botao_exclusao_item = tk.Button(janela_principal, text="Excluir item", width=35, height=3, bg="red2", command=excluir_item, activebackground="grey", activeforeground="black", border=3)
    botao_exclusao_item.place(x=505, y=60)
    
    janela_principal.mainloop()
    
    
def funcoes_pedidos():
    def lancar_pedido():
        def add_id_prato():
            id_prato = tk.Entry(janela_lancar_pedidos, width=50, border=3, bd=5)
            id_prato.pack(side="top", anchor="w", padx=150)
            pratos_pedido.append(id_prato)


        def adicionar_fila_cozinha():
            pedido_completo = []
            for id_prato in pratos_pedido:
                for dic in lista_itens_cardapio:
                    if id_prato.get() not in dic["id"] or id_prato.get() == None:
                        messagebox.showwarning("Atenção", "ID do prato não encontrado: " + id_prato.get(), parent=janela_lancar_pedidos)
                        return
                pedido_completo.append(id_prato.get())
            fila_cozinha.entrar(f"{cliente_pedido.get()} | {", ".join(pedido_completo)}")
            listBox_pedidos.insert(tk.END, f"{cliente_pedido.get()} | {", ".join(pedido_completo)}")
            janela_lancar_pedidos.destroy()
            caixa.destroy()


        if len(lista_itens_cardapio) == 0:
            messagebox.showwarning("Atenção", "Cardápio vazio", parent=janela_pedidos)
            return            

        janela_lancar_pedidos = criar_janela(janela_pedidos, "Lançamento de pedidos", "darkblue", "600x450")
        fixar_centro(janela_lancar_pedidos, 600, 450)

        tk.Label(janela_lancar_pedidos, text="Dados do pedido ", font="30", bg="grey80", relief="ridge").pack(side="top", pady=30)
        
        pratos_pedido = []
        tk.Label(janela_lancar_pedidos, text="Nome do cliente:", font=("arial", 14), bg="grey80", relief="solid").pack(side="top", anchor="w", padx=150)
        cliente_pedido = tk.Entry(janela_lancar_pedidos, width=50, border=3, bd=5)
        cliente_pedido.pack(side="top", anchor="w", padx=150)

        tk.Label(janela_lancar_pedidos, text="Id do(s) prato(s):", font=("arial", 14), bg="grey80", relief="solid").pack(side="top", anchor="w", padx=150)
        add_id_prato()

        botao_mais = tk.Button(janela_lancar_pedidos, text="+", font=50, relief="ridge", command=add_id_prato)
        botao_mais.place(x=525, y=85)
        botao_salvar = tk.Button(janela_lancar_pedidos, text="SALVAR", font=("arial", 12), relief="ridge", command=adicionar_fila_cozinha)
        botao_salvar.place(x=490, y=360)


    def atender_pedido():
        fila_cozinha.chamar()
        listBox_pedidos.delete(0)


    janela_pedidos = tk.Tk()
    janela_pedidos.title("Pedidos")
    janela_pedidos.config(bg="darkblue")
    fixar_centro(janela_pedidos, 800, 780)

    borda = tk.Frame(janela_pedidos, bg="#7A0707", relief="ridge", bd=10)
    borda.pack(side="top", padx=20, pady=40)
    
    tk.Label(borda, text='MENU DE PEDIDOS', font=("arial", 25), bg='grey').pack()
    tk.Label(janela_pedidos, text='Lista de pedidos', font=("arial", 20), background='lightgrey').pack(side='top', anchor='nw', padx=20)
    

    botao_lancar_pedido = tk.Button(janela_pedidos, text="Lançar pedido", font=20, width=12, height=10, command=lancar_pedido, background="grey80")
    botao_lancar_pedido.place(x=625, y=150)
    
    botao_atender_pedido = tk.Button(janela_pedidos, text="Atender pedido", font=20, width=12, height=10, command=atender_pedido, background="grey80")
    botao_atender_pedido.place(x=625, y=450)
    
    
    quadrado_central = tk.Frame(janela_pedidos, background="white", width=600, height=650)
    quadrado_central.pack(side='left', anchor='center', padx=15, pady=15)
    
    listBox_pedidos = tk.Listbox(quadrado_central, selectmode="single", font=("Arial", 14), width=50, height=25)
    listBox_pedidos.config(border=5, borderwidth=5)
    listBox_pedidos.pack(anchor='w')

    caixa = None
    if listBox_pedidos.size() == 0:
        caixa = caixa_vazia(quadrado_central, "FILA DA COZINHA VAZIA", 16, 40, 40)


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

botao_historico = tk.Button(janela, text="Abrir histórico", width=30, height=30, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_historico.pack(side='right', padx=15, pady=80)


janela.mainloop()

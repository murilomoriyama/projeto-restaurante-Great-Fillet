import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Pilha import Pilha
from fila import Fila


lista_itens_cardapio = []
fila_cozinha = Fila()
pilha_historico = Pilha()


ACAO_LANCAR = "LANCAR_PEDIDO"
ACAO_ATENDER = "ATENDER_PEDIDO"
ROTULOS_ACAO = {ACAO_LANCAR: "Lançar pedido", ACAO_ATENDER: "Atender pedido"}


telas_abertas = {}

def esvaziar_fila():
    itens = []
    while not fila_cozinha.isEmpty():
        itens.append(fila_cozinha.chamar())
    return itens


def obter_pedidos_fila():
    itens = esvaziar_fila()
    for item in itens:
        fila_cozinha.entrar(item)
    return itens


def remover_pedido_da_fila(pedido):
    itens = esvaziar_fila()
    removido = False
    for i in range(len(itens) - 1, -1, -1):
        if itens[i] == pedido:
            itens.pop(i)
            removido = True
            break
    for item in itens:
        fila_cozinha.entrar(item)
    return removido


def devolver_pedido_ao_inicio_da_fila(pedido):
    itens = esvaziar_fila()
    fila_cozinha.entrar(pedido)
    for item in itens:
        fila_cozinha.entrar(item)


def obter_historico():
    temporario = []
    while not pilha_historico.isEmpty():
        temporario.append(pilha_historico.pop())
    for registro in reversed(temporario):
        pilha_historico.push(registro)
    return temporario


def atualizar_tela_aberta(nome):
    atualizar = telas_abertas.get(nome)
    if atualizar is None:
        return
    try:
        atualizar()
    except tk.TclError:
        telas_abertas.pop(nome, None)


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
        
        
        quadrado_central = tk.Frame(janela_cadastro_item, background="lightgrey", width=550, height=400)
        quadrado_central.pack(anchor='center', padx=15, pady=15)
        
        texto1 = tk.Label(janela_cadastro_item, text="JANELA DE CADASTRO DE PRATOS", font=("Consolas", 9, "bold"), bg="gray77")
        texto1.config(relief='ridge', bd=5)
        texto1.place(x=200, y=10)
        
        
        tk.Label(janela_cadastro_item, text="ID do prato: ", font=("Consolas", 9, "bold"), relief='groove', bd=2).place(x=30, y=85)
        entrada_id = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
        entrada_id.place(x=30, y=105)
        
        
        tk.Label(janela_cadastro_item, text="Nome do prato: ", font=("Consolas", 9, "bold"), relief='groove', bd=2).place(x=30, y=180)
        entrada_nome = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
        entrada_nome.place(x=30, y=200)
        
        
        tk.Label(janela_cadastro_item, text="Preço do prato: ", font=("Consolas", 9, "bold"), relief='groove', bd=2).place(x=30, y=280)
        entrada_preco = tk.Entry(janela_cadastro_item, width=50, border=3, bd=5)
        entrada_preco.place(x=30, y=300)

        
        def salvar():
            id_item = entrada_id.get().strip()
            nome = entrada_nome.get().strip()
            preco_texto = entrada_preco.get().strip().replace(",", ".")
    
    
            for i in nome:
                if not i.isalpha():
                    messagebox.showwarning("Atenção", "Nome inválido.", parent=janela_cadastro_item)
                    return

            for i in id_item:
                if not i.isnumeric():
                    messagebox.showwarning("Atenção", "ID inválido.", parent=janela_cadastro_item)
                    return
            
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
    

        botao_salvar = tk.Button(janela_cadastro_item, text="SALVAR PRATO", font=("Consolas", 9, "bold"), width=40, height=3, bg="green2", activebackground="green4", command=salvar)
        botao_salvar.config(relief="raised", bd=3)
        botao_salvar.place(x=150, y=350)
        
        botao_sair = tk.Button(janela_cadastro_item, text="SAIR", font=("Consolas", 9, "bold"), width=10, height=5, bg="firebrick1", foreground="white", activebackground="red4", command=janela_cadastro_item.destroy)
        botao_sair.config(relief="raised", bd=3)
        botao_sair.place(x=480, y=30)
    
        return janela_cadastro_item
    
    
    def adicionar_ao_cardapio(id_item, nome, preco):
        item = {
            "id": id_item,
            "nome": nome,
            "preco": preco
        }
        lista_itens_cardapio.append(item)
        
        id_formatado = f"{item['id']:<5}"
        nome_formatado = f"{item['nome']:<30}"
        preco_formatado = f"R$ {item['preco']:<7.2f}"
        
        listBox_cardapio.insert(tk.END, f"{id_formatado} | {nome_formatado} | {preco_formatado}")
        

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
    
    texto_cardapio = tk.Label(janela_principal, text="Cardápio", font=("Consolas", 20))
    texto_cardapio.config(bg="lightgrey", relief='ridge', bd=5)
    texto_cardapio.pack(side='top', anchor='nw', padx=30, pady=60)
    
    listBox_cardapio = tk.Listbox(quadrado_central, selectmode="single", font=("Consolas", 14), width=70, height=25)
    listBox_cardapio.config(border=5, borderwidth=5)
    listBox_cardapio.pack(anchor='center', fill=tk.BOTH, expand=True)

    for item in lista_itens_cardapio:
        id_formatado = f"{item['id']:<5}"
        nome_formatado = f"{item['nome']:<30}"
        preco_formatado = f"R$ {item['preco']:<7.2f}"
    
    
        linha = f"{id_formatado} | {nome_formatado} | {preco_formatado}"
    
        listBox_cardapio.insert(tk.END, linha)
    
    botao_cadastro_item = tk.Button(janela_principal, text="ADICIONAR ITEM", font=("Consolas", 9, "bold"), width=35, height=3, bg="green2", foreground="black", command=cadastrar_item, activebackground="green4", activeforeground="black", border=3)
    botao_cadastro_item.config(relief='raised', bd=5)
    botao_cadastro_item.place(x=205, y=58)
    
    botao_exclusao_item = tk.Button(janela_principal, text="EXCLUIR ITEM", font=("Consolas", 9, "bold"), width=35, height=3, bg="red2", foreground="white", command=excluir_item, activebackground="red4", activeforeground="black", border=3)
    botao_exclusao_item.config(relief='raised', bd=5)
    botao_exclusao_item.place(x=505, y=58)
    
    janela_principal.mainloop()
    
    
def funcoes_pedidos():
    def lancar_pedido():
        def add_prato_pedido():
            opcoes = []
            for dic in lista_itens_cardapio:
                opcoes.append(f"{dic["id"]} - {dic["nome"]}")
            prato = ttk.Combobox(janela_lancar_pedidos, values=opcoes, font=("Consolas", 14), state="readonly")
            prato.pack(side="top", anchor="w", padx=150)
            pratos_pedido.append(prato)
    
    
        def remove_prato_pedido():
            if len(pratos_pedido) > 1:
                prato = pratos_pedido.pop()
                prato.destroy()
            else:
                messagebox.showwarning("Atenção", "Informe ao menos um prato.", parent=janela_lancar_pedidos)


        def adicionar_fila_cozinha():
            nome_cliente = cliente_pedido.get()
            for i in nome_cliente:
                if not i.isalpha():
                    messagebox.showwarning("Atenção", "Nome inválido.", parent=janela_lancar_pedidos)
                    return
                
            if len(nome_cliente) == 0:
                messagebox.showwarning("Atenção", "Informe o nome do cliente.", parent=janela_lancar_pedidos)
                return
            
            pedido_completo = []
            for prato in pratos_pedido:
                prato_escolhido = prato.get()
                if prato_escolhido == "":
                    messagebox.showwarning("Atenção", "Prato vazio.", parent=janela_lancar_pedidos)
                    return
                pedido_completo.append(prato_escolhido)
            
            
            pedido = ", ".join(pedido_completo)
            nome_formatado = f"{nome_cliente:<15}"
            pedido_formatado = f"{pedido:<15}"
            
            pedido = f"{nome_formatado} | {pedido_formatado}"
            fila_cozinha.entrar(pedido)
            pilha_historico.push({"acao": ACAO_LANCAR, "pedido": pedido})
            janela_lancar_pedidos.destroy()
            atualizar_lista_pedidos()
            atualizar_tela_aberta("historico")


        if len(lista_itens_cardapio) == 0:
            messagebox.showwarning("Atenção", "Cardápio vazio", parent=janela_pedidos)
            return


        janela_lancar_pedidos = criar_janela(janela_pedidos, "Lançamento de pedidos", "darkblue", "600x450")
        fixar_centro(janela_lancar_pedidos, 600, 550)

        tk.Label(janela_lancar_pedidos, text="DADOS DO PEDIDO", font=("Consolas", 25, "bold"), bg="grey80", relief="ridge", bd=5).pack(side="top", pady=30)
        
        pratos_pedido = []
        tk.Label(janela_lancar_pedidos, text="Nome do cliente:", font=("Consolas", 14), bg="grey80", relief="solid").pack(side="top", anchor="w", padx=150)
        cliente_pedido = tk.Entry(janela_lancar_pedidos, width=50, border=3, bd=5)
        cliente_pedido.pack(side="top", anchor="w", padx=150)

        tk.Label(janela_lancar_pedidos, text="Prato(s) do pedido:", font=("Consolas", 14), bg="grey80", relief="solid").pack(side="top", anchor="w", padx=150)
        add_prato_pedido()

        botao_mais = tk.Button(janela_lancar_pedidos, text="+", font=50, relief="ridge", command=add_prato_pedido)
        botao_mais.place(x=465, y=180)
        botao_menos = tk.Button(janela_lancar_pedidos, text="-", font=50, relief="ridge", command=remove_prato_pedido)
        botao_menos.place(x=515, y=180)
        botao_salvar = tk.Button(janela_lancar_pedidos, text="SALVAR", font=("Consolas", 12), relief="ridge", command=adicionar_fila_cozinha)
        botao_salvar.place(x=490, y=360)


    def atender_pedido():
        if fila_cozinha.isEmpty():
            messagebox.showwarning("Atenção", "Fila da cozinha vazia.", parent=janela_pedidos)
            return

        pedido = fila_cozinha.chamar()
        pilha_historico.push({"acao": ACAO_ATENDER, "pedido": pedido})
        atualizar_lista_pedidos()
        atualizar_tela_aberta("historico")
        messagebox.showinfo("Pedido atendido", "Pedido finalizado:\n" + pedido, parent=janela_pedidos)


    def atualizar_lista_pedidos():
        nonlocal caixa
        pedidos = obter_pedidos_fila()
        listBox_pedidos.delete(0, tk.END)
        for pedido in pedidos:
            listBox_pedidos.insert(tk.END, pedido)


    janela_pedidos = tk.Tk()
    janela_pedidos.title("Pedidos")
    janela_pedidos.config(bg="darkblue")
    fixar_centro(janela_pedidos, 800, 780)

    borda = tk.Frame(janela_pedidos, bg="grey", relief="ridge", bd=5)
    borda.pack(side="top", padx=20, pady=35)
    
    tk.Label(borda, text='MENU DE PEDIDOS', font=("Consolas", 25, "bold"), bg='grey').pack()
    tk.Label(janela_pedidos, text='Lista de pedidos', font=("Consolas", 20), background='lightgrey', relief='ridge', bd=5).pack(side='top', anchor='nw', padx=20)
    

    botao_lancar_pedido = tk.Button(janela_pedidos, text="LANÇAR PEDIDO", font=("Consolas", 13, "bold"), width=14, height=10, command=lancar_pedido, background="LightBlue1")
    botao_lancar_pedido.config(relief='raised', bd=5)
    botao_lancar_pedido.place(x=625, y=205)
    
    botao_atender_pedido = tk.Button(janela_pedidos, text="ATENDER PEDIDO", font=("Consolas", 13, "bold"), width=14, height=10, command=atender_pedido, background="orange")
    botao_atender_pedido.config(relief='raised', bd=5)
    botao_atender_pedido.place(x=625, y=450)
    
    
    quadrado_central = tk.Frame(janela_pedidos, background="white", width=600, height=650)
    quadrado_central.pack(side='left', anchor='center', padx=15, pady=15)
    
    listBox_pedidos = tk.Listbox(quadrado_central, selectmode="single", font=("Consolas", 14), width=50, height=25)
    listBox_pedidos.config(border=5, borderwidth=5)
    listBox_pedidos.pack(anchor='w')

    caixa = None
    telas_abertas["pedidos"] = atualizar_lista_pedidos
    atualizar_lista_pedidos()


    janela_pedidos.mainloop()


def funcoes_historico():
    def atualizar_historico():
        registros = obter_historico()
        listBox_historico.delete(0, tk.END)
        for registro in registros:
            listBox_historico.insert(tk.END, f"{ROTULOS_ACAO[registro['acao']]} ➔ {registro['pedido']}")


    def desfazer_ultima_acao():
        if pilha_historico.isEmpty():
            messagebox.showwarning("Desfazer", "Não há ações para desfazer.", parent=janela_principal)
            return

        registro = pilha_historico.pop()
        pedido = registro["pedido"]

        if registro["acao"] == ACAO_LANCAR:
            remover_pedido_da_fila(pedido)
            mensagem = "Lançamento cancelado e removido da fila:\n" + pedido
        else:
            devolver_pedido_ao_inicio_da_fila(pedido)
            mensagem = "Atendimento desfeito, pedido devolvido ao início da fila:\n" + pedido

        atualizar_historico()
        atualizar_tela_aberta("pedidos")
        messagebox.showinfo("Desfazer", mensagem, parent=janela_principal)


    janela_principal = tk.Tk()
    janela_principal.title("JANELA DE HISTÓRICO")
    janela_principal.config(bg='darkblue')
    fixar_centro(janela_principal, 800, 780)
    
    tk.Label(janela_principal, text='Histórico de ações', relief='ridge', bd=5, background='lightgrey', font=("Consolas", 20)).pack(side='top', anchor='nw', padx=20, pady=40)
    
    listBox_historico = tk.Listbox(janela_principal, width=130, height=40, font=("Consolas", 14))
    listBox_historico.config(border=5, borderwidth=5)
    listBox_historico.pack(side='bottom', anchor='center', padx=20, pady=5)

    botao_desfazer = tk.Button(janela_principal, text="DESFAZER ÚLTIMA AÇÃO", font=("Consolas", 10, "bold"), foreground="white", width=35, height=3, bg="red2", command=desfazer_ultima_acao, border=3)
    botao_desfazer.config(relief='raised', bd=5)
    botao_desfazer.place(x=520, y=40)

    telas_abertas["historico"] = atualizar_historico
    atualizar_historico()

    janela_principal.mainloop()
    

janela = tk.Tk()
janela.config(bg='darkblue')
fixar_centro(janela, 1125, 500)


tk.Label(janela, text='MENU DO SISTEMA', font=("Consolas", 25), bg='grey', relief='ridge', bd=5).pack(side='top', anchor='center', pady=15)


botao_cardapio = tk.Button(janela, text="Abrir cardápio", width=30, height=30, command=funcoes_cardapio, background="grey80", relief='raised', bd=5, font=("Consolas", 15))
botao_cardapio.pack(side='left', padx=15, pady=80)

botao_pedido = tk.Button(janela, text="Abrir pedidos", width=30, height=30, command=funcoes_pedidos, background="grey80", relief='raised', bd=5, font=("Consolas", 15))
botao_pedido.pack(side='left', anchor='center', padx=15, pady=80)

botao_historico = tk.Button(janela, text="Abrir histórico", width=30, height=30, command=funcoes_historico, background="grey80", relief='raised', bd=5, font=("Consolas", 15))
botao_historico.pack(side='right', padx=15, pady=80)


janela.mainloop()

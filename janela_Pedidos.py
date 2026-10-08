def funcoes_pedidos():
    def lancar_pedido():
        def add_id_prato():
            prato_pedido = tk.Entry(janela_lancar_pedidos, width=50, border=3, bd=5)
            prato_pedido.pack(side="top", anchor="w", padx=150)
            pratos_pedido.append(prato_pedido)


        def adicionar_fila_cozinha():
            pedido_completo = []
            for id_prato in pratos_pedido:
                #if id_prato.get() not in dicionario_cardapio:
                    #messagebox.showwarning("Atenção", "ID de prato não encontrado: " + id_prato.get(), parent=janela_lancar_pedidos)
                    #return
                pedido_completo.append(id_prato.get())
            fila_cozinha.entrar(f"{cliente_pedido.get()} | {", ".join(pedido_completo)}")
            listBox_pedidos.insert(tk.END, f"{cliente_pedido.get()} | {", ".join(pedido_completo)}")
            janela_lancar_pedidos.destroy()


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
    
    atender_pedido = tk.Button(janela_pedidos, text="Atender pedido", font=20, width=12, height=10, command=atender_pedido, background="grey80")
    atender_pedido.place(x=625, y=450)
    
    
    quadrado_central = tk.Frame(janela_pedidos, background="white", width=600, height=650)
    quadrado_central.pack(side='left', anchor='center', padx=15, pady=15)
    
    listBox_pedidos = tk.Listbox(quadrado_central, selectmode="single", font=("Arial", 14), width=50, height=25)
    listBox_pedidos.config(border=5, borderwidth=5)
    listBox_pedidos.pack(anchor='w')
    
    if listBox_pedidos.size() == 0:
        caixa = caixa_vazia(quadrado_central, "FILA DA COZINHA VAZIA", 16, 40, 40)
    else:
        caixa.destroy()
    


    janela_pedidos.mainloop()

def funcoes_pedidos():
    janela_pedidos = tk.Tk()
    janela_pedidos.title("Pedidos")
    janela_pedidos.config(bg="darkblue")
    largura_janela = 800
    altura_janela = 780
    largura_tela = janela_pedidos.winfo_screenwidth()
    altura_tela = janela_pedidos.winfo_screenheight()
    posicao_x = int(largura_tela / 2 - largura_janela / 2)
    posicao_y = int(altura_tela / 2 - altura_janela / 2)
    janela_pedidos.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    janela_pedidos.resizable(False, False)
    

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
    
    
    janela_pedidos.mainloop()

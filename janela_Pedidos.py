def funcoes_pedidos():
    janela_pedidos = tk.Tk()
    janela_pedidos.title("Pedidos")
    janela_pedidos.config(bg="darkblue")
    largura_janela = 700
    altura_janela = 600
    largura_tela = janela_pedidos.winfo_screenwidth()
    altura_tela = janela_pedidos.winfo_screenheight()
    posicao_x = int(largura_tela / 2 - largura_janela / 2)
    posicao_y = int(altura_tela / 2 - altura_janela / 2)
    janela_pedidos.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    janela_pedidos.resizable(False, False)

    borda = tk.Frame(janela_pedidos, bg="#7A0707", relief="ridge", bd=10)
    borda.pack(side="top", padx=20, pady=40)
    tk.Label(borda, text='MENU DE PEDIDOS', font=("arial", 25), bg='grey').pack()

    lancar_pedido = tk.Button(janela_pedidos, text="Lançar pedido", font=20, width=20, height=10, command=..., background="grey80")
    lancar_pedido.pack(side="left", padx=20)
    atender_pedido = tk.Button(janela_pedidos, text="Atender pedido", font=20, width=20, height=10, command=..., background="grey80")
    atender_pedido.pack(side="right", padx=20)
    visualisar_fila = tk.Button(janela_pedidos, text="Visualisar fila", font=20, width=20, height=10, command=..., background="grey80")
    visualisar_fila.pack(side="bottom", anchor="n", pady=40)
    
    
    
    janela.mainloop()

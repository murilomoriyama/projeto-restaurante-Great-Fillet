janela = tk.Tk()
janela.config(bg='darkblue')
largura_janela = 1125
altura_janela = 500
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = int(largura_tela / 2 - largura_janela / 2)
posicao_y = int(altura_tela / 2 - altura_janela / 2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")


tk.Label(janela, text='MENU DO SISTEMA', font=("arial", 25), bg='grey', relief='ridge', bd=5).pack(side='top', anchor='center', pady=15)


botao_cardapio = tk.Button(janela, text="Abrir cardápio", width=30, height=30, command=funcoes_cardapio, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_cardapio.pack(side='left', padx=15, pady=80)

botao_pedido = tk.Button(janela, text="Abrir pedidos", width=30, height=30, command=funcoes_pedidos, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_pedido.pack(side='left', anchor='center', padx=15, pady=80)

botao_historico = tk.Button(janela, text="Abrir histórico", width=30, height=30, background="grey80", relief='raised', bd=5, font=("arial", 15))
botao_historico.pack(side='right', padx=15, pady=80)


janela.mainloop()

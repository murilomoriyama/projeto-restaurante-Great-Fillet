def funcoes_historico():
    janela_principal = tk.Tk()
    janela_principal.title("JANELA DE HISTÓRICO")
    janela_principal.config(bg='darkblue')
    largura_janela = 800
    altura_janela = 780
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()
    posicao_x = int(largura_tela / 2 - largura_janela / 2)
    posicao_y = int(altura_tela / 2 - altura_janela / 2)
    janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    
    
    tk.Label(janela_principal, text='Histórico de ações', background='lightgrey', font=("arial", 20)).pack(side='top', anchor='nw', padx=20, pady=40)
    
    
    listBox_historico = tk.Listbox(janela_principal, width=130, height=40)
    listBox_historico.pack(side='bottom', anchor='center', padx=20, pady=5)

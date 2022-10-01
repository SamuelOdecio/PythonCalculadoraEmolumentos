from  tkinter import *

janela = Tk()
janela.title("FUNDOS CARTORIO")
texto = Label(janela, text="Clique no botão para gerar os Fundos")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="GERAR FUNDOS")
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()


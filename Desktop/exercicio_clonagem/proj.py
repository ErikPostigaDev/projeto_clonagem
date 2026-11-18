import tkinter as tk

janela = tk.Tk()
etiqueta = tk.Label(janela, text="olá mundo") 
botao = tk.Button(janela, text="clique aqui")    

janela.title("uma janela")
janela.geometry("300x300")
janela.resizable(False, False)
janela.configure(background='#35ADCC')


janela.iconbitmap(r"C:\Users\ERIKSANCHESPOSTIGA\Desktop\aula4\brasil.ico")

etiqueta.configure(text='Uma etiqueta', background="#FF0000",foreground="#FFFFFF", font=("Verdana",10,'bold'), width=20, height=3, anchor='w')


etiqueta.pack(pady=20)
botao.pack(pady=10)

janela.mainloop()
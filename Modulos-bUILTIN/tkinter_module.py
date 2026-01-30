import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Minha primeira GUI")
janela.geometry("300x200")  # largura x altura

# Criar um rótulo (label)
label = tk.Label(janela, text="Olá, Tkinter!")
label.pack()  # adiciona na janela

# Criar um botão
def clicar():
    label.config(text="Você clicou no botão!")

botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack()

# Executar a janela
janela.mainloop()
import tkinter as tk
from tkinter import Menu
#from tkinter import ImageTk, Image

class MenuGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x500')
        self.root.title('Menu com Logo em Python')

        # Carregando a imagem do logo
       # self.logo = ImageTk.PhotoImage(Image.open("logo.png"))

        # Criando a barra de menu
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Criando os menus
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu = Menu(self.menu_bar, tearoff=0)

        # Adicionando os menus à barra de menu
        self.menu_bar.add_cascade(label='Arquivo', menu=self.file_menu)
        self.menu_bar.add_cascade(label='Ajuda', menu=self.help_menu)

        # Adicionando os itens ao menu Arquivo
        self.file_menu.add_command(label='Novo')
        self.file_menu.add_command(label='Abrir')
        self.file_menu.add_command(label='Salvar')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Sair', command=self.root.quit)

        # Adicionando os itens ao menu Ajuda
        self.help_menu.add_command(label='Sobre')

        # Adicionando o logo ao topo da janela
        #self.logo_label = tk.Label(self.root, image=self.logo)
        #self.logo_label.pack(side='top')

        # Iniciando o loop da GUI
        self.root.mainloop()

# Criando a GUI do menu com logo
MenuGUI()



git remote add origin https://github.com/luciomotta/Menu-Tkinter.git
 git branch -M main 
git push -u origin main
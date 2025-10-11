from tkinter import *


window = Tk()

class Aplication():
    def __init__(self):
        self.window = window 
        self.tela() 
        self.frames_tela()
        window.mainloop() # loop para deixar a tela rodar 
    
    def tela(self):
        self.window.title("Cadastro de Alunos")
        self.window.configure(background= 'black')
        self.window.geometry("700x500") # tamanho da tela 
        self.window.resizable(True , TRUE) # responsividade
        self.window.maxsize(width = 900 , height= 700) # tamanho maximo
        self.window.minsize(width = 400 , height = 300) # tamanho minimo
    
    def frames_tela(self):
        self.frames_1 = Frame(self.window)
        self.frames_1.place(relx= 0.02 , rely= 0.02 , relwidth= 0.9 , relheight= 0.5)


Aplication()

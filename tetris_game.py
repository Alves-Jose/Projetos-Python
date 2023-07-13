from tkinter import *

#dimensions
lado = 20
q_largura = 10
q_altura = 20
largura = lado*q_largura
altura = lado*q_altura

class  Peca:

    def __init__(self, x, y)
        self. x = X
        self, y = y
        #self.grade[self]
        #self.size
   
   
    def vira(self):
        break

    
    def desce(self):
        break

    def direita(self):
        break

    def esquerda(self):
        break

class Tela:
    def __init__(self):
        self.grade = [0]

class Game:
    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=largura, height=altura, bg='black')
        self.canvas.pack()


        #self.window.bind

    def run(self):
        while(True):

            self.canvas.after(50)
            self.window.update_iddletasks()
            self.window.update()

g = Game()
g.run()
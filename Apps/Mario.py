# CHANGE TO ENGLISH ALL WORDS. VERIFY IF IT'S POSSIBLE TO FIX THE MOVEMENT STOPPED IF THERE IS A FAST CHANGE WAY

from tkinter import *

class Mario_App(object):
    xy = '400x300'

    def __init__(self, root):
        self.root = root
        self.frame1 = Frame(self.root)
        self.frame1.pack()

        self.canvas1 = Canvas(self.frame1, height = 200, width = 300, bg = 'black')
        self.canvas1.pack()

        self.botao1 = Button(self.frame1, text = 'Iniciar', command = self.criaMario)
        self.botao1.pack()

    def criaMario(self):
        self.canvas1.focus_force()
        self.imagemMario = 1
        self.vMario = 0
        self.move = True
        self.posMarioX = 100
        self.spriteMarioD = [PhotoImage(file = 'Images/Mario/mario_%i.ppm'%x) for x in range(1,5)]
        self.spriteMarioE = [PhotoImage(file = 'Images/Mario/mario_l%i.ppm'%x) for x in range(1,5)]
        self.spriteMario = [self.spriteMarioD,self.spriteMarioE]
        self.canvas1.create_image(self.posMarioX, 144, image = self.spriteMario[0][self.imagemMario])
        
        self.canvas1.bind('<Right>', self.direita)
        self.canvas1.bind('<KeyRelease-Right>',self.solta)
        self.canvas1.bind('<Left>', self.esquerda)
        self.canvas1.bind('<KeyRelease-Left>', self.solta)

        self.root.after(70, self.animaMario)

    def direita(self, event):
        self.move = True
        self.vMario = 10

    def esquerda(self, event):
        self.move = False
        self.vMario = -10

    def solta(self, event):
        self.vMario = 0
        if self.imagemMario == 0:
            self.imagemMario = 1
        elif self.imagemMario == 2:
            self.imagemMario = 3

    def animaMario(self):
        self.posMarioX += self.vMario
        self.imagemMario += 1
        if self.imagemMario > 3:
            self.imagemMario = 0

        self.canvas1.focus_force()
        
        if self.move == True:
            self.canvas1.delete(ALL)
            self.canvas1.create_image(self.posMarioX, 144, image = self.spriteMario[0][self.imagemMario])
        else:
            self.canvas1.delete(ALL)
            self.canvas1.create_image(self.posMarioX, 144, image = self.spriteMario[1][self.imagemMario])
        
        self.root.after(70, self.animaMario)


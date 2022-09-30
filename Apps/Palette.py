# CHANGE TO ENGLISH ALL WORDS. VERIFY IF IT'S RIGHT THE COLORS SHOWED AFTER PRESS ANY CANVAS CIRCLE

from tkinter import *

class Palette_App(object):
    xy = '300x200'

    def __init__(self, root):
        master = root

        self.canvas = Canvas(master, width=300, height=200, bg='gray')
        self.canvas.pack()
        self.canvas.focus_force()

        self.green_color = "#%02x%02x%02x" % (0, 255, 0)
        self.red_color = "#%02x%02x%02x" % (0, 0, 255)
        self.blue_color = "#%02x%02x%02x" % (255, 0, 0)
        self.white_RGB = (255, 255, 255)
        self.corBranca = "#%02x%02x%02x" % self.white_RGB

        # CONTINUE FROM HERE
        #Centro do círculo central é 150 para x e 60 para y, sendo o raio igual a 50.
        self.circuloCentral = self.canvas.create_oval((100,10),(200,110), fill = self.corBranca, tag = 'bola1')

        #Centro do círculo vermelho é 90 para x e 150 para y, sendo o raio igual a 50.
        self.filtroVermelho = self.canvas.create_oval((65,125),(115,175), fill = self.red_color)
        
        #Centro do cículo verde é 150 para x e 150 para y, sendo o raio igual a 25
        self.filtroVerde = self.canvas.create_oval((125,125),(175,175), fill = self.green_color)
        
        #Centro do círculo azul é 210 para x e 150 para y, sendo o raio igual a 50.
        self.filtroAzul = self.canvas.create_oval((185,125),(235,175), fill = self.blue_color)

        self.canvas.bind(('<Motion>','<Button-1>'), func = self.acao)

    def acao(self, event):
        self.cor = ''

        self.y = event.y -150
        
        if event.x <= 115:
            self.x = event.x -90
            self.cor = 'red'

        elif event.x <= 175:
            self.x = event.x -150
            self.cor = 'green'

        elif event.x > 175:
            self.x = event.x -210
            self.cor = 'blue'

        if self.x <0:
            self.x *= -1
        elif self.y <0:
            self.y *= -1

        if (self.x**2 + self.y**2) < 25**2 and self.cor == 'red':
            self.white_RGB = (self.white_RGB[0]-10, self.white_RGB[1], self.white_RGB[2])
            if self.white_RGB[0] < 0:
                self.white_RGB = (0, self.white_RGB[1], self.white_RGB[2])
                
            self.corBranca = "#%02x%02x%02x"%self.white_RGB
            self.canvas.itemconfig(self.circuloCentral, fill = self.corBranca)

        elif (self.x**2 + self.y**2) < 25**2 and self.cor == 'green':
            self.white_RGB = (self.white_RGB[0], self.white_RGB[1]-10, self.white_RGB[2])
            if self.white_RGB[1] < 0:
                self.white_RGB = (self.white_RGB[0], 0, self.white_RGB[1])
                
            self.corBranca = "#%02x%02x%02x"%self.white_RGB
            self.canvas.itemconfig(self.circuloCentral, fill = self.corBranca)

        elif (self.x**2 + self.y**2) < 25**2 and self.cor == 'blue':
            self.white_RGB = (self.white_RGB[0], self.white_RGB[1], self.white_RGB[2]-10)
            if self.white_RGB[2] < 0:
                self.white_RGB = (self.white_RGB[0], self.white_RGB[1], 0)
                
            self.corBranca = "#%02x%02x%02x"%self.white_RGB
            self.canvas.itemconfig(self.circuloCentral, fill = self.corBranca)


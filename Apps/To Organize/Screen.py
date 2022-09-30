from tkinter import *

class root(object):
    def __init__(self, inst):
        inst.geometry('400x100')
        inst.minsize(width = 400, height = 100)
        inst.maxsize(width = 600, height = 400)
        inst.title('Teste Grid')
        self.corMestre = 'white'
        inst['bg'] = self.corMestre

        self.frameGeral = Frame(inst, bg = self.corMestre)
        self.frameGeral.pack(anchor = 'center')

        self.labelAltura = Label(self.frameGeral, text = 'Altura', bg = self.corMestre)
        self.labelAltura.grid(column = 1, row = 1)

        self.labelLargura = Label(self.frameGeral, text = 'Largura', bg = self.corMestre)
        self.labelLargura.grid(column = 1, row = 2)

        self.entradaAltura = Entry(self.frameGeral, bg = self.corMestre)
        self.entradaAltura.grid(column = 2, row = 1, padx = 10)

        self.entradaLargura = Entry(self.frameGeral, bg = self.corMestre)
        self.entradaLargura.grid(column = 2, row = 2, padx = 10)

        self.imagemUm = PhotoImage(file = 'img.ppm').subsample(1,1)
        self.zoom = 1
        self.imagemAuxiliar = self.imagemUm
        self.labelImagemUm = Label(self.frameGeral, image = self.imagemUm)
        self.labelImagemUm.grid(column = 3, row = 1, rowspan = 2, columnspan = 2)

        self.botaoPreservaAspec = Checkbutton(self.frameGeral, text = 'Preserva Aspecto', bg = self.corMestre)
        self.botaoPreservaAspec.grid(column = 1, row = 3, sticky = E+W, columnspan = 2)

        self.botaoZoomIn = Button(self.frameGeral, text = 'Zoom In', bg = self.corMestre, command = self.zoomIn)
        self.botaoZoomIn.grid(column = 3, row = 3, padx = 3, pady = 5)

        self.botaoZoomOut = Button(self.frameGeral, text = 'Zoom Out', bg = self.corMestre, command = self.zoomOut)
        self.botaoZoomOut.grid(column = 4, row = 3, padx = 2)

    def zoomIn(self):
        if self.zoom <8:
            self.zoom += 1
        self.imagemUm = self.imagemAuxiliar.zoom(self.zoom, self.zoom)
        self.labelImagemUm['image'] = self.imagemUm

    def zoomOut(self):
        if self.zoom > 1:
            self.zoom -= 1
        self.imagemUm = self.imagemAuxiliar.zoom(self.zoom, self.zoom)
        self.labelImagemUm['image'] = self.imagemUm

if __name__ == '__main__':
    inst = Tk()
    root(inst)
    inst.mainloop()
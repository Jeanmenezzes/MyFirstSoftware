from tkinter import *

class lousa(object):
    def __init__(self,construtor):
        master = construtor
        master.geometry('300x200')
        master.title('Desenhe Linhas')

        self.listaEventos = []
        self.canvas = Canvas(master, width = 300, height = 200, bg = 'white')
        self.canvas.pack()

        self.canvas.bind(('<Motion>','<Button-1>'), func = self.criaLinha)
        
    def criaLinha(self, event):
        x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
        y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

        self.listaEventos.append((x,y))
        
        if len(self.listaEventos) == 2:
            self.canvas.create_line(self.listaEventos[0], self.listaEventos[1], fill = 'black')
            self.listaEventos = []

if __name__ == '__main__':
    root = Tk()
    inst = lousa(root)
    root.mainloop()

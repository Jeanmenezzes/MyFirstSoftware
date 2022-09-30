from tkinter import *
import shelve, functools, random

class frontEnd(object):
    def __init__(self):
        self.master = Tk()
        self.master.geometry('800x600')
        self.master.title('Menu Entrar')
        
        #Cor do background geral
        self.db = shelve.open('Usuários.db')
        self.backG = 'gray'
        self.fonteG = ('Verdana','24','bold')
        self.master['bg'] = self.backG

        if  not 'remind' in self.db:
            self.boolCb1 = False
        else:
            self.boolCb1 = self.db['remind']
        

        #Carrega as imagens
        self.imagem1 = PhotoImage(file = 'Imagens/bg_python.gif')
        self.imagem2 = PhotoImage(file = 'Imagens/b_entrar.ppm')
        self.imagem3 = PhotoImage(file = 'Imagens/b_criar.ppm')
        self.imagem4 = PhotoImage(file = 'Imagens/b_novo.ppm')

        #Cria todas os frames da tela inicial
        self.frameGeral = Frame(self.master, bg = self.backG)
        self.frame1 = Frame(self.frameGeral, bg = self.backG)
        self.frame2 = Frame(self.frameGeral, bg = self.backG)

        #Cria os demais botões
        self.label1 = Label(self.frame1, bg = self.backG, text = 'Usuário', font = self.fonteG)
        self.entrada1 = Entry(self.frame1)
        self.label2 = Label(self.frame1, bg = self.backG, text = 'Senha', font = self.fonteG)
        self.entrada2 = Entry(self.frame1)
        self.cbotao1 = Checkbutton(self.frame1, text = 'Lembrar-me', font = self.fonteG, bg = self.backG, activebackground = self.backG, command = self.cbAtiva)
        self.botao1 = Button(self.frame2, image = self.imagem2, command = self.ativaEntrar)
        self.botao2 = Button(self.frame2, image = self.imagem4, command = self.ativaNovo)
        self.label7 = Label(self.frameGeral, bg = self.backG)

        try:
            if self.db['remind']:
                self.entrada1.insert(END, self.db['lastUser'][0])
                self.entrada2.insert(END, self.db['lastUser'][1])
                self.boolCb1 = False
        except KeyError:
            pass

        #Empacota todos os widgets
        self.frameGeral.pack()
        self.frame1.pack()
        self.label1.pack()
        self.entrada1.pack()
        self.label2.pack()
        self.entrada2.pack()
        self.cbotao1.pack()
        
        self.frame2.pack()
        self.botao1.pack(side = LEFT)
        self.botao2.pack()
        
        self.label7.pack()
        self.master.mainloop()

    def cbAtiva(self):
        self.boolCb1 = not self.boolCb1
        self.db['remind'] = self.boolCb1
        #l 40
        if self.boolCb1:
            self.db['lastUser'] = [self.entrada1.get(),self.entrada2.get()]

    def ativaNovo(self):
        #Esquece todos os widgets
        self.frame1.pack_forget()
        self.label1.pack_forget()
        self.entrada1.pack_forget()
        self.label2.pack_forget()
        self.entrada2.pack_forget()
        self.cbotao1.pack_forget()

        self.frame2.pack_forget()
        self.botao1.pack_forget()
        self.botao2.pack_forget()

        self.label7.pack_forget()
        self.label7['text'] = ''

        #Cria novos frames
        self.frame3 = Frame(self.frameGeral, bg = self.backG, bd = 20)
        self.frame4 = Frame(self.frameGeral, bg = self.backG)
        
        self.frame3.pack()
        self.frame4.pack()

        #Cria os novos widgets
        self.label3 = Label(self.frame3, text = 'Nome', font = self.fonteG, bg = self.backG)
        self.entrada3 = Entry(self.frame3)
        
        self.label4 = Label(self.frame3, text = 'Email', font = self.fonteG, bg = self.backG)
        self.entrada4 = Entry(self.frame3)
        
        self.label5 = Label(self.frame3, text = 'Usuário', font = self.fonteG, bg = self.backG)
        self.entrada5 = Entry(self.frame3)
        
        self.label6 = Label(self.frame3, text = 'Senha', font = self.fonteG, bg = self.backG,)
        self.entrada6 = Entry(self.frame3, show = '*')

        self.botao3 = Button(self.frame4, image = self.imagem3, command = self.ativaCriar)

        #Empacotamos todos os widgets da tela de criar usuários
        self.label3.pack()
        self.entrada3.pack()
        self.label4.pack()
        self.entrada4.pack()
        self.label5.pack()
        self.entrada5.pack()
        self.label6.pack()
        self.entrada6.pack()
        self.botao3.pack()
        self.label7.pack()

    def ativaCriar(self):
        if not self.entrada5.get() in self.db and self.entrada3.get() != '' and self.entrada4.get() != '' and self.entrada5.get() != '' and self.entrada6.get() != '':
            self.db[self.entrada5.get()] = [self.entrada4.get(),self.entrada3.get(),self.entrada6.get()]
                
            #Esquece todos os Widgets da tela de criar
            self.label3.destroy()
            self.entrada3.destroy()
            self.label4.destroy()
            self.entrada4.destroy()
            self.label5.destroy()
            self.entrada5.destroy()
            self.label6.destroy()
            self.entrada6.destroy()
            self.botao3.destroy()
            self.label7['text'] = ''
            self.label7.destroy()
            self.frame3.destroy()
            self.frame4.destroy()
                
            #Recria todos os widgets da tela inicial
            self.frame1.pack()
            self.label1.pack()
            self.entrada1.pack()
            self.label2.pack()
            self.entrada2.pack()
            self.cbotao1.pack()

            self.frame2.pack()
            self.botao1.pack(side = LEFT)
            self.botao2.pack()
            self.label7.pack()

        else:
            self.label7['text'] = 'Usuário Indisponível'

    def ativaEntrar(self):
        if self.entrada1.get() in self.db:
            if self.db[self.entrada1.get()][2] == self.entrada2.get():
                #Esquece todos os widgets
                self.frame1.destroy()
                self.label1.destroy()
                self.entrada1.destroy()
                self.label2.destroy()
                self.entrada2.destroy()
                self.cbotao1.destroy()

                self.frame2.destroy()
                self.botao1.destroy()
                self.botao2.destroy()

                self.label7.destroy()
                
                self.db.close()

                #Chama o método de construção da nova tela
                self.menu()
            else:
                self.label7['text'] = 'Senha Inválida'
        else:
            self.label7['text'] = 'Usuário Inválido'

    def menu(self):
        #cria os novos botões
        self.botao1 = Button(self.frameGeral, text = 'Desenho', command = self.desenho)
        self.botao2 = Button(self.frameGeral, text = 'SPFC', command = self.spfc)
        self.botao3 = Button(self.frameGeral, text = 'Gráfico', command = functools.partial(self.grafico,self.master))
        self.botao4 = Button(self.frameGeral, text = 'Descanço de Tela', command = self.animacao)
        self.botao5 = Button(self.frameGeral, text = 'Carinha 2', command = self.animacao2)

        #Empacota todos os novos botões
        self.botao1.pack()
        self.botao2.pack()
        self.botao3.pack()
        self.botao4.pack()
        self.botao5.pack()

    def animacao2(self):
        #Exclui todos os botões para criar a animação
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.botao4.destroy()
        self.botao5.destroy()

        #Criado o objeto canvas
        self.LARGURA = 400
        self.ALTURA = 300
        self.canvas1 = Canvas(self.frameGeral, width = self.LARGURA, height = self.ALTURA, bg = 'black')
        self.canvas1.pack()

        #Cria o desenho da carinha que será movimentada
        self.raio = 25
        self.carinha2 = self.canvas1.create_oval((self.LARGURA/2-self.raio, self.ALTURA/2-self.raio),(self.LARGURA/2+self.raio,self.ALTURA/2+self.raio),
        tag = 'carinha', fill = 'yellow')
        self.canvas1.create_oval((self.LARGURA/2-(self.raio/4)*3,self.ALTURA/2-self.raio/2),(self.LARGURA/2-self.raio/4,self.ALTURA/2),tag = 'carinha',
        fill = 'black')
        self.canvas1.create_oval((self.LARGURA/2+(self.raio/4)*3,self.ALTURA/2-self.raio/2),(self.LARGURA/2+self.raio/4,self.ALTURA/2),tag = 'carinha',
        fill = 'black')
        self.canvas1.create_arc((self.LARGURA/2-(self.raio/3)*2,self.ALTURA/2),(self.LARGURA/2+(self.raio/3)*2,self.ALTURA/2+(self.raio/3)*2),
        tag = 'carinha', style = ARC, start = 180, extent = 180)

        #Cria as velocidades e a posição do desenho
        self.posx, self.posy = 200 - self.raio, 150 - self.raio
        self.vx, self.vy = 10, 10
        self.bbcarinha = self.canvas1.bbox('carinha')

        #Inicia o processo de binding dos direcionais com o desenho da carinha
        self.canvas1.focus_force()
        self.canvas1.bind('<Motion>', self.anima2)
    def anima2(self, event):
        self.vx = event.x - self.posx
        self.vy = event.y - self.posy
        self.canvas1.move('carinha',self.vx, self.vy)

        self.posx += self.vx
        self.posy += self.vy
        '''
        self.canvas1.bind('<Right>',self.animaDir)
        self.canvas1.bind('<Left>',self.animaEsq)
        self.canvas1.bind('<Up>',self.animaCim)
        self.canvas1.bind('<Down>',self.animaBai)

    def animaDir(self, event): self.canvas1.move('carinha',self.vx,0)
    def animaEsq(self, event): self.canvas1.move('carinha',-self.vx,0)
    def animaCim(self, event): self.canvas1.move('carinha',0,-self.vy)
    def animaBai(self, event): self.canvas1.move('carinha',0,self.vy)
    '''

    def animacao(self):
        #Exclui todos os botões para criar a animação.
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        self.botao4.destroy()

        #Cria o canvas principal da animação.
        self.canvas1 = Canvas(self.frameGeral, width = 400, height = 300, bg = 'black')
        self.canvas1.focus_force()
        self.canvas1.pack()

        #Estabelece os pontos iniciais, centrais e a velocidade da esfera.
        self.p1 = 175
        self.p2 = 125
        self.mov_y = 150
        self.mov_x = 200
        self.vx = 5
        self.vy = 4

        #Cria as formas geométricas da esfera.
        self.carinha = self.canvas1.create_oval((self.p1,self.p2),(self.p1+50,self.p2+50), fill = 'lightblue', bd = None, tag = 'carinha')
        self.canvas1.create_oval((185,138),(197,150), fill = 'black', tag = 'carinha')
        self.canvas1.create_oval((203,138),(215,150), fill = 'black', tag = 'carinha')
        self.canvas1.create_arc((185,155),(215,165), start = 180, extent = 180, style = ARC, tag = 'carinha')

        self.botao1 = Button(self.frameGeral, text = 'START', command = self.comeca)
        self.botao1.pack()

    def comeca(self):
        self.anima()

    def anima(self):
        self.canvas1.move('carinha', self.vx, self.vy)
        self.mov_x += self.vx
        self.mov_y += self.vy

        if self.mov_x > 375 or self.mov_x < 25:
            self.vx *= -1
        if self.mov_y > 275 or self.mov_y < 25:
            self.vy *= -1
        self.master.after(25, self.anima)

    def grafico(self,i):
        #Exclui os botões antigos
        self.botao1.destroy()
        self.botao2.destroy()
        self.botao3.destroy()
        
        #Cria um novo canvas e altera a cor de fundo do frame geral
        self.canvas1 = Canvas(self.frameGeral, bg = 'lightgray', width = 300, height = 250)
        i['bg'] = 'lightblue'
        self.frameGeral['bg'] = 'lightgray'
        self.frame2 = Frame(self.frameGeral, bg = 'lightgray')
        self.label1 = Label(self.frame2, text = 'Fatia:', fg = 'blue')
        self.entrada1 = Entry(self.frame2)
        self.label2 = Label (self.frame2, text = '%', fg = 'blue')
        self.botao1 = Button(self.frame2, text = 'Desenhar', bg = 'lightgray', fg = 'blue', command = self.desenhar)
        
        self.canvas1.pack()
        self.frame2.pack()
        self.label1.pack(side = LEFT)
        self.entrada1.pack(side = LEFT)
        self.label2.pack(side = LEFT)
        self.botao1.pack(side = LEFT)

        self.canvas1.create_oval((50,25),(250,225), fill = 'blue')

    def desenhar(self):
        percentual = int(int(self.entrada1.get())*360/100)
        self.canvas1.create_arc((50,25),(250,225), fill = 'yellow', extent = percentual)

    def spfc(self):
        #Exclui os botões antigos
        self.botao1.destroy()
        self.botao2.destroy()

        #Cria os novos widgets
        self.canvas1 = Canvas(self.frameGeral, width = 400, height = 400, bg = 'blue')

        self.canvas1.pack()

        self.canvas1.create_polygon((75,50),(75,100),(200,250),(325,100),(325,50),fill = 'white')
        self.canvas1.create_line((75,50),(75,100),(200,250),(325,100),(325,50),(75,50), fill = 'black')
        self.canvas1.create_rectangle((79,54),(321,96),fill = 'black')
        self.canvas1.create_polygon((79,100),(196,240),(196,100), fill = 'red')
        self.canvas1.create_polygon((204,100),(204,240),(321,100), fill = 'black')
        self.canvas1.create_text((200,75), text = 'S P F C', font = ('Verdana',34, 'bold'), fill = 'white')

    def desenho(self):
        #Exclui os botões antigos
        self.botao1.destroy()
        self.botao2.destroy()
        
        #Cria as variáveis
        self.corLinha1 = 'blue'
        self.corLinha2 = 'yellow'
        self.corLinha3 = 'green'
        self.corLinha4 = 'red'
        self.posicao = [200,200]

        #Cria os widgets
        self.frame1 = Frame(self.frameGeral, bg = self.backG, bd = 20)
        self.frame2 = Frame(self.frameGeral, bg = self.backG)

        self.canvas1 = Canvas(self.frame1, width = 400, height = 400, bg = 'white')

        self.botao1 = Button(self.frame2, text = '  Cima  ', command = self.cima)
        self.botao2 = Button(self.frame2, text = '  Baixo  ', command = self.baixo)
        self.botao3 = Button(self.frame2, text = 'Esquerda', command = self.esquerda)
        self.botao4 = Button(self.frame2, text = ' Direita ', command = self.direita)

        #Empacota todos os widgets
        self.frame1.pack()
        self.canvas1.pack()
        self.frame2.pack()
        self.botao1.pack(side = LEFT)
        self.botao2.pack(side = LEFT)
        self.botao3.pack(side = LEFT)
        self.botao4.pack(side = LEFT)

    def cima(self):
        self.canvas1.create_line(self.posicao, (self.posicao[0],self.posicao[1]-40), fill = self.corLinha1)
        self.posicao = [self.posicao[0],self.posicao[1] - 40]

    def baixo(self):
        self.canvas1.create_line(self.posicao, (self.posicao[0],self.posicao[1]+30), fill = self.corLinha2)
        self.posicao = [self.posicao[0], self.posicao[1] +30]

    def esquerda(self):
        self.canvas1.create_line(self.posicao, (self.posicao[0]-30,self.posicao[1]), fill = self.corLinha3)
        self.posicao = [self.posicao[0]-30, self.posicao[1]]

    def direita(self):
        self.canvas1.create_line(self.posicao, (self.posicao[0]+40,self.posicao[1]), fill = self.corLinha4)
        self.posicao = [self.posicao[0]+40, self.posicao[1]]

i = frontEnd()

        

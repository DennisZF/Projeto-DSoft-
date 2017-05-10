#Projeto Design de Software -- Sistema de Agendamento de Horário para o FabLab

from tkinter import *

class Janela:
	def __init__(self, titulo):
		self = Tk()
		self.title(titulo)
class Login:
	def __init__(self):
		self.janela= Tk()
		self.janela.title("ENTRAR - FabLab Insper")
		
		titulo= Label(self.janela, text="FabLab", justify=CENTER, bg = 'white', width = 20, height=3, fg= 'red',font=("Helvetica", 35, 'bold'))
		titulo.pack(side = TOP)
		
		pede_usuario = Label(self.janela, text="Login:", height=1 ,font=("Helvetica", 16))
		pede_usuario.pack()
		
		self.usuario = Entry(self.janela, width= 25)
		self.usuario.pack(padx = 0, pady = 10)
		
		pede_senha = Label(self.janela, text="Senha:", height=1 ,font=("Helvetica", 16))
		pede_senha.pack()
		
		self.senha = Entry(self.janela, show="*",width = 25)
		self.senha.pack(padx = 0, pady = 10)
		
		entrar = Button( self.janela, text="Entrar", height =2,width = 9,bg= 'Red4',fg= 'Black',command=self.entrar, font =("Helvetica", 16, 'bold')).pack(side=BOTTOM)
		
	def entrar(self):
		self.janela.destroy()
		abre= Menu_principal()
		
		
class Menu_principal:
	def __init__(self):
		self.janela = Tk()
		self.janela.title("Página principal - FabLab Insper")
		
		titulo= Label(self.janela, text="FabLab", justify=CENTER, bg = 'white', width = 1366, height=3, fg= 'red',font=("Helvetica", 35, 'bold'))
		titulo.pack(side = TOP)
		
		canto = Frame(self.janela, relief = SUNKEN, cursor = 'hand2')
		canto.pack(side = TOP)
		
		self.calendario =Button(canto, text="Calendário",height = 1,width = 30,bg= 'Maroon', fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.agendamento = Button(canto, text="Agendamento",height = 1, width =30, bg='Tomato',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.cancelamento = Button(canto, text="Cancelamento",height = 1,width = 30,bg= 'Maroon',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.instrucoes = Button(canto, text="Instruções",height = 1,width = 30, bg='Tomato',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.historico = Button(canto, text="Histórico", height =1,width = 30,bg= 'Maroon',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.sair = Button(canto, text="Sair", height =1, width =15,bg= 'black',fg= 'White',command= self.sai,font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		
	def sai(self):
		self.atual = Sair(self.janela) 
		
class Sair():
	def __init__(self, janela):
		self.janela = janela
		
		frame=Frame(self.janela)
		frame.pack(padx=0, pady = 15)
		
		certeza= Label(frame, text="Tem certeza que deseja sair?", height=1 ,font=("Helvetica", 16))
		certeza.pack(side= TOP,padx=0, pady = 25)
		
		sim = Button(frame,text="Sim",height = 2,width = 9,bg= 'Seashell4',fg= 'Black',command=self.sim,font= ("Helvetica", 16, 'bold')).pack(side=LEFT)
		nao = Button(frame,text="Não",height = 2,width = 9,bg= 'Seashell4',fg= 'Black', command=self.nao, font=("Helvetica", 16, 'bold')).pack(side=RIGHT)
	def sim(self):
		self.janela.destroy()
		volta = Login()
	def nao(self):
		pass

class Calendario:
	def __init__(self, janela):
		self.janela = janela
		
		frame=Frame(self.janela)
		frame.pack(padx=0, pady = 15)
		
		certeza= Label(frame, text="Tem c deseja sair?", height=1 ,font=("Helvetica", 16))
		certeza.pack(side= TOP,padx=0, pady = 25)
		
		sim = Button(frame,text="oi", height =2,width = 9, bg='Seashell4',fg= 'Black', command= self.sim,font= ("Helvetica", 16, 'bold')).pack(side=LEFT)
		nao = Button(frame, text="aao",height = 2,width = 9,bg= 'Seashell4', fg='Black', command= self.nao, font=("Helvetica", 16, 'bold')).pack(side=RIGHT)


pagina1 = Login()
mainloop()
		
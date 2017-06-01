from tkinter import *
class Menu_principal:
	def __init__(self, dados, usuario):
		self.usuario = usuario
		self.dados = dados
		self.janela = Tk()	#Abre nova janela
		self.janela.wm_iconbitmap("icon_bitmap.ico")
		self.janela.geometry("{0}x{1}+0+0".format(self.janela.winfo_screenwidth(), self.janela.winfo_screenheight()))
		self.janela.title("Página principal - FabLab Insper")
		
		#------------ Cabeçalho ----------
		
		foto =PhotoImage(file="ferramentas.PNG")
		titulo=Label(self.janela, image=foto,width = 1366, height=200)
		titulo.image=foto
		titulo.pack(side = TOP)
		
		#------------ Menu ------------
		
		#Frame menu:
		canto = Frame(self.janela, relief = SUNKEN, cursor = 'hand2')
		canto.pack(side = TOP)
		
		#Botões:
		self.calendario =Button(canto, text="Calendário",height = 1,width = 25,bg= 'Maroon', fg='White',command= self.calendar, font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.agendamento = Button(canto, text="Agendamento",height = 1, width =25, bg='Tomato',fg='Black',command= self.agenda,font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.cancelamento = Button(canto, text="Cancelamento",height = 1,width = 25,bg= 'Maroon',fg='White',font =("Helvetica", 10, 'bold'), command= self.cancela).pack(side=LEFT)
		self.instrucoes = Button(canto, text="Instruções",height = 1,width = 25, bg='Tomato',fg='Black',font =("Helvetica", 10, 'bold'), command=self.instrucoes).pack(side=LEFT)
		self.historico = Button(canto, text="Histórico", height =1,width = 25,bg= 'Maroon',fg='White',font =("Helvetica", 10, 'bold'),command=self.historia).pack(side=LEFT)
		self.minha_conta =Button(canto, text="Minha Conta",height = 1,width = 25,bg= 'Tomato', fg='Black',font =("Helvetica", 10, 'bold'), command= self.conta).pack(side=LEFT)
		self.sair = Button(canto, text="Sair", height =1, width =15,bg= 'black',fg= 'White',command= self.sai,font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		
		
		#----------------- Imagem ------------
		
		foto2 = PhotoImage(file="Imagem_Menu.PNG")
		corpo = Label(self.janela, image=foto2, width = 1366, height=600)
		corpo.image=foto2
		corpo.pack(side = TOP)
		
	#------- Funções ---------	
	
	#Botão sair:
	
	def sai(self):
		from Classe_Sair import Sair
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame =Frame(self.janela)
		self.frame.pack(padx=0, pady = 15)
		s = Sair(self.janela,self.frame, self.dados) 
	
	def calendar(self):
		from Classe_Calendario import Calendario
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame =Frame(self.janela)
		self.frame.pack(side = LEFT, anchor ='n')
		self.menu = Frame(self.janela)
		self.menu.pack(side = RIGHT, padx = 30)
		C = Calendario(self.frame, self.dados, self.menu) 
	
	def agenda(self):
		from Classe_Agendamento import Agendamento
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame=Frame(self.janela)
		self.frame.pack(padx=0, pady=15)
		selecoes= Agendamento(self.frame, self.dados, self.usuario)
		
	def instrucoes(self):
		from Classe_Instruções import Instrucoes
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,"frame"):
			self.frame.destroy()
		self.menu=Frame (cursor="hand2")
		self.menu.pack(side=LEFT)
		self.frame=Frame(self.janela)
		self.frame.pack(padx=0, pady=15)
		I=Instrucoes(self.frame, self.dados, self.menu)
	
	def conta(self):
		from Classe_Minha_conta import Minha_conta
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame=Frame(self.janela)
		self.frame.pack(padx=0, pady=15)
		M= Minha_conta(self.frame, self.dados, self.usuario)

	def cancela(self):
		from Classe_Cancelamento import Cancelamento
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame=Frame(self.janela)
		self.frame.pack(padx=0, pady=15)
		A= Cancelamento(self.frame, self.dados, self.usuario)

	def historia(self):
		from Classe_Historico import Historico
		if hasattr(self, 'menu'):
			self.menu.destroy()
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame=Frame(self.janela)
		self.frame.pack(padx=0, pady=15)
		H = Historico(self.frame, self.dados, self.usuario)
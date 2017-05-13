from tkinter import *
class Menu_principal:
	def __init__(self, dados):
		self.dados = dados
		self.janela = Tk()					#Abre nova janela
		self.janela.title("Página principal - FabLab Insper")
		
		#------------ Cabeçalho ----------
		
		titulo= Label(self.janela, text="FabLab", justify=CENTER, bg = 'white', width = 1366, height=3, fg= 'red',font=("Helvetica", 35, 'bold'))
		titulo.pack(side = TOP)
		
		#------------ Menu ------------
		
		#Frame:
		canto = Frame(self.janela, relief = SUNKEN, cursor = 'hand2')
		canto.pack(side = TOP)
		
		#Botões:
		self.calendario =Button(canto, text="Calendário",height = 1,width = 25,bg= 'Maroon', fg='Black',command= self.calendar, font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.agendamento = Button(canto, text="Agendamento",height = 1, width =25, bg='Tomato',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.cancelamento = Button(canto, text="Cancelamento",height = 1,width = 25,bg= 'Maroon',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.instrucoes = Button(canto, text="Instruções",height = 1,width = 25, bg='Tomato',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.historico = Button(canto, text="Histórico", height =1,width = 25,bg= 'Maroon',fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.minha_conta =Button(canto, text="Minha Conta",height = 1,width = 25,bg= 'Tomato', fg='Black',font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		self.sair = Button(canto, text="Sair", height =1, width =15,bg= 'black',fg= 'White',command= self.sai,font =("Helvetica", 10, 'bold')).pack(side=LEFT)
		
	#------- Funções ---------	
	
	#Botão sair:
	def sai(self):
		from Classe_Sair import Sair
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame =Frame(self.janela)
		self.frame.pack(padx=0, pady = 15)
		s = Sair(self.janela,self.frame, self.dados) 
	def calendar(self):
		from Classe_Calendario import Calendario
		if hasattr(self,'frame'):
			self.frame.destroy()
		self.frame =Frame(self.janela)
		self.frame.pack(padx=0, pady = 15)
		C = Calendario(self.frame) 
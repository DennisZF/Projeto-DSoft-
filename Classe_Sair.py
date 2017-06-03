from tkinter import *
class Sair:
	def __init__(self, janela, frame, dados,menu):
		self.dados = dados
		self.janela = janela
		self.frame=frame
		self.menu = menu
		#-----------pergunta
		certeza= Label(self.frame, text="Tem certeza que deseja sair?", height=1 ,font=("Helvetica", 16))
		certeza.pack(side= TOP,padx=0, pady = 25)
		#------botões
		sim = Button(self.frame,text="Sim",height = 2,width = 9,bg= 'Seashell4',fg= 'Black',command=self.sim,font= ("Helvetica", 16, 'bold'),  cursor = 'hand2').pack(side=LEFT)
		nao = Button(self.frame,text="Não",height = 2,width = 9,bg= 'Seashell4',fg= 'Black', command=self.nao, font=("Helvetica", 16, 'bold'),  cursor = 'hand2').pack(side=RIGHT)
	
	#-----------funções para seus respectivos botões
	def sim(self):
		self.janela.destroy()
		
		from Classe_login import Login
		
		volta = Login(self.dados)
	def nao(self):
		self.frame.destroy()
		foto2 = PhotoImage(file="Imagem_Menu.PNG")
		self.menu.pack(side = TOP)
		self.menu2 = Label(self.menu, image=foto2, width = 1366, height=600)
		self.menu2.image=foto2
		self.menu2.pack(side = TOP)

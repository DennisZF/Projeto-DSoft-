from tkinter import *
class Sair:
	def __init__(self, janela, frame, dados):
		self.dados = dados
		self.janela = janela
		self.frame=frame
		
		certeza= Label(self.frame, text="Tem certeza que deseja sair?", height=1 ,font=("Helvetica", 16))
		certeza.pack(side= TOP,padx=0, pady = 25)
		
		sim = Button(self.frame,text="Sim",height = 2,width = 9,bg= 'Seashell4',fg= 'Black',command=self.sim,font= ("Helvetica", 16, 'bold')).pack(side=LEFT)
		nao = Button(self.frame,text="Não",height = 2,width = 9,bg= 'Seashell4',fg= 'Black', command=self.nao, font=("Helvetica", 16, 'bold')).pack(side=RIGHT)
	def sim(self):
		self.janela.destroy()
		
		from Classe_login import Login
		
		volta = Login(self.dados)
	def nao(self):
		self.frame.destroy()
		#o ideal seria colocar alguma pag de entrada para que agora apareca

from tkinter import *
from tkinter import messagebox

class Alteracao_de_senha:
	def __init__(self,janela, frame, dados, usuario):
		self.frame = frame
		self.dados = dados
		self.usuario = usuario
		self.janela = janela
		
		self.alteracao = Label(self.frame, text = 'Alteração de senha', font=('Helvetica', 30,'bold'))
		self.alteracao.grid(row =0, columnspan = 2, pady = 30)
		
		#-----espaço Nova senha
		nova_senha = Label(self.frame, text="Nova senha:", height=1 ,font=("Helvetica", 14))
		nova_senha.grid(row=2, column = 0,pady = 10)
		self.nova_senha = Entry(self.frame, width= 25, font=('Helvetica',14), show = "*")
		self.nova_senha.grid(row=2, column = 1,pady = 10, padx=10) 
		
		#-----espaço Repete nova senha
		repete_nova_senha = Label(self.frame, text="Repita a nova senha:", height=1 ,font=("Helvetica", 14))
		repete_nova_senha.grid(row=4, column = 0,pady = 10)
		self.repete_nova_senha = Entry(self.frame, width= 25, font=('Helvetica',14), show = "*")
		self.repete_nova_senha.grid(row=4, column = 1,pady = 10, padx=10) 
		
		self.altera = Button(self.frame, text = "Salvar nova senha", font=('Helvetica', 15, 'bold'), height = 2, bg = 'Red4', cursor = 'hand2', command = self.muda)
		self.altera.grid(row = 6, column = 0, columnspan = 1, padx= 10, pady=10)
		
		#----- atualização
	def muda(self):
		tudo = self.preenchido()
		if tudo == True:
			if self.nova_senha.get() == self.repete_nova_senha.get():
				self.dados.muda_senha(self.usuario,self.nova_senha.get())
				notificacao = messagebox.showinfo("Salvo", "Sua senha foi redefinida")
				for child in self.frame.winfo_children():
					child.destroy()
				from Classe_Minha_conta import Minha_conta
				M= Minha_conta(self.janela,self.frame, self.dados, self.usuario)
			else:
				if hasattr(self, 'notifica'):
					self.notifica.destroy()
				self.notifica = Label(self.frame, text = 'Senhas não compatíveis', font= ("Helvetica", 10, 'bold'),fg = 'red')
				self.notifica.grid(row = 8, column = 0, columnspan = 1, padx= 10, pady = 10)
		else:
			for x in tudo:
				x.configure(bg = 'Khaki1')
			if hasattr(self, 'notifica'):
				self.notifica.destroy()
			self.notifica = Label(self.frame, text = 'Preencha todos os espaços', font= ("Helvetica", 10, 'bold'),fg = 'red')
			self.notifica.grid(row = 8, column = 0, columnspan = 1, padx= 10, pady = 10)
			
		#-------verificação de preenchiemnto  
	def preenchido(self):
		vazios = []
		if self.nova_senha.get() == "":
			vazios.append(self.nova_senha)
		if self.repete_nova_senha.get() == "":
			vazios.append(self.repete_nova_senha)
		if len(vazios) == 0:
			return True
		else:
			return vazios
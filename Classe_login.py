from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

class Login:
	def __init__(self, dados):
		self.janela= Tk()				#Abre a janela
		self.janela.title("ENTRAR - FabLab Insper")
		
		self.dados = dados
		
		#Cabeçalho:	
		titulo= Label(self.janela, text="FabLab", justify=CENTER, bg = 'white', width = 29, height=3, fg= 'red',font=("Helvetica", 35, 'bold'))
		titulo.pack(side = TOP)
		
		#--------- Idententificação --------
		
		#Usuário:
		pede_usuario = Label(self.janela, text="Login:", height=1 ,font=("Helvetica", 14))			#"Texto" pedindo o nome de usuário
		pede_usuario.pack()
		
		self.usuario = Entry(self.janela, width= 25)												#Caixa de texto que recebe o que o usuário digitar
		self.usuario.pack(padx = 0, pady = 10)
		
		#Senha:
		pede_senha = Label(self.janela, text="Senha:", height=1 ,font=("Helvetica", 14))			#"Texto" pedindo a senha
		pede_senha.pack()
		
		self.senha = Entry(self.janela, show="*",width = 25)										#Caixa de texto que a senha recebe o que o usuário digitar
		self.senha.pack()																			#Segurança: o que o usuário digitar ira aparecer como "*" na tela
		
		#Botão para entrar:
		entrar = Button( self.janela, text="Entrar", height =2,width = 9,bg= 'Red4',fg= 'Black',command=self.entrar, font =("Helvetica", 16, 'bold'))
		self.janela.bind("<Return>", self.entrar)
		entrar.pack(side=BOTTOM, pady=15)
		
		#Ainda não tem cdastro:
		self.clique = Label(self.janela, text="Clique aqui", fg="red", cursor="hand2", font=("Helvetica", 10, 'underline'))			#link que abre a página de cadastro
		self.clique.pack(side= RIGHT, pady=15)
		self.clique.bind("<Button-1>", self.cadastrar)
		
		self.pergunta= Label(self.janela, text="Ainda não é cadastrado?", justify=CENTER,font=("Helvetica", 10))					#"Texto que se refere ao link
		self.pergunta.pack(side = RIGHT)
	
	#------- Funções ---------
	
	#Cadastrar:
	def cadastrar(self,event):
		from Classe_Cadastro import Cadastro
		c= Cadastro(self.dados)					#Abre página de Cadastro
	
	#Entrar:
	def entrar(self, event = None):
		u= self.usuario.get()				#Pega o usuário que foi digitado
		s= self.senha.get()					#Pega a senha que foi digitada
		verifica= self.dados.verificacao(u,s)
		if verifica == True:
			from Classe_Menu_principal import Menu_principal
			self.janela.destroy()				#Fecha a janela de login
			abre= Menu_principal(self.dados)				#Abre a janela principal
		else:
			if hasattr(self, 'erro'):
				self.erro.destroy()
			self.erro= Label(self.janela, text="Usuário e/ou senha incorretos. Por favor, tente novamente",fg= 'red', justify=CENTER,font=("Helvetica", 12, 'bold'))					#"Texto que se refere ao link
			self.erro.pack(side= BOTTOM , padx = 35)
			self.usuario.configure(bg='Khaki1')
			self.senha.configure(bg = 'Khaki1')
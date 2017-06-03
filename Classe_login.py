from tkinter import *            #importa o pacote e permite que este seja utilizado sem "chamada" (tk.)
import tkinter.font as tkFont
import tkinter.ttk as ttk

class Login:
	def __init__(self, dados):
		#--------janela
		self.janela= Tk()				#Abre a janela
		self.janela.title("ENTRAR - FabLab Insper")
		self.janela.wm_iconbitmap("icon_bitmap.ico")
		
		self.dados = dados
		
		#-----------Cabeçalho:	
		foto =PhotoImage(file="ferramentas.PNG")
		titulo=Label(self.janela, image=foto,width=700, height=170)
		titulo.image=foto
		titulo.pack(side = TOP)
		
		#--------- Idententificação --------
		
		#---------setor Usuário:
		pede_usuario = Label(self.janela, text="Login:", height=1 ,font=("Helvetica", 14))			
		pede_usuario.pack(pady = 15)
		#-----------entrada do usuário
		self.usuario = Entry(self.janela, width= 25)												
		self.usuario.pack(padx = 0)
		
		#---------setor Senha:
		pede_senha = Label(self.janela, text="Senha:", height=1 ,font=("Helvetica", 14))			
		pede_senha.pack(pady=15)
		#---------entrada do usuário
		self.senha = Entry(self.janela, show="*",width = 25)								
		self.senha.pack()															
		
		#---------Botão para entrar:
		entrar = Button( self.janela, text="Entrar", height =2,width = 9,bg= 'Red4',fg= 'white',command=self.entrar, font =("Helvetica", 16, 'bold'),cursor="hand2")
		self.janela.bind("<Return>", self.entrar)
		entrar.pack(side=BOTTOM, pady=15)
		
		#-------------Ainda não tem cadastro:
		self.clique = Label(self.janela, text="Clique aqui", fg="red", cursor="hand2", font=("Helvetica", 10, 'underline'))	
		self.clique.pack(side= RIGHT, pady=15)
		self.clique.bind("<Button-1>", self.cadastrar)
		#-----------pergunta
		self.pergunta= Label(self.janela, text="Ainda não é cadastrado?", justify=CENTER,font=("Helvetica", 10))	
		self.pergunta.pack(side = RIGHT)
	
	#------- Funções ---------
	
	#------Cadastrar: abrir página de cadastro
	def cadastrar(self,event):
		from Classe_Cadastro import Cadastro
		c= Cadastro(self.dados)					
	
	#------------Entrar:
	def entrar(self, event = None):
		u= self.usuario.get()				
		s= self.senha.get()					
		verifica= self.dados.verificacao(u,s)
		if verifica == True:
			from Classe_Menu_principal import Menu_principal
			self.janela.destroy()			
			abre= Menu_principal(self.dados, u)			
		else:
			if hasattr(self, 'erro'):
				self.erro.destroy()
			self.erro= Label(self.janela, text="Usuário e/ou senha incorretos. Por favor, tente novamente",fg= 'red', justify=CENTER,font=("Helvetica", 12, 'bold'))					#"Texto que se refere ao link
			self.erro.pack(side= BOTTOM , padx = 35)
			self.usuario.configure(bg='Khaki1')
			self.senha.configure(bg = 'Khaki1')
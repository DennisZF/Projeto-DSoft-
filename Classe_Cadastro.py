from tkinter import *
import tkinter.ttk as ttk


class Cadastro:
		def __init__(self, dados):
			self.dados = dados
			
			#-----Abre a janela
			self.pagina_nova= Tk()					
			self.pagina_nova.title("Cadastro - FabLab Insper")
			self.pagina_nova.wm_iconbitmap("icon_bitmap.ico")
			self.pagina_nova.bind("<Return>", self.envia)
			#-----título da página
			titulo_cadastro = Label(self.pagina_nova, text="Ficha de cadastro", height=1 ,font=("Helvetica", 25, 'bold'))	
			titulo_cadastro.grid(row=0, columnspan=2)

			#-------- Formulário -------
			
			#------ espaço Nome
			pede_nome = Label(self.pagina_nova, text="Nome:", height=1 ,font=("Helvetica", 10))
			pede_nome.grid(row=3, column = 0)
			self.nome = Entry(self.pagina_nova, width= 25)
			self.nome.grid(row=3, column = 1) 
			
			#------ espaço Curso
			pede_curso = Label(self.pagina_nova, text="Curso:", height=1 ,font=("Helvetica", 10))
			pede_curso.grid(row=5, column = 0)
			self.curso=ttk.Combobox(self.pagina_nova,width= 22)
			#------- combobox de seleção
			self.curso.grid(row=5, column=1) 
			self.curso['values']=('Administração','Economia','Engenharia de Computação','Engenharia Meacânica','Engenharia Mecatrônica', 'Outro')
			self.curso.current(0)
			
			#--------espaço Semestre
			pede_semestre = Label(self.pagina_nova, text="Semestre:", height=1 ,font=("Helvetica", 10))
			pede_semestre.grid(row=7, column = 0)
			self.semestre = Entry(self.pagina_nova, width= 25)
			self.semestre.grid(row=7, column = 1) 
			
			#---------espaço Número de matrícula
			pede_matricula = Label(self.pagina_nova, text="Número de matrícula:", height=1 ,font=("Helvetica", 10))
			pede_matricula.grid(row=9, column = 0)
			self.matricula = Entry(self.pagina_nova, width= 25)
			self.matricula.grid(row=9, column = 1) 
			
			#--------espaço Email
			pede_email = Label(self.pagina_nova, text="Email do Insper:", height=1 ,font=("Helvetica", 10))
			pede_email.grid(row=11, column = 0)
			self.email = Entry(self.pagina_nova, width= 25)
			self.email.grid(row=11, column = 1) 
			
			#---------espaço Nome de usuário
			pede_usuario = Label(self.pagina_nova, text="Nome de usuário:", height=1 ,font=("Helvetica", 10))
			pede_usuario.grid(row=13, column = 0)
			self.usuario = Entry(self.pagina_nova, width= 25)
			self.usuario.grid(row=13, column = 1) 
			
			#--------- espaço Senha
			pede_senha = Label(self.pagina_nova, text="Senha:", height=1 ,font=("Helvetica", 10))
			pede_senha.grid(row=15, column = 0)
			self.senha = Entry(self.pagina_nova, width= 25,show='*')
			self.senha.grid(row=15, column = 1) 
			
			#-------espaço Repetição da senha
			pede_repete = Label(self.pagina_nova, text="Repita a senha:", height=1 ,font=("Helvetica", 10))
			pede_repete.grid(row=17, column = 0)
			self.repete = Entry(self.pagina_nova, width= 25,show='*')
			self.repete.grid(row=17, column = 1) 
			
			#------- Botão de envio
			enviar = Button( self.pagina_nova, text="Enviar",width = 9,bg= 'Red4',fg= 'white',command=self.envia, font =("Helvetica", 16, 'bold'),cursor="hand2")
			enviar.grid(rowspan = 19, column = 1, pady=5)
			
		#------- Função -------
		def envia(self, event = None):
			tudo = self.preenchido()
			if tudo == True:
				if self.curso.get() in self.curso['values']:
					if self.senha.get() == self.repete.get():
						add = self.dados.usuarioexistente(self.usuario.get(), self.senha.get(),self.nome.get(),self.curso.get(), self.semestre.get(), self.matricula.get(), self.email.get())
						if add == True:
							self.pagina_nova.destroy()
						else:
							if hasattr(self,'notifica'):
								self.notifica.destroy()
							self.notifica= Label(self.pagina_nova, text="Usuário já existente",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
							self.notifica.grid(row = 2, columnspan = 2)
					else:
						if hasattr(self,'notifica'):
								self.notifica.destroy()
						self.notifica= Label(self.pagina_nova, text="Senhas não compatíveis",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
						self.notifica.grid(row = 2, columnspan = 2)
				else:
					self.notifica= Label(self.pagina_nova, text="Preencha todos os campos adequadamente",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
					self.notifica.grid(row = 2, columnspan = 2)
				
			else:
				for info in tudo:
					info.configure(bg = 'Khaki1')
				self.notifica= Label(self.pagina_nova, text="Preencha todos os campos",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
				self.notifica.grid(row = 2, columnspan = 2)
				
		#-------- verificação de preenchimento	
		def preenchido(self):
			vazios=[]
			for x in [self.usuario, self.senha, self.nome, self.semestre, self.matricula, self.email, self.repete, self.curso]:
				a = x.get()
				if a == "":
					vazios.append(x)
			if vazios == []:
				return True
			else:
				return vazios
from tkinter import *

class Minha_conta:
	def __init__(self, frame,dados, usuario):
		self.data  = dados
		self.dados= dados.dados[usuario]
		self.frame = frame
		self.user = usuario
		
		self.titulo = Label(self.frame, text = "Minha conta", font=('Helvetica', 30,'bold'))
		self.titulo.grid(row =0, columnspan = 2, pady = 30)
		
		pede_nome = Label(self.frame, text="Nome:", height=1 ,font=("Helvetica", 14))
		pede_nome.grid(row=3, column = 0, pady = 10)
		self.nome = Entry(self.frame, width= 25,font=('Helvetica',14))
		self.nome.insert(END, self.dados[1])
		self.nome.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.nome.grid(row=3, column = 1, pady = 10, padx = 10) 
	
		#Curso
		pede_curso = Label(self.frame, text="Curso:", height=1 ,font=("Helvetica", 14))
		pede_curso.grid(row=5, column = 0,pady = 10)
		self.curso = Entry(self.frame, width= 25,font=('Helvetica',14))
		self.curso.insert(END, self.dados[2])
		self.curso.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.curso.grid(row=5, column = 1,pady = 10, padx=10) 
			
			
		#Semestre
		pede_semestre = Label(self.frame, text="Semestre:", height=1 ,font=("Helvetica", 14))
		pede_semestre.grid(row=7, column = 0,pady = 10)
		self.semestre = Entry(self.frame, width= 25, font=('Helvetica',14))
		self.semestre.insert(END, self.dados[3])
		self.semestre.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.semestre.grid(row=7, column = 1,pady = 10, padx=10) 
			
		#Número de matrícula
		pede_matricula = Label(self.frame, text="Número de matrícula:", height=1 ,font=("Helvetica", 14))
		pede_matricula.grid(row=9, column = 0,pady = 10)
		self.matricula = Entry(self.frame, width= 25, font=('Helvetica',14))
		self.matricula.insert(END, self.dados[4])
		self.matricula.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.matricula.grid(row=9, column = 1,pady = 10, padx=10) 
			
		#Email
		pede_email = Label(self.frame, text="Email do Insper:", height=1 ,font=("Helvetica", 14))
		pede_email.grid(row=11, column = 0,pady = 10)
		self.email = Entry(self.frame, width= 25, font=('Helvetica',14))
		self.email.insert(END, self.dados[5])
		self.email.configure(state = 'disabled', disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.email.grid(row=11, column = 1,pady = 10, padx=10) 
			
		#Nome de usuário
		pede_usuario = Label(self.frame, text="Nome de usuário:", height=1 ,font=("Helvetica", 14))
		pede_usuario.grid(row=13, column = 0,pady = 10)
		self.usuario = Entry(self.frame, width= 25, font=('Helvetica',14))
		self.usuario.insert(END, usuario)
		self.usuario.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.usuario.grid(row=13, column = 1,pady = 10, padx=10) 
			
		#Senha
		pede_senha = Label(self.frame, text="Senha:", height=1 ,font=("Helvetica", 14))
		pede_senha.grid(row=15, column = 0,pady = 10)
		self.senha = Entry(self.frame, width= 25, font=('Helvetica',14))
		self.senha.insert(END, self.dados[0])
		self.senha.configure(state = 'disabled',disabledbackground= "NavajoWhite", disabledforeground= 'Peru')
		self.senha.grid(row=15, column = 1,pady = 10, padx=10) 
		
		
		self.editar = Button(self.frame, height= 2 , width = 15, text = 'Editar', font = ('Helvetica', 12), bg='tomato', command = self.edit)
		self.editar.grid(row=9, column = 4, padx = 20)
	def salvar(self):
		tudo = self.preenchido()
		if tudo == True:
			self.data.deletausuario(self.user)
			self.data.addusuario(self.usuario.get(), self.senha.get(),self.nome.get(),self.curso.get(), self.semestre.get(), self.matricula.get(), self.email.get())
			for x in [self.usuario, self.senha, self.nome,self.curso, self.semestre, self.matricula, self.email, self.curso]:
				x.configure(state = 'disabled')
			self.salva.destroy()
			self.editar = Button(self.frame, height= 2 , width = 15, text = 'Editar', font = ('Helvetica', 12), bg='tomato', command = self.edit)
			self.editar.grid(row=9, column = 4, padx = 20)
		else:
			for info in tudo:
				info.configure(bg = 'Khaki1')
				self.notifica= Label(self.frame, text="Preencha todos os campos",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
				self.notifica.grid(row = 2, columnspan = 2)
	def preenchido(self):
		vazios=[]
		for x in [self.usuario, self.senha, self.nome,self.curso, self.semestre, self.matricula, self.email, self.curso]:
			a = x.get()
			if a == "":
				vazios.append(x)
		if vazios == []:
			return True
		else:
			return vazios
			
	def edit(self):
		for x in [self.usuario, self.senha, self.nome,self.curso, self.semestre, self.matricula, self.email, self.curso]:
			x.configure(state = 'normal')
		self.editar.destroy()
		self.salva = Button(self.frame, height = 2, width = 25, text='Salvar alterações',font = ('Helvetica', 12), bg='tomato', command = self.salvar)
		self.salva.grid(row= 9, column = 4, padx = 20)
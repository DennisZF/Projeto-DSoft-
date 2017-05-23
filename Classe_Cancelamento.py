from tkinter import *
from tkinter import messagebox
class Cancelamento:
	def __init__(self, frame, dados, usuario):
		self.frame = frame
		self.dados = dados
		self.usuario = usuario
		
		self.titulo = Label( self.frame, text= 'Cancelamento' ,font=("Helvetica", 30, 'bold'))
		self.titulo.grid(rowspan=1, columnspan = 6, pady = 15)
		
		from Classe_Calendar2 import Calendar2
		
		calendario = Calendar2(self.frame)  #calendário para escolha de datas
		calendario.grid(row = 4, rowspan=4, column=1, padx= 10)
		
		self.escolher = Label(self.frame, text=" Selecione a data ",font=("Helvetica", 8, 'bold'))    #instrução
		self.escolher.grid(row=3, column=1, padx= 10)
		
		self.escolha = Label(self.frame,font=("Helvetica", 8, 'bold'))    #instrução
		self.escolha.grid(row=8, column=1, padx= 10)
		selecao = calendario.quando_selecionada(self.atualiza)		#pega a seleção e guarda numa variável
		
		self.escolha2= Label(self.frame, text=" Selecione o setor do FabLab ", font=("Helvetica",8, 'bold'))
		self.escolha2.grid(row=3, column=2, padx= 10)     #instrução
		self.combo=ttk.Combobox(self.frame)
		self.combo.grid(row=4, column=2, padx= 10)  #combobox de seleção
		self.combo['values']=('Fresadora','Impressora 3D','Costura','Marcenaria','Eletrônica')
		self.combo.current(0) #default é o primeiro termo

	
		self.escolha5= Label(self.frame, text=" Selecione o horário de início ", font=("Helvetica",8, 'bold'))     #instrução
		self.escolha5.grid(row=6, column=2, padx= 10)
		self.combo4=ttk.Combobox(self.frame)       #combobox de seleção
		self.combo4.grid(row=7, column=2, padx= 10)
		self.combo4['values']=('8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30')
		self.combo4.current(0) #default é o primeiro termo
		
		self.cancelar = Button(self.frame, height= 2 , width = 15, text = 'Cancelar', font = ('Helvetica', 12), bg='tomato', command = self.cancela,cursor="hand2")
		self.cancelar.grid(row=9, column = 2)
	
	def atualiza(self,x):
		self.escolha['text'] = x;
		self.data=x
	
	def cancela(self):
		confirma = messagebox.askquestion("Confirmação de envio", "Tem certeza que deseja cancelar a reserva do dia {} às {} no(a) {}?".format(self.data, self.combo4.get(), self.combo.get()))
		if confirma == 'yes':
			try:
				if self.dados.dados[self.usuario][1]==self.dados.horarios[self.data][self.combo4.get()][self.combo.get()]["nome"]:
					self.dados.cancelahorario(self.data, self.combo4.get(), self.combo.get())
					for child in self.frame.winfo_children():
								child.destroy()
					self.sucesso = Label(self.frame, text = "Seu cancelamento foi realizado com sucesso!", font = ("Helvetica", 15, 'bold'))
					self.sucesso.grid(row = 4, rowspan = 3, columnspan= 2)
				else: 
					erro = messagebox.showerror("Erro","Não há um horário registrado em seu nome")
			except:
				erro2 = messagebox.showerror("Erro","Não há nenhum agendamento compatível")
			
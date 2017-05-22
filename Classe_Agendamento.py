from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import datetime

class Agendamento:
	def __init__(self,frame, dados, usuario):
		self.usuario = usuario
		self.dados = dados
		titulo=Label(frame, text="Agendamento", height=1, font=("Helvetica", 30, 'bold'))
		titulo.grid(rowspan=1, columnspan = 6, pady = 15)        #título
		
		from Classe_Calendar2 import Calendar2
		
		calendario = Calendar2(frame)  #calendário para escolha de datas
		calendario.grid(row = 4, rowspan=4, column=1, padx= 10)
		
		self.escolher = Label(frame, text=" Selecione uma data ",font=("Helvetica", 8, 'bold'))    #instrução
		self.escolher.grid(row=3, column=1, padx= 10)
		
		self.escolha = Label(frame,font=("Helvetica", 8, 'bold'))    #instrução
		self.escolha.grid(row=8, column=1, padx= 10)
		selecao = calendario.quando_selecionada(self.atualiza)		#pega a seleção e guarda numa variável
		
		self.escolha2= Label(frame, text=" Selecione um setor do FabLab ", font=("Helvetica",8, 'bold'))
		self.escolha2.grid(row=3, column=2, padx= 10)     #instrução
		self.combo=ttk.Combobox(frame)
		self.combo.grid(row=4, column=2, padx= 10)  #combobox de seleção
		self.combo['values']=('Fresadora','Impressora 3D','Costura','Marcenaria','Eletrônica')
		self.combo.current(0) #default é o primeiro termo

		self.escolha3= Label(frame, text=" Você sabe utilizar esse setor sozinho? ", font=("Helvetica", 8, 'bold'))   #pergunta
		self.escolha3.grid(row=6, column=2, padx= 10)
		self.combo2=ttk.Combobox(frame)    #combobox de seleção
		self.combo2.grid(row=7, column=2, padx= 10)
		self.combo2['values']=('sim','não')
		self.combo2.current(1) #default é o segundo termo

		self.escolha4= Label(frame, text=" Selecione o número de pessoas ", font=("Helvetica", 8, 'bold'))     #instrução
		self.escolha4.grid(row=3, column=3, padx= 10)
		self.combo3=ttk.Combobox(frame)       #combobox de seleção
		self.combo3.grid(row=4, column=3, padx= 10)
		self.combo3['values']=('1','2','3','4','5','6')
		self.combo3.current(0) #default é o primeiro termo
		
		self.escolha6= Label(frame, text=" Selecione o tempo necessaário: ", font=("Helvetica",8, 'bold'))     #instrução
		self.escolha6.grid(row=4, column=4, padx= 10)
		self.combo5=ttk.Combobox(frame)       #combobox de seleção
		self.combo5.grid(row=5, column=4, padx= 10)
		self.combo5['values']=('1','2','3','4')
		self.combo5.current(0) #default é o primeiro termo
		
		
		self.escolha5= Label(frame, text=" Selecione um horário de início ", font=("Helvetica",8, 'bold'))     #instrução
		self.escolha5.grid(row=6, column=3, padx= 10)
		self.combo4=ttk.Combobox(frame)       #combobox de seleção
		self.combo4.grid(row=7, column=3, padx= 10)
		self.combo4['values']=('8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30')
		self.combo4.current(0) #default é o primeiro termo
		
		self.frame = frame
		
		self.enviar = Button(self.frame, height= 2 , width = 15, text = 'Enviar', font = ('Helvetica', 12), bg='tomato', command = self.envia,cursor="hand2")
		self.enviar.grid(row=9, column = 2)
	
	def atualiza(self,x):
		self.escolha['text'] = x;
		self.data=x
		
	def envia(self):
		confirma = messagebox.askquestion("Confirmação de envio", "Tem certeza que deseja enviar o formulário?")
		if confirma == 'yes':
			tudo = self.preenchido()
			if tudo == True:
				dia = int(self.data[0:2])
				mes = int(self.data[3:5])
				ano = int(self.data[6:])
				if 	datetime.datetime(ano, mes, dia).strftime("%A") == "Thursday":
					if hasattr(self,'notifica'):
						self.notifica.destroy()
					self.notifica= Label(self.frame, text="Não é possível agendar horários de Quinta-feira",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))					#"Texto que se refere ao link
					self.notifica.grid(row = 2,column=1)
				else:
					if self.combo2.get() == 'não':
						if hasattr(self,'notifica'):
							self.notifica.destroy()
						self.notifica= Label(self.frame, text="Não é possível agendar horários sem já ter a inicialização do setor. Contate alguém do FabLab Insper para mais informações",fg= 'red', justify=CENTER,font=("Helvetica", 9, 'bold'))					#"Texto que se refere ao link
						self.notifica.grid(rowspan = 2,columnspan=5, pady=10)
					self.dados.addhorario(self.data, self.combo4.get(), self.dados.dados[self.usuario][1],self.combo.get(), self.combo3.get(), self.combo5.get())
			else:
				if hasattr(self,'notifica'):
					self.notifica.destroy()
				self.notifica= Label(self.frame, text="Preencha todos os campos",fg= 'red', justify=CENTER,font=("Helvetica", 15, 'bold'))					#"Texto que se refere ao link
				self.notifica.grid(row = 2,column=1)
	def preenchido(self):
		vazio=[]
		if self.escolha['text'] == "":
			vazio.append("data")
		if self.combo4.get() not in self.combo4['values']:
			vazio.append("combo4")
		if self.combo.get() not in self.combo['values']:
			vazio.append("setor")
		if self.combo3.get() not in self.combo3['values']:
			vazio.append("pessoas")
		if self.combo5.get() not in self.combo5['values']:
			vazio.append("tempo")
		if len(vazio) == 0:
			return True
		else:
			return vazio
		

	
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import datetime

class Agendamento:
	def __init__(self,frame, dados, usuario):
		self.usuario = usuario
		self.dados = dados
		#------- título
		titulo=Label(frame, text="Agendamento", height=1, font=("Helvetica", 30, 'bold'))
		titulo.grid(rowspan=1, columnspan = 6, pady = 15)    
		
		from Classe_Calendar2 import Calendar2
		#------ calendário para a escolha de datas
		calendario = Calendar2(frame)  
		calendario.grid(row = 4, rowspan=4, column=1, padx= 10)
		
		#-----instrução
		self.escolher = Label(frame, text="1. Selecione uma data ",font=("Helvetica", 8, 'bold')) 
		self.escolher.grid(row=3, column=1, padx= 10)
		
		self.escolha = Label(frame,font=("Helvetica", 8, 'bold'))  
		self.escolha.grid(row=8, column=1, padx= 10)
		#------armazenamento da seleção
		selecao = calendario.quando_selecionada(self.atualiza_calendario)
		
		#-------instrução
		self.escolha2= Label(frame, text="2.  Selecione um setor do FabLab ", font=("Helvetica",8, 'bold'))
		self.escolha2.grid(row=3, column=2, padx= 10)
		#------combobox de seleção
		self.combo=ttk.Combobox(frame)
		self.combo.grid(row=4, column=2, padx= 10)
		self.combo['values']=('---Selecione---','Fresadora','Impressora 3D','Costura','Marcenaria','Eletrônica')
		#-------função de clique e atualização
		self.combo.bind('<<ComboboxSelected>>', self.atualiza_setor)
		
		#------pergunta
		self.escolha3= Label(frame, text="6. Você sabe utilizar este setor sozinho? ", font=("Helvetica", 8, 'bold')) 
		self.escolha3.grid(row=6, column=3, padx= 10)
		#---------combobox de seleção
		self.combo2=ttk.Combobox(frame) 
		self.combo2.grid(row=7, column=3, padx= 10)
		self.combo2['values']=('sim','não')
		#------ posição do valor adotado como padrão
		self.combo2.current(1)
		
		#-------instrução
		self.escolha4= Label(frame, text="5.  Selecione o número de pessoas ", font=("Helvetica", 8, 'bold')) 
		self.escolha4.grid(row=6, column=2, padx= 10)
		#------- combobox de seleção
		self.combo3=ttk.Combobox(frame) 
		self.combo3.grid(row=7, column=2, padx= 10)
		self.combo3['values']=(1,2,3,4,5,6)
		#------ posição do valor adotado como padrão
		self.combo3.current(0) 
		
		#------instrução
		self.escolha6= Label(frame, text="3.  Selecione o tempo necessaário: ", font=("Helvetica",8, 'bold')) 
		self.escolha6.grid(row=3, column=3, padx= 10)
		#------ combobox de seleção
		self.combo5=ttk.Combobox(frame)     
		#------ função de clique e atualização
		self.combo5.bind('<<ComboboxSelected>>', self.atualiza_inicio)
		self.combo5.grid(row=4, column=3, padx= 10)
		
		#------instrução
		self.escolha5= Label(frame, text="4. Selecione um horário de início ", font=("Helvetica",8, 'bold')) 
		self.escolha5.grid(row=4, column=4, padx= 10)
		#------ combobox de seleção
		self.combo4=ttk.Combobox(frame)
		self.combo4.grid(row=5, column=4, padx= 10)
		
		self.frame = frame
		
		#-----botão de envio
		self.enviar = Button(self.frame, height= 2 , width = 15, text = 'Enviar', font = ('Helvetica', 12, 'bold'), bg='tomato', command = self.envia,cursor="hand2")
		self.enviar.grid(row=9, column = 2)
	
	#-------funções
	
		#envio das informações
	def envia(self):
		confirma = messagebox.askquestion("Confirmação de envio", "Tem certeza que deseja enviar o formulário?")
		if confirma == 'yes':
			tudo = self.preenchido()
			if tudo == True:
				if self.data == False:
					if hasattr(self,'notifica'):
						self.notifica.destroy()
					self.notifica= Label(self.frame, text="Data fora de alcance",fg= 'red', justify=CENTER,font=("Helvetica", 13, 'bold'))					#"Texto que se refere ao link
					self.notifica.grid(row = 2,column=1)
				else:
					dia = int(self.data[0:2])
					mes = int(self.data[3:5])
					ano = int(self.data[6:])
					if 	datetime.datetime(ano, mes, dia).strftime("%A") == "Thursday":
						if hasattr(self,'notifica'):
							self.notifica.destroy()
						self.notifica= Label(self.frame, text="Não é possível agendar horários de Quinta-feira",fg= 'red', justify=CENTER,font=("Helvetica", 10, 'bold'))	#"Texto que se refere ao link
						self.notifica.grid(row = 2,column=1)
					else:
						if self.combo2.get() == 'não':
							if hasattr(self,'notifica'):
								self.notifica.destroy()
							self.notifica= Label(self.frame, text="Não é possível agendar horários sem já ter a inicialização do setor. Contate alguém do FabLab Insper para mais informações",fg= 'red', justify=CENTER,font=("Helvetica", 9, 'bold'))					#"Texto que se refere ao link
							self.notifica.grid(rowspan = 2,columnspan=5, pady=10)
						else:
							setor=self.combo.get()
							hora= self.combo4.get()
							tempo=self.combo5.get()
							nome = self.dados.coletadados(self.usuario)[1]
							self.dados.addhorario(self.usuario,self.data, self.combo4.get(), nome,self.combo.get(), self.combo3.get(), self.combo5.get())
							for child in self.frame.winfo_children():
								child.destroy()
							self.sucesso = Label(self.frame, text = "Seu agendamento foi realizado com sucesso!", font = ("Helvetica", 15, 'bold'))
							self.sucesso.grid(row = 4, rowspan = 3, pady = 30)
							self.sucesso2 = Label(self.frame, text = "Dia: {}".format(self.data), font = ("Helvetica", 12, 'bold'))
							self.sucesso2.grid(row = 10)
							self.sucesso3 = Label(self.frame, text = "Setor: {}".format(setor), font = ("Helvetica", 12, 'bold'))
							self.sucesso3.grid(row = 11)
							self.sucesso4 = Label(self.frame, text = "Horário: {}".format(hora), font = ("Helvetica", 12, 'bold'))
							self.sucesso4.grid(row = 12)
							self.sucesso5 = Label(self.frame, text = "Tempo agendado: {}".format(tempo), font = ("Helvetica", 12, 'bold'))
							self.sucesso5.grid(row = 13)
			else:
				if hasattr(self,'notifica'):
					self.notifica.destroy()
				self.notifica= Label(self.frame, text="Preencha todos os campos",fg= 'red', justify=CENTER,font=("Helvetica", 15, 'bold'))			#"Texto que se refere ao link
				self.notifica.grid(row = 2,column=1)
		#-----verificação de preenchimento
	def preenchido(self):
		vazio=[]
		if self.escolha['text'] == "":
			vazio.append("data")
		if self.combo4.get() not in self.combo4['values'] or self.combo4.get() == 'Não há mais horários'or self.combo4.get() == '----Selecione----':
			vazio.append("combo4")
		if self.combo.get() not in self.combo['values'] or self.combo.get() == '----Selecione----':
			vazio.append("setor")
		if self.combo3.get() not in self.combo3['values']:
			vazio.append("pessoas")
		if self.combo5.get() not in self.combo5['values'] or self.combo5.get() == '----Selecione----':
			vazio.append("tempo")
		if self.combo2.get() not in self.combo2['values']:
			vazio.append("inicializacao")
		if len(vazio) == 0:
			return True
		else:
			return vazio
			
		#-----atualização do calendário
	def atualiza_calendario(self,x):
		hoje = datetime.datetime.today()
		a=hoje.strftime('%d/%m/%Y')
		if x < a:
			self.escolha['text'] = "Data fora de alcance"
			self.data= False

		else:
			self.escolha['text'] = x;
			self.data=x
		self.atualiza_data()
		

			#------atualização do setor escolhido
	def atualiza_setor(self, event):
		tempos= {'Fresadora': ['30 min','1h','1h30min','2h','2h30min', '3h'],'Impressora 3D':['30 min','1h','1h30min','2h','2h30min', '3h'],'Costura':['30 min','1h','1h30min','2h'],'Marcenaria':['30 min','1h','1h30min','2h','2h30min', '3h'],'Eletrônica':['30 min','1h','1h30min','2h']}
		V = ['----Selecione----']
		for x in tempos[self.combo.get()]:
			V.append(x)
		self.combo5['values'] = V
		self.combo5.current(0)	
		#------ atualização do horário de início escolhido
	def atualiza_inicio(self,event):
		comeca = list(self.horario_de_inicio())
		V= ['----Selecione----']
		for x in comeca:
			V.append(x)
		self.combo4['values'] = V
		self.combo4.current(0)
	
	 #------define as opções de horário de início a serem escolhidas
	def horario_de_inicio(self):
		
		self.horas = {'8:00': 800,'8:30': 850,'9:00':900,'9:30':950,'10:00':1000,'10:30':1050,'11:00':1100,'11:30':1150,'12:00':1200,'12:30':1250,'13:00':1300,'13:30':1350,'14:00':1400,'14:30':1450,'15:00':1500,'15:30':1550,'16:00':1600,'16:30':1650,'17:00': 1700,'17:30': 1750,'18:00':1800,'18:30':1850}
		self.horas_invertido = {'800':'8:00','850':'8:30','900':'9:00','950':'9:30','1000':'10:00','1050':'10:30','1100':'11:00','1150':'11:30','1200':'12:00','1250':'12:30','1300':'13:00','1350':'13:30','1400':'14:00','1450':'14:30','1500':'15:00','1550':'15:30','1600':'16:00','1650':'16:30','1700':'17:00','1750':'17:30','1800':'18:00','1850':'18:30'}
		self.intervalo = {'30 min':50,'1h':100,'1h30min':150,'2h':200,'2h30min':250, '3h':300}
		
		self.inicio = dict(self.horas)
		setor = self.combo.get()
		
		dia = self.data[0:2]
		mes = self.data[3:5]
		ano = self.data[6:]
		
		diadb = self.dados.dias()
		mesdb = self.dados.meses(dia)
		anodb = self.dados.anos(dia,mes)
		if dia in diadb:
			if mes in mesdb:
				if ano in anodb:
					horasdb = self.dados.horas(self.data)
					
					
					for hora in self.horas.keys():
						
						if hora in horasdb:
							setordb = self.dados.setor(self.data,hora)
							
							if setor in setordb:
								tempodb = self.dados.tempo(self.data,hora,setor)
								tempo = self.intervalo[tempodb]
								inicio = self.horas[hora]
								horarios = inicio + tempo
								while inicio < horarios:
									a = str(inicio)
									del self.inicio[self.horas_invertido[a]]
									inicio += 50
							
							else:
								continue
						
						else:
							continue
		
		
		self.fim = dict(self.inicio)
		for hora2 in self.fim.keys():
			tempo = self.intervalo[self.combo5.get()]
			comecou = self.horas[hora2]
			fim = comecou + tempo
			if fim <= 1900:
				while comecou < fim and len(self.inicio)>0:
					b=str(comecou)
					try:
						tem = self.inicio[self.horas_invertido[b]]
					except:
						del self.inicio[hora2]
						break
					comecou += 50
				
					
			else:
				del self.inicio[hora2]
		if len(self.inicio) == 0:
			self.inicio['Não há mais horários'] = 'cheio'
		
				
		return self.inicio
	#-----atualizção de data
	def atualiza_data(self):
		self.combo.current(0)
		
							
		
	
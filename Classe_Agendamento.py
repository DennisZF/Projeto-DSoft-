from tkinter import *
import tkinter.ttk as ttk

class Agendamento:
	def __init__(self,frame):
		titulo=Label(frame, text="Agendamento", height=1, font=("Helvetica", 20, 'bold'))
		titulo.grid(row=1, column=0)        #título
		
		from Classe_Calendar2 import Calendar2
		
		calendario = Calendar2(frame)  #calendário para escolha de datas
		calendario.grid(row=1, column=1)
		
		self.escolha = Label(frame, text=" Selecione uma data ",font=("Helvetica", 8, 'bold'))    #instrução
		self.escolha.grid(row=0, column=1)
		selecao = calendario.quando_selecionada(self.atualiza)		#pega a seleção e guarda numa variável
		
		self.escolha2= Label(frame, text=" Selecione um setor do FabLab ", font=("Helvetica",8, 'bold'))
		self.escolha2.grid(row=0, column=2)     #instrução
		self.combo=ttk.Combobox(frame)
		self.combo.grid(row=1, column=2)  #combobox de seleção
		self.combo['values']=('Fresadora','Impressora 3D','Costura','Marcenaria','Eletrônica')
		self.combo.current(0) #default é o primeiro termo

		self.escolha3= Label(frame, text=" Você sabe utilizar esse setor sozinho? ", font=("Helvetica", 8, 'bold'))   #pergunta
		self.escolha3.grid(row=0, column=3)
		self.combo2=ttk.Combobox(frame)    #combobox de seleção
		self.combo2.grid(row=1, column=3)
		self.combo2['values']=('sim','não')
		self.combo2.current(1) #default é o segundo termo

		self.escolha4= Label(frame, text=" Selecione o número de pessoas ", font=("Helvetica", 8, 'bold'))     #instrução
		self.escolha4.grid(row=0, column=4)
		self.combo3=ttk.Combobox(frame)       #combobox de seleção
		self.combo3.grid(row=1, column=4)
		self.combo3['values']=('1','2','3','4','5','6')
		self.combo3.current(0) #default é o primeiro termo
		
		self.escolha5= Label(frame, text=" Selecione uma faixa de horário ", font=("Helvetica",8, 'bold'))     #instrução
		self.escolha5.grid(row=0, column=5)
		self.combo4=ttk.Combobox(frame)       #combobox de seleção
		self.combo4.grid(row=1, column=5)
		self.combo4['values']=('8:00-8:30','8:30-9:00','9:00-9:30','9:30-10:00','10:00-10:30','10:30-11:00','11:00-11:30','11:30-12:00','12:00-12:30','12:30-13:00','14:00-14:30','14:30-15:00','15:00-15:30','15:30-16:00','16:00-16:30','16:30-17:00','17:00-17:30','17:30-18:00','18:00-18:30','18:30-19:00')
		self.combo4.current(0) #default é o primeiro termo
		
		
		
		
	
	def atualiza(self,x):
		self.escolha['text'] = x;
		
import datetime
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import calendar

class Calendario:
	def __init__(self, frame,dados, menu):
		self.frame = frame 
		self.dados= dados
		self.menu = menu
		
		from Classe_Calendar2 import Calendar2
		#----título da página
		titulo = Label(frame, text="Calendário", height=1 ,font=("Helvetica", 30, 'bold'))
		titulo.pack(side= TOP, pady=25)
		
		#-------instrução
		data = Label(frame, text="Escolha a data que deseja visualizar", height=1 ,font=("Helvetica", 13, 'bold'))
		data.pack(side = TOP)
		
		self.escolha = Label(frame, text=["Selecione uma data"], font=("Helvetica", 11, 'bold'))
		self.escolha.pack(side = TOP, pady= 15)
		
		#------- calendário e sua geometrização
		calendario = Calendar2(frame)
		calendario.pack(side = TOP)
		
		
		calendario.quando_selecionada(self.atualiza)
		
		
	#------função de atualização 
	def atualiza(self,x):
		self.escolha['text'] = x;
		from Classe_Horarios import Horarios
		if hasattr(self, 'horarios'):
			self.horarios.novadata(self,x, self.dados, self.menu)
		else:
			from Classe_Horarios import Horarios
			self.horarios = Horarios()
			self.horarios.selecionado(self,x, self.dados, self.menu)
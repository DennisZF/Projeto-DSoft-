import datetime
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import calendar

class Calendario:
	def __init__(self, frame,dados):
		self.frame = frame 
		self.dados= dados
		
		from Classe_Calendar2 import Calendar2
	
		titulo = Label(frame, text="Calendário", height=1 ,font=("Helvetica", 25, 'bold'))
		titulo.pack(side= TOP)
		
		data = Label(frame, text="Escolha a data que deseja visualizar", height=1 ,font=("Helvetica", 13, 'bold'))
		data.pack(side = TOP)
		
		calendario = Calendar2(frame)
		calendario.pack(side = LEFT, padx= 70, pady = 80)
		
		self.escolha = Label(frame, text=["Selecione uma data"])
		self.escolha.pack(side = RIGHT)
		
		calendario.quando_selecionada(self.atualiza)
		
		
	
	def atualiza(self,x):
		self.escolha['text'] = x;
		from Classe_Horarios import Horarios
		if hasattr(self, 'horarios'):
			self.horarios.novadata(self,x)
		else:
			from Classe_Horarios import Horarios
			self.horarios = Horarios()
			self.horarios.selecionado(self,x)
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import datetime

class Historico:
	def __init__(self,frame, dados, usuario):
		self.usuario = usuario
		self.dados = dados
		titulo=Label(frame, text="Histórico", height=1, font=("Helvetica", 30, 'bold'))
		titulo.grid(rowspan=1, columnspan = 6, pady = 15)       #título

		self.tree = ttk.Treeview(columns=('Setor', 'Quantidade de pessoas', 'Tempo agendado'))
		self.tree.heading('#0', text='Data')
		self.tree.heading('#1', text='Setor')
		self.tree.heading('#2', text='Quantidade de pessoas')
		self.tree.heading('#3', text='Tempo agendado')
		self.tree.grid(column=4, row=4, sticky='nsew', in_= frame)
		frame.grid_columnconfigure(0, weight=1)
		frame.grid_rowconfigure(0, weight=1)
		
		for data in self.dados.historia.keys():
			for hora in self.dados.historia[data].keys():
					for setor in self.dados.historia[data][hora].keys():
						self.tree.insert('','end', text = data, values = (setor, self.dados.horarios[data][hora][setor]["numero de pessoas"], self.dados.horarios[data][hora][setor]["tempo"]))

		self.tree.column('Setor', anchor = CENTER)
		self.tree.column('Quantidade de pessoas', anchor = CENTER)
		self.tree.column('Tempo agendado', anchor = CENTER)

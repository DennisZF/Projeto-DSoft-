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

		self.tree = ttk.Treeview(columns=('Data','Setor', 'Quantidade de pessoas', 'Tempo agendado', 'Status'), show='headings')
		self.tree.heading('#1', text='Data')
		self.tree.heading('#2', text='Setor')
		self.tree.heading('#3', text='Quantidade de pessoas')
		self.tree.heading('#4', text='Tempo agendado')
		self.tree.heading('#5', text='Status')
		self.tree.grid(column=4, row=4, sticky='nsew', in_= frame)
		frame.grid_columnconfigure(0, weight=1)
		frame.grid_rowconfigure(0, weight=1)
		
		self.datas = {}
		for data in self.dados.historia.keys():
			for hora in self.dados.historia[data].keys():
					for setor in self.dados.historia[data][hora].keys():
						self.tree.insert('','end', values = (data, setor, self.dados.historia[data][hora][setor]["numero de pessoas"], self.dados.historia[data][hora][setor]["tempo"],self.dados.historia[data][hora][setor]["status"]))
						dia = int(data[0:2])
						mes = int(data[3:5])
						ano = int(data[6:])
						data_final = dia+(mes*100)+(ano*1000000)
						self.datas[data] = data_final
						
		self.tree.column('Data', anchor = CENTER)
		self.tree.column('Setor', anchor = CENTER)
		self.tree.column('Quantidade de pessoas', anchor = CENTER)
		self.tree.column('Tempo agendado', anchor = CENTER)
		self.tree.column('Status', anchor = CENTER)
		self.ordem()
		
	def ordem(self):
		l = [(self.tree.set(k, 'Data'), k) for k in self.tree.get_children('')]
		
		l.sort(key=lambda t: int(self.datas[t[0]]))

		for index, (val, k) in enumerate(l):
			self.tree.move(k, '', index)
		

from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import datetime

class Horarios:
	def selecionado(self,item,data, dados, menu):
		self.dados = dados
		dia = int(data[0:2])
		mes = int(data[3:5])
		ano = int(data[6:])

		self.tree = ttk.Treeview(columns=('Setor', 'Nome', 'Quantidade de pessoas', 'Tempo agendado'))
		self.tree.heading('#0', text='Horário')
		self.tree.heading('#1', text='Setor')
		self.tree.heading('#2', text='Nome')
		self.tree.heading('#3', text='Quantidade de pessoas')
		self.tree.heading('#4', text='Tempo agendado')
		self.tree.grid(column=0, row=0, sticky='nsew', in_=menu)
		menu.grid_columnconfigure(0, weight=1)
		menu.grid_rowconfigure(0, weight=1)
		
		if 	datetime.datetime(ano, mes, dia).strftime("%A") == "Thursday":
			self.tree.insert('', 'end', text = "   Não é possível", values =("fazer agendamentos", "de Quinta-feira"),tag='monospace')
			self.tree.tag_configure('monospace', font='courier')

		else:
			if data in self.dados.horarios.keys():
				for hora in self.dados.horarios[data]:
						for setor in self.dados.horarios[data][hora]:
							self.tree.insert('', 'end', text=hora, values=(setor, self.dados.horarios[data][hora][setor]["nome"], self.dados.horarios[data][hora][setor]["numero de pessoas"], self.dados.horarios[data][hora][setor]["tempo"]))

	def novadata(self,item,data, dados, menu):
		self.tree.destroy()
		self.selecionado(item,data, dados, menu)

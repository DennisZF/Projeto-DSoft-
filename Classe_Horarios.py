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

		self.tree = ttk.Treeview(columns=('Horário','Setor', 'Nome', 'Quantidade de pessoas', 'Tempo agendado'), show = 'headings')
		self.tree.heading('#1', text='Horário')
		self.tree.heading('#2', text='Setor')
		self.tree.heading('#3', text='Nome')
		self.tree.heading('#4', text='Quantidade de pessoas')
		self.tree.heading('#5', text='Tempo agendado')
		self.tree.grid(column=0, row=0, sticky='nsew', in_=menu)
		menu.grid_columnconfigure(0, weight=1)
		menu.grid_rowconfigure(0, weight=1)
		
		if 	datetime.datetime(ano, mes, dia).strftime("%A") == "Thursday":
			self.tree.insert('', 'end', values =("   Não é possível","fazer agendamentos", "no dia aberto"),tag='monospace')
			self.tree.tag_configure('monospace', font='courier')

		else:
			if data in self.dados.horarios.keys():
				for hora in self.dados.horarios[data]:
						for setor in self.dados.horarios[data][hora]:
							self.tree.insert('', 'end', values=(hora,setor, self.dados.horarios[data][hora][setor]["nome"], self.dados.horarios[data][hora][setor]["numero de pessoas"], self.dados.horarios[data][hora][setor]["tempo"]))
			self.ordem()
	def novadata(self,item,data, dados, menu):
		self.tree.destroy()
		self.selecionado(item,data, dados, menu)

	def ordem(self):
		l = [(self.tree.set(k, 'Horário'), k) for k in self.tree.get_children('')]
		l.sort(key=lambda t: int(self.dados.horas[t[0]]))

		for index, (val, k) in enumerate(l):
			self.tree.move(k, '', index)
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

class Horarios:
	def selecionado(self,item,data, dados, menu):
		#self.horarios = Listbox(item.frame)
		#self.horarios.pack(side= RIGHT, padx=70)
		#print(item.dados.horarios)
		#for a in item.dados.horarios[data]:
	#		self.horarios.insert(END,a)
		self.dados = dados
		self.tree = ttk.Treeview(columns=('Máquina', 'Nome', 'Quantidade de pessoas', 'Tempo'))
		self.tree.heading('#0', text='Horário')
		self.tree.heading('#1', text='Máquina')
		self.tree.heading('#2', text='Nome')
		self.tree.heading('#3', text='Quantidade de pessoas')
		self.tree.heading('#4', text='Tempo')
		self.tree.grid(column=0, row=0, sticky='nsew', in_=menu)
		
		
		#menu.grid_columnconfigure(0, weight=1)
		#menu.grid_rowconfigure(0, weight=1)
		if data in self.dados.horarios.keys():
			for i in range(len(self.dados.horarios[data])):
				for hora in self.dados.horarios[data][i]:
						for z in range(len(self.dados.horarios[data][i][hora])):
							self.tree.insert('', 'end', text=hora, values=(self.dados.horarios[data][i][hora][z]["setor"], self.dados.horarios[data][i][hora][z]["nome"], self.dados.horarios[data][i][hora][z]["numero de pessoas"], self.dados.horarios[data][i][hora][z]["tempo"]))

	def novadata(self,item,data, dados, menu):
		self.tree.destroy()
		self.selecionado(item,data, dados, menu)

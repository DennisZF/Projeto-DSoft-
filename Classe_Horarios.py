from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk

class Horarios:
	def selecionado(self,item,data):
		self.horarios = Listbox(item.frame)
		self.horarios.pack(side= RIGHT, padx=70)
		print(item.dados.horarios)
		for a in item.dados.horarios[data]:
			self.horarios.insert(END,a)
	def novadata(self,item,data):
		self.horarios.destroy()
		self.selecionado(item,data)
#		segundaframe = ttk.Frame()
#		self.tree = ttk.Treeview(columns=["Horário", "Máquina", "Nome", "Quantidade dde pessoas"], show="headings")
#		vsb = ttk.Scrollbar(orient="vertical",command=self.tree.yview)
#		hsb = ttk.Scrollbar(orient="horizontal",command=self.tree.xview)
#		self.tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
#		self.tree.grid(column=0, row=0, sticky='nsew', in_=segundaframe)
#		vsb.grid(column=1, row=0, sticky='ns', in_=segundaframe)
#		hsb.grid(column=0, row=1, sticky='ew', in_=segundaframe)
#		
#		item.frame.grid_columnconfigure(0, weight=1)
#		item.frame.grid_rowconfigure(0, weight=1)
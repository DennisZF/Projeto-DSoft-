from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import datetime

class Horarios:
	def selecionado(self,item,data, dados, menu):
		self.dados = dados
		dia = data[0:2]
		mes = data[3:5]
		ano = data[6:]
		self.horas={'8:00': 800,'8:30': 850,'9:00':900,'9:30':950,'10:00':1000,'10:30':1050,'11:00':1100,'11:30':1150,'12:00':1200,'12:30':1250,'13:00':1300,'13:30':1350,'14:00':1400,'14:30':1450,'15:00':1500,'15:30':1550,'16:00':1600,'16:30':1650,'17:00': 1700,'17:30': 1750,'18:00':1800,'18:30':1850}
	
		#--------corpo da guia
		self.tree = ttk.Treeview(columns=('Horário','Setor', 'Nome', 'Quantidade de pessoas', 'Tempo agendado'), show = 'headings')
		self.tree.heading('#1', text='Horário')
		self.tree.heading('#2', text='Setor')
		self.tree.heading('#3', text='Nome')
		self.tree.heading('#4', text='Quantidade de pessoas')
		self.tree.heading('#5', text='Tempo agendado')
		self.tree.grid(column=0, row=0, sticky='nsew', in_=menu)
		menu.grid_columnconfigure(0, weight=1)
		menu.grid_rowconfigure(0, weight=1)
		 #---------bloqueia dia livre
		if 	datetime.datetime(int(ano), int(mes), int(dia)).strftime("%A") == "Thursday":
			self.tree.insert('', 'end', values =("   Não é possível","fazer agendamentos", "no dia aberto"),tag='monospace')
			self.tree.tag_configure('monospace', font='courier')
		
		#-------obtenção de valores
		else:
			diadb = self.dados.dias()
			mesdb = self.dados.meses(dia)
			anodb = self.dados.anos(dia,mes)
			if dia in diadb:
				if mes in mesdb:
					if ano in anodb:
						horasdb = self.dados.horas(data)
						
						
						for hora in self.horas.keys():
							
							if hora in horasdb:
								setordb = self.dados.setor(data,hora)
								
								for setor in setordb:
									val = self.dados.valores(data,hora,setor)
									self.tree.insert('', 'end', values=(hora,setor, val[0], val[1], val[2]))
			self.ordem()
		#-----atualizador
	def novadata(self,item,data, dados, menu):
		self.tree.destroy()
		self.selecionado(item,data, dados, menu)

	def ordem(self):
		l = [(self.tree.set(k, 'Horário'), k) for k in self.tree.get_children('')]
		l.sort(key=lambda t: int(self.horas[t[0]]))

		for index, (val, k) in enumerate(l):
			self.tree.move(k, '', index)
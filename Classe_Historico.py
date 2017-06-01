from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import datetime

class Historico:
	def __init__(self,frame, dados, usuario):
		self.usuario = usuario
		self.dados = dados
		self.horas={'8:00': 800,'8:30': 850,'9:00':900,'9:30':950,'10:00':1000,'10:30':1050,'11:00':1100,'11:30':1150,'12:00':1200,'12:30':1250,'13:00':1300,'13:30':1350,'14:00':1400,'14:30':1450,'15:00':1500,'15:30':1550,'16:00':1600,'16:30':1650,'17:00': 1700,'17:30': 1750,'18:00':1800,'18:30':1850}
	
		
		
		
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
		
		diadb = self.dados.dias2()
		
		for dia in diadb:
			mesdb = self.dados.meses2(dia)
			for mes in mesdb:
				anodb = self.dados.anos2(dia,mes)
				for ano in anodb:
					data = "{}/{}/{}".format(dia,mes,ano)
					for hora in self.dados.horas2(data):
						for setor in self.dados.setor2(data,hora):
							val = self.dados.valores2(data,hora,setor)
							self.tree.insert('','end', values = (data, setor, val[0], val[1],val[2]))
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
		

from tkinter import *
import tkinter.font as tkFont
import tkinter as ttk
from PIL import ImageTk, Image

class Instrucoes:
	def __init__(self, frame, dados, menu):
		self.frame=frame
		self.dados=dados

		titulo=Label(frame, text="Instruções", height=1, font=("Helvetica", 25, "bold"))
		titulo.pack(side=TOP)

		#Frame das instruções:

		#Botões:
		self.impressora3d=Button(menu, text="Impressora 3D",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'), command=self.impressora3d ).pack(side=TOP)
		self.marcenaria=Button(menu, text="Marcenaria",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'), command=self.marcenaria).pack(side=TOP)
		self.vinil=Button(menu, text="Vinil",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),  command=self.vinil).pack(side=TOP)
		self.costura=Button(menu, text="Costura",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),command=self.costura).pack(side=TOP)
		self.impressoralaser=Button(menu, text="Impressora Laser",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),command=self.laser).pack(side=TOP)
		self.milena=Button(menu, text="MILENA",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),command=self.milena).pack(side=TOP)
		self.fresadora=Button(menu, text="Fresadora",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),command=self.fresadora).pack(side=TOP)
		
	
	def vinil(self):
		photo=PhotoImage(file="Vinil.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)

	def impressora3d(self):
		photo=PhotoImage(file="Setor Complexo.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)

	def marcenaria(self):
		photo=PhotoImage(file="Setor Complexo.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)
	

	def fresadora(self):
		photo=PhotoImage(file="Fresadora.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)
		

	def laser(self):
		photo=PhotoImage(file="Laser.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)
		

	def costura(self):
		photo=PhotoImage(file="Setor Complexo.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(fill=BOTH, expand=2)
	 

	def milena(self):
		photo=PhotoImage(file="Vinil.PNG")
		img=Label(image=photo)
		img.image=photo
		img.pack(side=RIGHT)
	
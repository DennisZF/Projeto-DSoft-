from tkinter import *
import tkinter.font as tkFont
import tkinter as ttk
from PIL import ImageTk, Image

class Instrucoes:
	def __init__(self, frame, menu):
		self.frame=frame
		#---------título da página
		titulo=Label(frame, text="Instruções", height=1, font=("Helvetica", 25, "bold"))
		titulo.pack(side=TOP)

		#----------Frame das instruções:

		#----------Botões que abrem as guias de seu respectivo setor:
		self.impressora3d=Button(menu, text="Impressora 3D",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'), command=self.impressora3d ).pack(side=TOP)
		self.marcenaria=Button(menu, text="Marcenaria",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'), command=self.marcenaria).pack(side=TOP)
		self.vinil=Button(menu, text="Vinil",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'),  command=self.vinil).pack(side=TOP)
		self.costura=Button(menu, text="Costura",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'),command=self.costura).pack(side=TOP)
		self.impressoralaser=Button(menu, text="Impressora Laser",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'),command=self.laser).pack(side=TOP)
		self.milena=Button(menu, text="MILENA",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'),command=self.milena).pack(side=TOP)
		self.fresadora=Button(menu, text="Fresadora",height = 1,width = 25,bg= 'Maroon', fg='white', font =("Helvetica", 10, 'bold'),command=self.fresadora).pack(side=TOP)
	
	#-------setor vinil
	def vinil(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Vinil.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)
	
	#--------setor impressora
	def impressora3d(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Setor Complexo.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)

	#---------setor marcenaria
	def marcenaria(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Setor Complexo.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)
	
	#-------setor fresadora
	def fresadora(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Fresadora.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)
		
	#--------setor laser
	def laser(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Laser.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)
		
	#-------setor costura
	def costura(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Setor Complexo.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(fill=BOTH, expand=2)
	 
	#----------setor fresadora de precisão
	def milena(self):
		if hasattr(self, "img"):
			self.img.destroy()
		photo=PhotoImage(file="Vinil.PNG")
		self.img=Label(self.frame, image=photo)
		self.img.image=photo
		self.img.pack(side=RIGHT)
	
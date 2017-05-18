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
		self.impressora3d=Button(menu, text="Impressora 3D",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold') ).pack(side=TOP)
		self.marcenria=Button(menu, text="Marcenaria",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold')).pack(side=TOP)
		self.vinil=Button(menu, text="Vinil",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold'),  command=self.vinil).pack(side=TOP)
		self.costura=Button(menu, text="Costura",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold')).pack(side=TOP)
		self.impressoralaser=Button(menu, text="Impressora Laser",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold')).pack(side=TOP)
		self.milena=Button(menu, text="MILENA",height = 1,width = 25,bg= 'Maroon', fg='Black', font =("Helvetica", 10, 'bold')).pack(side=TOP)

		self.imagem = Label(self.frame, image=none)
	
	def vinil(self):
		img=ImageTk.PhotoImage(Image.open('Vinil.JPG'))
		self.imagem['image']= img

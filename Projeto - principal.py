#Projeto Design de Software -- Sistema de Agendamento de Horário para o FabLab
#------------importações
from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from Classe_login import Login
from Classe_Fire2 import Fire
#--------variável chama firebase
D= Fire()
#----------login com firebase
abre=Login(D)
#----------loop
mainloop()
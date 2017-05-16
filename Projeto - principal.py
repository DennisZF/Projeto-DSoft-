#Projeto Design de Software -- Sistema de Agendamento de Horário para o FabLab

from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from Classe_login import Login
from Classe_Database import Database

D= Database()
abre=Login(D)
mainloop()
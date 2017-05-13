#Projeto Design de Software -- Sistema de Agendamento de Horário para o FabLab

from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
from Classe_login import Login
from Classe_Cadastro import Cadastro
from Classe_Menu_principal import Menu_principal
from Classe_Sair import Sair
from Classe_Database import Database
from Classe_Calendario import Calendario

D= Database()
abre=Login(D)
mainloop()
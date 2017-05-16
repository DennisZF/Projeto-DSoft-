from tkinter import *
class Database:
	def __init__(self):
	#Seria melhor se houvesse um dicionario com esses dados online
		self.usuarios = {}
		self.dados = {}
		self.horarios = {"16/05/2017":["00:00 - oi", "21:00 - tchau"],"18/05/2017":["00:00 - oi", "21:00 - tchau"]}
	def addusuario(self, usuario, senha, nome, semestre, matricula, email):
		self.usuarios[usuario] = senha
		self.dados[usuario] = [senha, nome, semestre, matricula, email]
	def verificacao(self,usuario,senha):
		if usuario in self.usuarios.keys():
			if self.usuarios[usuario]==senha:
				return True
		else:
			return False
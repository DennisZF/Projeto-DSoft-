from tkinter import *
class Database:
	def __init__(self):
	#Seria melhor se houvesse um dicionario com esses dados online
		self.usuarios = {}
		self.dados = {}
		self.horarios = {"16/05/2017":[{"08:00": [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo": 2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo": 3} ]}, {"15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo": 1} ]}],"18/05/2017":[{"08:00": [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3,"tempo":4},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}, {"15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}]}
	def addusuario(self, usuario, senha, nome, semestre, matricula, email):
		self.usuarios[usuario] = senha
		self.dados[usuario] = [senha, nome, semestre, matricula, email]
	def verificacao(self,usuario,senha):
		if usuario in self.usuarios.keys():
			if self.usuarios[usuario]==senha:
				return True
		else:
			return False
			
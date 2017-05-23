from tkinter import *
class Database:
	def __init__(self):
	#Seria melhor se houvesse um dicionario com esses dados online
		self.usuarios = {}
		self.dados = {}
		self.horarios = {} #16/05/2017":{"08:00": {"fresadora":{"nome":"joao"  , "numero de pessoas":3, "tempo": 2},"3d":{"nome":"maria"  , "numero de pessoas":1, "tempo": 3}}}} #], "15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo": 1} ]},"18/05/2017":[{"08:00": [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3,"tempo":4},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}, {"15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}]}
		self.historia = {}

	def addusuario(self, usuario, senha, nome, curso, semestre, matricula, email):
		self.usuarios[usuario] = senha
		self.dados[usuario] = [senha, nome, curso, semestre, matricula, email]
	def verificacao(self,usuario,senha):
		if usuario in self.usuarios.keys():
			if self.usuarios[usuario]==senha:
				return True
		else:
			return False
	def deletausuario(self, usuario):
		if usuario in self.usuarios.keys():
			del self.dados[usuario]
			del self.usuarios[usuario]
	def addhorario(self,data,hora, nome, setor, pessoas, tempo):
		if data not in self.horarios.keys():
			self.horarios[data]={}
		if hora not in self.horarios[data].keys():
			self.horarios[data][hora]={}
		if setor not in self.horarios[data][hora].keys():
			self.horarios[data][hora][setor] = {}
		
		self.horarios[data][hora][setor]["nome"]= nome
		self.horarios[data][hora][setor]["numero de pessoas"]= pessoas
		self.horarios[data][hora][setor]["tempo"]= tempo
		
		self.historia[data] = self.horarios[data]


	def cancelahorario(self,data,hora, setor):
		del self.horarios[data][hora][setor]


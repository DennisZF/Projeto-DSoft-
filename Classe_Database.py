from tkinter import *
class Database:
	def __init__(self):
	#Seria melhor se houvesse um dicionario com esses dados online
		self.usuarios = {}
		self.dados = {}
		self.horarios = {} #16/05/2017":{"08:00": {"fresadora":{"nome":"joao"  , "numero de pessoas":3, "tempo": 2},"3d":{"nome":"maria"  , "numero de pessoas":1, "tempo": 3}}}} #], "15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo": 1} ]},"18/05/2017":[{"08:00": [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3,"tempo":4},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}, {"15:00" : [{"nome":"joao" , "setor": "fresadora" , "numero de pessoas":3, "tempo":2},{"nome":"maria" , "setor": "3d" , "numero de pessoas":1, "tempo":2} ]}]}
		self.historia = {}
		self.horas = {'8:00': 800,'8:30': 850,'9:00':900,'9:30':950,'10:00':1000,'10:30':1050,'11:00':1100,'11:30':1150,'12:00':1200,'12:30':1250,'13:00':1300,'13:30':1350,'14:00':1400,'14:30':1450,'15:00':1500,'15:30':1550,'16:00':1600,'16:30':1650,'17:00': 1700,'17:30': 1750,'18:00':1800,'18:30':1850}
		self.horas_invertido = {'800':'8:00','850':'8:30','900':'9:00','950':'9:30','1000':'10:00','1050':'10:30','1100':'11:00','1150':'11:30','1200':'12:00','1250':'12:30','1300':'13:00','1350':'13:30','1400':'14:00','1450':'14:30','1500':'15:00','1550':'15:30','1600':'16:00','1650':'16:30','1700':'17:00','1750':'17:30','1800':'18:00','1850':'18:30'}

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
		for dic in [self.horarios, self.historia]:
			if data not in dic.keys():
				dic[data]={}
			if hora not in dic[data].keys():
				dic[data][hora]={}
			if setor not in dic[data][hora].keys():
				dic[data][hora][setor] = {}
		
			dic[data][hora][setor]["nome"]= nome
			dic[data][hora][setor]["numero de pessoas"]= pessoas
			dic[data][hora][setor]["tempo"]= tempo
		self.historia[data][hora][setor]["status"] = 'Agendado'
			
	


	def cancelahorario(self,data,hora, setor):
		del self.horarios[data][hora][setor]
		self.historia[data][hora][setor]["status"] = 'CANCELADO'


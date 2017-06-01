import pyrebase

class Fire:
	def __init__(self):

		config = {
					"apiKey": "apiKey",
					"authDomain": "projeto-dsoft-final.firebaseapp.com",
					"databaseURL": "https://projeto-dsoft-final.firebaseio.com",
					"storageBucket": "projeto-dsoft-final.appspot.com"
				}

		self.firebase = pyrebase.initialize_app(config)

		self.db = self.firebase.database()
		
		
		
	def usuarioexistente(self,usuario, senha,nome,curso, semestre, matricula, email):
		existentes = self.db.child("usuarios").get()
		ja= existentes.val()
		if usuario not in ja:
			self.addusuario(usuario, senha,nome,curso, semestre, matricula, email)
			return True
		else:
			return False
	def addusuario(self,usuario, senha,nome,curso, semestre, matricula, email):
		dados = {	
					"/usuarios/"+usuario: {
						"senha":senha,
						"nome":nome,
						"curso":curso,
						"semestre":semestre,
						"matricula":matricula,
						"email": email
					}
				}
		self.db.update(dados)
	def verificacao(self,usuario,senha):
		existentes = self.db.child("usuarios").get()
		ja= existentes.val()
		if usuario in ja:
			if ja[usuario]["senha"]==senha:
				return True
				
	def deletaconta(self,usuario):
		self.db.child("usuarios").child(usuario).remove()
	def coletadados(self,usuario):
		existentes = self.db.child("usuarios").get()
		ja= existentes.val()
		D = []
		for x in ["senha","nome","curso","semestre","matricula","email"]:
			D.append(ja[usuario][x])
		return D
	def attusuario(self,usuario,nome,curso, semestre, matricula, email):
		self.db.child("usuarios").child(usuario).update({'curso':curso})
		self.db.child("usuarios").child(usuario).update({'nome':nome})
		self.db.child("usuarios").child(usuario).update({'semestre':semestre})
		self.db.child("usuarios").child(usuario).update({'matricula':matricula})
		self.db.child("usuarios").child(usuario).update({'email':email})
		
	def muda_senha(self,usuario,senha):
		self.db.child("usuarios").child(usuario).update({'senha':senha})
		
	def addhorario(self,data,hora, nome, setor, pessoas, tempo):
		agenda = {
					"{}/".format(data)+hora:{
										setor:{
												"nome":nome,
												"numero de pessoas":pessoas,
												"tempo":tempo,
												"status":"Agendado"
											}
									}
				}
		self.db.child("horarios").update(agenda)
		
	def horas(self,data):
		existentes = self.db.child("horarios").child(data).get()
		ja= existentes.val()
		return ja
		
	def setor(self,data, hora):
		existentes = self.db.child("horarios").child(data).child(hora).get()
		ja= existentes.val()
		return ja
	def tempo(self,data,hora,setor)	:
		existentes = self.db.child("horarios").child(data).child(hora).child(setor).get()
		ja= existentes.val()
		t = ja["tempo"]
		return t
		
	def dias(self):
		existentes = self.db.child("horarios").get()
		ja= existentes.val()
		return ja
	def meses(self,dia):
		existentes = self.db.child("horarios").child(dia).get()
		ja= existentes.val()
		return ja
	def anos(self,dia,mes):
		existentes = self.db.child("horarios").child(dia).child(mes).get()
		ja= existentes.val()
		return ja		
	def valores(self,data,hora,setor):
		existentes = self.db.child("horarios").child(data).child(hora).get()
		ja= existentes.val()
		D = []
		for x in ["nome","numero de pessoas","tempo","status"]:
			D.append(ja[setor][x])
		return D
		
	def verificanome(self,usuario,data,hora,setor):
		existentes = self.db.child("horarios").child(data).child(hora).child(setor).get()
		ja= existentes.val()
		if self.coletadados(usuario)[1] == ja["nome"]:
			return True
		else:
			return False
		
	def cancelahorario(self,data,hora,setor):
		self.db.child("horarios").child(data).child(hora).child(setor).remove()
		
										
		
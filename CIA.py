import random
class Client:
	def __init__(self, name):
		self.name = name
		self.Connection_serveur_client = False
		self.virement = False
		self.depot_cheque= False
		self.rdv_planing = False
		self.appel_tel = False
		self.emprunt=False
		self.Connection_serveur_admin=False
		self.Financial_planning=False
		self.Approuve_Pret=False
		self.Connection_serveur_employee=False
		self.Commit_cheque=False
class Employee:
	def __init__(self, name):
		self.name=name
		self.Connection_serveur_client = False
		self.virement = False
		self.depot_cheque= False
		self.rdv_planing = False
		self.appel_tel = False
		self.emprunt=False
		self.Connection_serveur_admin=False
		self.Financial_planning=False
		self.Approuve_Pret=False
		self.Connection_serveur_employee=False
		self.Commit_cheque=False
class Admin:
	def __init__(self, name):
	    	self.name=name
	    	self.Connection_serveur_client = False
	    	self.virement = False
	    	self.depot_cheque= False
	    	self.rdv_planing = False
	    	self.appel_tel = False
	    	self.emprunt=False
	    	self.Connection_serveur_admin=False
	    	self.Financial_planning=False
	    	self.Approuve_Pret=False
	    	self.Connection_serveur_employee=False
	    	self.Commit_cheque=False
# Create Character
char1 = Client("Client1")
char2 = Employee("Conseillers_financiers")
char3 = Employee("Secrétaires")
char4 = Admin("IT Support")
char5 = Employee("Directeur")

# Set the bool_var variable for each character
char2.Approuve_Pret=False
char2.Commit_cheque=False
char3.Financial_planning=False
char3.Approuve_Pret=False
char3.Commit_cheque=False
char5.Financial_planning=False


if __name__ == '__main__':
	while True:
		#IF admin don't connect everyone can't do a thing
		char4.Connection_serveur_admin=random.choice([True,False])
		if(char4.Connection_serveur_admin !=True):
			print("Server isn't online \n")
		else: #char4.Connection_serveur_admin =True
			print("Server start by Admin All operation is permitted\n")
			char1.Connection_serveur_client=random.choice([True,False])
			if(char1.Connection_serveur_client !=True):
				pass
			else:#char1.Connection_serveur_client=True
				print("Client is connected\n")
			char1.virement=random.choice([True,False])
			if(char1.virement !=True):
				pass
			else: #char1.virement=True
				print("Client demanded vivement\n")
				char5.Approuve_Pret=random.choice([True,False])
				if(char5.Approuve_Pret!=True):
					pass
				else:#char5.Approuve_Pret=True
					print("Director appouve the cheque \n")

import random
class Client:
	def __init__(self, name):
		self.name = name
		self.Connection_serveur_client = False
		self.virement = False
		self.depot_cheque= False
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
char4 = Admin("IT Support")
char5 = Employee("Directeur")

quit=0
listx=[0,0,0,0,0,0,0,0] 
#admin_connect,server_status,client_connect,demand_vivement,depot_cheque,employee_connect,vivement_approuved,cheque_approuved


if __name__ == '__main__':
	while (quit==0):
		#IF admin don't connect everyone can't do a thing
		char4.Connection_serveur_admin=random.choice([True,False])
		if(char4.Connection_serveur_admin !=True):
			print("Server isn't online \n")
			quit=1
			print(listx)
		else: #char4.Connection_serveur_admin =True
			listx[0]=1
			print("Server start by Admin All operation is permitted\n")
			char1.Connection_serveur_client=random.choice([True,False])
			if(char1.Connection_serveur_client !=True):
				pass
			else:#char1.Connection_serveur_client=True
				listx[2]=1
				print("Client is connected\n")
				char1.depot_cheque=random.choice([True,False])
				if(char1.depot_cheque !=True):
					pass
				else: #char1.depot_cheque=True
					listx[4]=1
					print("Client demanded depot_cheque\n")
					char5.Commit_cheque=random.choice([True,False])
					if(char5.Commit_cheque!=True):
						listx[7]=0
						print("Director rejected the cheque \n")
					else:#char5.Approuve_Pret=True
						listx[7]=1
						print("Director appouve the cheque \n")
				char1.rdv_planing=random.choice([True,False])
				if(char1.rdv_planing !=True):
					pass
				else:#char1.rdv_planing=True
					char2.Financial_planning=True
					print("Conseillers_financiers a donné un conseil financier\n")
					

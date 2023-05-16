import random
import itertools
class Client:
	def __init__(self, name):
		self.name = name
		self.Connection_serveur_client = False
		self.virement = False
		self.depot_cheque= False
		self.appel_tel = False
		self.emprunt=False
		self.Connection_serveur_admin=False
		self.vivement_Approuve=False
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
		self.vivement_Approuve=False
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
        self.vivement_Approuve=False
        self.Approuve_Pret=False
        self.Connection_serveur_employee=False
        self.Commit_cheque=False
        self.server_start=False
# Create Character
char1 = Client("Client1")
char4 = Admin("IT Support")
char5 = Employee("Directeur")

 
#admin_connect,server_status,client_connect,demand_vivement,depot_cheque,vivement_approuved,cheque_approuved

def Eventgen():
    listx=[0,0,0,0,0,0,0,0]
    char4.Connection_serveur_admin=random.choice([True,False])
    if(char4.Connection_serveur_admin !=True):
        print("Admin isn't here \n")
        print(listx)
        return listx
    else: #char4.Connection_serveur_admin =True
        listx[0]=1
        print("Admin come to work!")
        #
        print(listx)
        char4.server_start=random.choice([True,False])
        if(char4.server_start!=True):
            print("Admin didn't start server")
            print(listx)
            return listx
            
        else:
            listx[1]=1
            print("Server start by Admin All operation is permitted\n")
            print(listx)
        char1.Connection_serveur_client=random.choice([True,False])
        if(char1.Connection_serveur_client !=True):
            print("Client isn't connected\n")
            print(listx)
            return listx
        else:#char1.Connection_serveur_client=True
            listx[2]=1
            print("Client is connected\n")
            print(listx)
            char1.depot_cheque=random.choice([True,False])
            if(char1.depot_cheque !=True):
                return listx
                #pass
            else: #char1.depot_cheque=True
                listx[4]=1
                print("Client demanded depot_cheque\n")
                print(listx)
                char5.Commit_cheque=random.choice([True,False])
                if(char5.Commit_cheque!=True):
                    listx[6]=0
                    print("Director rejected the cheque \n")
                    print(listx)
                    return listx
                else:#char5.Approuve_Pret=True
                    listx[6]=1
                    print("Director appouve the cheque \n")
                    print(listx)
                    char1.virement=random.choice([True,False])
                    if(char1.virement !=True):
                        return listx
                        #pass
                    else:#char1.virement=True
                        listx[3]=1
                        print("Client demanded for virement")
                        print(listx)
                        char5.vivement_Approuve=random.choice([True,False])
                        if(char5.vivement_Approuve!=True):
                            listx[5]=0
                            print("Director rejected the vivement\n")
                            print(listx)
                            return listx
                        else:#char5.vivement_Approuve=True
                            listx[5]=1
                            print("Director appouve the cheque \n")
                            print(listx)
                            return listx
def generate_possibilities():
    possibilities = []
    for admin_connect in [False, True]:
        for server_status in [False, True]:
            if not server_status or admin_connect:
                for client_connect in [False, True]:
                    if not client_connect or not depot_cheque or not cheque_approuve or not demand_virement or not vivement_approuve:
                        for demand_virement in [False, True]:
                            if not demand_virement or not depot_cheque:
                                for depot_cheque in [False, True]:
                                    if not depot_cheque or not cheque_approuve:
                                        for employee_connect in [False, True]:
                                            for vivement_approuve in [False, True]:
                                                if not vivement_approuve or demand_virement:
                                                    for cheque_approuve in [False, True]:
                                                        possibilities.append([
                                                            admin_connect,
                                                            server_status,
                                                            client_connect,
                                                            demand_virement,
                                                            depot_cheque,
                                                            employee_connect,
                                                            vivement_approuve,
                                                            cheque_approuve
                                                        ])

    return possibilities





                         
if __name__ == '__main__':
    print("[admin_connect,server_status,client_connect,demand_vivement,depot_cheque,vivement_approuved,cheque_approuved]")
    Eventgen()
    possibilities = generate_possibilities()
    possibilities_count = len(generate_possibilities())
    for possibility in possibilities:
        print(possibility)
    print("Possibility_count : ",possibilities_count)
        
    
                    
            
                    
                    

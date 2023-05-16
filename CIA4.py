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

 
#admin_connect,server_status,client_connect,demand_vivement,depot_cheque,employee_connect,vivement_approuved,cheque_approuved

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
                    listx[7]=0
                    print("Director rejected the cheque \n")
                    print(listx)
                    return listx
                else:#char5.Approuve_Pret=True
                    listx[7]=1
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
                            listx[6]=0
                            print("Director rejected the vivement\n")
                            print(listx)
                            return listx
                        else:#char5.vivement_Approuve=True
                            listx[6]=1
                            print("Director appouve the cheque \n")
                            print(listx)
                            return listx
def generate_possibilities():
    possibilities = []
    for admin_connect in [False, True]:
        for server_status in [False, True]:
            for client_connect in [False, True]:
                for demand_virement in [False, True]:
                    for depot_cheque in [False, True]:
                        for employee_connect in [False, True]:
                            for vivement_approuve in [False, True]:
                                for cheque_approuve in [False, True]:
                                    # Apply conditions and exclude invalid possibilities
                                    if (not admin_connect) or (admin_connect and server_status):
                                        if (not client_connect) or (client_connect and depot_cheque and cheque_approuve and demand_virement and vivement_approuve):
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
    possibilities_count = len(generate_possibilities())
    print("Posibility Count:", possibilities_count)
    return possibilities
                         
if __name__ == '__main__':
    print("[admin_connect,server_status,client_connect,demand_vivement,depot_cheque,employee_connect,vivement_approuved,cheque_approuved]")
    Eventgen()
    possibilities = generate_possibilities()
    
    total_possibilities = len(possibilities)
    print("Total number of possibilities:", total_possibilities)
    for possibility in possibilities:
        print(possibility)

    #print("How many event you want to generate ?")
    #inum=int(input())
    #listforshow=[]
    #for i in range (inum-1):
        #listforshow[i].append(Eventgen())
       # print(listforshow[i])
        
    
                    
            
                    
                    

import time
import datetime
import random

# Fonction pour sélectionner un but
def select_goal():
    # Exemple de sélection de but aléatoire
    goals = ["Ouvrir un nouveau compte", "Effectuer un virement", "Demander un prêt"]
    return random.choice(goals)

# Fonction de moteur de planification en extension avec pré-conditions
def planning_engine(goal):
    # Exemple de planification pour atteindre le but avec pré-conditions
    plan = []
    if goal == "Ouvrir un nouveau compte":
        if check_condition_1():
            plan.append("Vérifier les documents d'identification")
            plan.append("Remplir le formulaire d'ouverture de compte")
            plan.append("Déposer le montant initial")
            plan.append("Créer un compte dans le système")
        else:
            return "Erreur : Condition 1 non respectée"
    elif goal == "Effectuer un virement":
        if check_condition_2():
            plan.append("Vérifier le solde du compte émetteur")
            plan.append("Vérifier les coordonnées bancaires du bénéficiaire")
            plan.append("Saisir le montant et les détails du virement")
            plan.append("Confirmer l'opération de virement")
        else:
            return "Erreur : Condition 2 non respectée"
    elif goal == "Demander un prêt":
        if check_condition_3():
            plan.append("Vérifier l'admissibilité du client")
            plan.append("Collecter les informations financières du client")
            plan.append("Évaluer la capacité de remboursement")
            plan.append("Préparer les documents de demande de prêt")
        else:
            return "Erreur : Condition 3 non respectée"
    return plan

# Fonction d'exécution du plan avec horodatage
def execute_plan(actions):
    # Exemple de fonction pour exécuter le plan d'actions
    print("Exécution du plan :")
    current_time = datetime.datetime.now()
    for i, action in enumerate(actions):
        action_name = action[0]
        action_description = action
        action_timestamp = current_time + datetime.timedelta(seconds=i)
        print("- Action : {} ({})".format(action_description, action_timestamp.strftime("%Y-%m-%d %H:%M:%S")))
        if "Connexion de l'administrateur" in action_description:
            print("    [ADMIN] {}".format(action_description))
        if "Connexion au serveur" in action_description:
            print("    [SERVEUR] Le serveur est en ligne.")
    print("Plan exécuté avec succès.")

# Exemple de fonctions de vérification des pré-conditions (à adapter selon les besoins)
def check_condition_1():
    # Vérifier la disponibilité du serveur en dehors des heures de travail et en présence de l'administrateur
    current_time = datetime.datetime.now().time()
    working_hours_start = datetime.time(9, 0)  # Heure de début des heures de travail
    working_hours_end = datetime.time(17, 0)  # Heure de fin des heures de travail
    is_admin_present = is_administrator_present()  # Vérifier la présence de l'administrateur

    if working_hours_start <= current_time <= working_hours_end and is_admin_present:
        server_status = get_server_status()  # Exemple de fonction pour obtenir l'état du serveur
        admin_login_time = get_admin_login_time(current_time)  # Obtenir l'heure de connexion de l'administrateur
        return server_status == "En ligne", "Connexion de l'administrateur à {}".format(admin_login_time)
    else:
        return False, ""

def check_condition_2():
    # Vérifier si le compte émetteur a suffisamment de fonds
    balance = get_account_balance()  # Exemple de fonction pour obtenir le solde du compte
    return balance >= 1000

def check_condition_3():
    # Vérifier si le client est admissible à un prêt
    credit_score = get_credit_score()  # Exemple de fonction pour obtenir le score de crédit du client
    return credit_score >= 600

def check_condition_server_connection():
    # Vérifier la disponibilité du serveur de la banque (simulons une disponibilité aléatoire avec une probabilité de 70%)
    server_status = random.random() < 0.7  # Exemple de fonction pour obtenir l'état du serveur de la banque
    return server_status, "Connexion au serveur de la banque"

def check_condition_admin_presence():
    # Vérifier la présence de l'administrateur sur le réseau (simulons une présence aléatoire avec une probabilité de 80%)
    is_admin_present = random.random() < 0.8  # Exemple de fonction pour vérifier la présence de l'administrateur
    return is_admin_present, "Présence de l'administrateur sur le réseau"

# Exemple de fonctions pour obtenir des informations (à adapter selon les besoins)
def get_server_status():
    # Exemple de fonction pour obtenir l'état du serveur
    current_time = datetime.datetime.now().time()
    working_hours_start = datetime.time(9, 0)  # Heure de début des heures de travail
    working_hours_end = datetime.time(17, 0)  # Heure de fin des heures de travail

    if working_hours_start <= current_time <= working_hours_end:
        return "En ligne"
    else:
        return "Hors service"

def get_account_balance():
    # Exemple de fonction pour obtenir le solde du compte
    # (simulons un compte avec un solde aléatoire entre 500 et 5000 unités en banque)
    return random.randint(500, 5000)

def get_credit_score():
    # Exemple de fonction pour obtenir le score de crédit du client
    # (simulons un score de crédit aléatoire entre 400 et 800 pour le client)
    return random.randint(400, 800)

def is_administrator_present():
    # Exemple de fonction pour vérifier la présence de l'administrateur
    # (simulons une présence aléatoire avec une probabilité de 80%)
    return random.random() < 0.8

def get_admin_login_time(current_time):
    # Exemple de fonction pour obtenir l'heure de connexion de l'administrateur en fonction de l'heure actuelle
    # (simulons une marge de 30 minutes avant l'heure actuelle)
    time_margin = datetime.timedelta(minutes=30)
    max_login_time = (datetime.datetime.combine(datetime.date.today(), current_time) - time_margin).time()
    admin_login_time = datetime.time(random.randint(9, max_login_time.hour), random.randint(0, 59))
    return admin_login_time



# Exemple d'utilisation des fonctions

selected_goal = select_goal()
print("But sélectionné :", selected_goal)

# Vérifier les pré-conditions de connexion au serveur et de présence de l'administrateur
server_connection_status, server_connection_message = check_condition_server_connection()
admin_presence_status, admin_presence_message = check_condition_admin_presence()

if server_connection_status and admin_presence_status:
    # Les pré-conditions sont remplies, on peut continuer
    planned_actions = planning_engine(selected_goal)
    if isinstance(planned_actions, str):
        print(planned_actions)  # Afficher le message d'erreur
    else:
        print("Actions planifiées :")
        print("- ", server_connection_message)
        print("- ", admin_presence_message)
        execute_plan(planned_actions)
else:
    # Une ou plusieurs pré-conditions ne sont pas remplies
    if not server_connection_status:
        print("Erreur : Impossible de se connecter au serveur de la banque.")
    if not admin_presence_status:
        print("Erreur : L'administrateur n'est pas présent sur le réseau.")

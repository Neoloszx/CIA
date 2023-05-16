import datetime

class Action:
    def __init__(self, name, preconditions, postconditions, machine=None, agent_type=None):
        self.name = name
        self.preconditions = preconditions
        self.postconditions = postconditions
        self.machine = machine
        self.agent_type = agent_type

# Définition des actions disponibles
actions = [
    Action("Observer le trafic réseau", [], ["Trafic observé"], "PC 1", "Agent de sécurité réseau"),
    Action("Analyser les vulnérabilités", ["Trafic observé"], ["Vulnérabilités identifiées"], "PC 2", "Agent de sécurité réseau"),
    Action("Exploiter une vulnérabilité", ["Vulnérabilités identifiées"], ["Système compromis"], "Salle serveurs", "Agent de sécurité réseau"),
    Action("Collecter des informations sensibles", ["Système compromis"], ["Informations sensibles collectées"], "Salle serveurs", "Agent de sécurité réseau"),
    Action("Atteindre l'objectif final", ["Informations sensibles collectées"], ["But atteint"], "PC 1", "Agent de sécurité réseau"),
    Action("Navigation sur des sites Web autorisés", [], ["Activité de navigation enregistrée"], "PC 2", "Salarié de la banque"),
    Action("Envoi et réception d'e-mails professionnels", [], ["E-mails professionnels envoyés/reçus"], "PC 2", "Salarié de la banque"),
    Action("Utilisation d'applications internes", [], ["Activité d'utilisation d'applications enregistrée"], "PC 2", "Salarié de la banque"),
    Action("Connexion aux systèmes de gestion", ["Authentification valide"], ["Accès aux systèmes de gestion établi"], "PC 2", "Salarié de la banque"),
    Action("Transmission de fichiers sensibles", ["Autorisation appropriée"], ["Fichiers sensibles transmis"], "PC 2", "Salarié de la banque"),
    Action("Mise à jour des informations client", ["Autorisation appropriée"], ["Informations client mises à jour"], "PC 2", "Salarié de la banque"),
    Action("Formation à la sécurité informatique", ["Participation à une session de formation"], ["Connaissances en sécurité informatique renforcées"], "PC 2", "Salarié de la banque"),
    Action("Consulter les comptes bancaires", [], ["Comptes bancaires consultés"], "PC personnel", "Client de la banque"),
    Action("Effectuer des transactions financières", ["Comptes bancaires consultés"], ["Transactions financières effectuées"], "PC personnel", "Client de la banque"),
    Action("Gérer les bénéficiaires", [], ["Bénéficiaires gérés"], "PC personnel", "Client de la banque"),
    Action("Modifier les préférences de compte", [], ["Préférences de compte modifiées"], "PC personnel", "Client de la banque")
]

# Fonction pour vérifier si les préconditions d'une action sont remplies
def verif_preconditions(action, etat):
    return all(etat[actions.index(condition)] for condition in action.preconditions)

# Fonction pour appliquer les postconditions d'une action à l'état
def appliquer_postconditions(action, etat):
    return [etat[i] or (i in action.postconditions) for i in range(len(etat))]

# Planificateur en extension
def planificateur_extension(etat_initial, but):
    plan = []
    etat = etat_initial
    while not etat[but]:
        action_possible = None

        for action in actions:
            if verif_preconditions(action, etat):
                action_possible = action
                break

        if action_possible is None:
            return None  # Aucun plan trouvé pour atteindre le but

        plan.append(action_possible)
        etat = appliquer_postconditions(action_possible, etat)

    return plan

# Exemple d'utilisation
etat_initial = [False] * len(actions)
etat_initial[0] = True # Condition initiale pour "Observer le trafic réseau"
but = 4 # But : "But atteint"

plan = planificateur_extension(etat_initial, but)

if plan is not None:
    with open("rapport_activites.txt", "w") as fichier:
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        etat = " - ".join(str(int(cond)) for cond in etat_initial)
        fichier.write(f"{heure} - {etat}\n")
        for action in plan:
            heure = datetime.datetime.now().strftime("%H:%M:%S")
            fichier.write(f"{heure} - {action.name}\n")
            etat_initial = appliquer_postconditions(action, etat_initial)
            heure = datetime.datetime.now().strftime("%H:%M:%S")
            etat = " - ".join(str(int(cond)) for cond in etat_initial)
            fichier.write(f"{heure} - {etat}\n")

        heure = datetime.datetime.now().strftime("%H:%M:%S")
        fichier.write(f"{heure} - But atteint\n")

else:
    print("Aucun plan trouvé pour atteindre le but.")

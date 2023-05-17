import cia
import subprocess

# Initialisation du but
but = [1,0,1,0,1,0,1]

# Exécution du script cia.py
result = subprocess.run(['python', 'cia.py'], capture_output=True)
etat_final = cia.Eventgen()
loop = 0

while (but != etat_final):
    result
    etat_final = cia.Eventgen()
    #print(etat_final)
    loop += 1

print("Etat final est :", etat_final)
print("Nbre itération :", loop)
    






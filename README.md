Ce script est un exemple d'implémentation d'un planificateur en extension pour atteindre un objectif donné à partir d'un état initial. Voici comment il fonctionne :

1. La classe `Action` est définie avec les attributs suivants :
   - `name` : le nom de l'action.
   - `preconditions` : les préconditions nécessaires pour exécuter l'action, représentées sous forme de liste.
   - `postconditions` : les conditions qui seront modifiées après l'exécution de l'action, également représentées sous forme de liste.
   - `machine` : la machine ou l'emplacement où l'action est effectuée (facultatif).
   - `agent_type` : le type d'agent qui exécute l'action (facultatif).

2. Une liste `actions` est créée, contenant des instances de la classe `Action` représentant les différentes actions disponibles.

3. La fonction `verif_preconditions(action, etat)` est définie pour vérifier si toutes les préconditions d'une action sont remplies. Elle retourne `True` si toutes les préconditions sont satisfaites, sinon elle retourne `False`.

4. La fonction `appliquer_postconditions(action, etat)` est définie pour appliquer les postconditions d'une action à un état donné. Elle retourne une nouvelle liste représentant l'état modifié après l'exécution de l'action.

5. La fonction principale `planificateur_extension(etat_initial, but)` implémente l'algorithme de planification en extension. Elle prend en paramètres l'état initial (une liste de booléens représentant les conditions initiales) et l'index de l'objectif à atteindre. Elle retourne un plan (une liste d'actions) pour atteindre l'objectif ou `None` s'il n'y a aucun plan trouvé.

6. Un exemple d'utilisation du planificateur est présenté :
   - Une liste `etat_initial` est créée avec toutes les conditions initiales à `False`, sauf la première condition mise à `True` (dans cet exemple, la première action est "Observer le trafic réseau").
   - L'objectif est défini en spécifiant l'index de l'action dans la liste `actions` (dans cet exemple, l'objectif est l'index 4, correspondant à l'action "Atteindre l'objectif final").
   - Le planificateur est appelé avec l'état initial et l'objectif, et le résultat est stocké dans la variable `plan`.
   - Si un plan est trouvé (c'est-à-dire que `plan` n'est pas `None`), un fichier "rapport_activites.txt" est ouvert en mode écriture.
   - Le script enregistre l'heure actuelle et l'état initial dans le fichier.
   - Pour chaque action dans le plan, le script enregistre l'heure, le nom de l'action, met à jour l'état initial et enregistre le nouvel état dans le fichier.
   - Enfin, le script enregistre l'heure actuelle et le message "But atteint" dans le fichier.

7. Si aucun plan n'est trouvé, le script affiche le message "Aucun plan trouvé pour atteindre le but".

En résumé, ce script utilise un planificateur en extension pour générer un plan d'actions permettant d'atteindre un objectif à partir d'un état initial. Les états

 et les actions sont représentés sous forme de listes, et les préconditions et les postconditions des actions sont vérifiées et appliquées pour progresser vers l'objectif.

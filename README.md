Explication Findpath.py : 
Ce code est un programme Python qui simule un processus de transition d'un état initial à un état final en utilisant des événements aléatoires.

Il définit trois classes : Client, Employee et Admin. Chacune de ces classes représente un acteur dans le système. Chaque acteur possède plusieurs attributs booléens qui indiquent l'état de différentes actions ou connexions.

La fonction RandomEvent simule un événement aléatoire en modifiant les attributs des acteurs. Les acteurs peuvent se connecter à des serveurs, effectuer des virements, déposer des chèques, etc. La fonction retourne une liste listx qui enregistre les états modifiés des attributs des acteurs.

La fonction find_path utilise une approche récursive pour trouver un chemin de l'état initial à l'état final en appelant la fonction RandomEvent pour générer des états aléatoires. Elle utilise également une liste visited_states pour éviter les boucles infinies en empêchant de revisiter les états déjà visités. La fonction retourne le chemin et les actions effectuées pour atteindre l'état final.

La fonction print_path imprime le chemin et les actions effectuées à chaque étape.

Dans la partie principale du code, un état initial et un état final sont définis sous forme de listes. La fonction find_path est appelée avec ces états et les listes vides visited_states et actions. Si un chemin est trouvé, il est imprimé en utilisant la fonction print_path. Sinon, un message indiquant l'absence de chemin est affiché.

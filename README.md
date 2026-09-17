Oui, exactement. 😄 Tu veux **le contenu brut du `README.md`**, sans que je l'entoure d'un bloc de code, pour pouvoir le copier directement dans ton fichier.

 # 🎮 Jeu du Pendu

 ## Version Graphique avec Pygame

 Bienvenue dans ce projet Python : une version graphique du célèbre **jeu du pendu**, développée avec la bibliothèque **Pygame**.

 Le jeu propose une expérience interactive avec une interface graphique permettant au joueur de deviner un mot lettre par lettre.

---

 ## 🛠 Fonctionnalités

 - 🎨 Interface graphique réalisée avec **Pygame**
- ⌨️ Contrôle du jeu via le **clavier**
- 🔠 Affichage des lettres **correctes** et **incorrectes**
- 🧍‍♂️ Dessin progressif du **pendu** à chaque erreur
- 🏁 Affichage de **victoire** ou **défaite**
- 🔁 Possibilité de **relancer une partie**
- 📝 Utilisation d'un fichier de mots personnalisé
- 🏆 Sauvegarde et affichage du **meilleur score**

---

 ## 🚀 Installation

 ### 🧬 1. Cloner le projet

```
git clone git@github.com:mohummadpeer13/HANGMAN-PYGAME.git
cd HANGMAN-PYGAME
```

 ### ⚙️ 2. Prérequis

 Le projet nécessite **Python 3.12**, `pip` ainsi que la bibliothèque **Pygame**.

 Sur Ubuntu/Debian :

```
sudo apt update
sudo apt install python3.12 python3.12-venv
```

 ### 🔒 3. Créer l'environnement virtuel

```
python3.12 -m venv .venv
```

 Activer l'environnement virtuel :

```
source .venv/bin/activate
```

 ### 📦 4. Installer les dépendances

```
python -m pip install --upgrade pip
python -m pip install pygame
```

---

 ## ▶️ Lancer le jeu

 Une fois l'environnement virtuel activé, lance le jeu avec :

```
python hangman-gui.py my_wordlist.txt
```

 Le fichier `my_wordlist.txt` contient les mots utilisés pour les différentes parties.

---

 ## 🎮 Comment jouer ?

 1. Un **mot est choisi aléatoirement** dans le fichier `my_wordlist.txt`.
2. Le joueur sélectionne des **lettres au clavier**.
3. Si la lettre est correcte, elle apparaît à la bonne position dans le mot.
4. Si la lettre est incorrecte, une partie du **pendu est dessinée**.
5. Le joueur doit trouver le mot avant que le dessin du pendu soit terminé.
6. Le joueur **gagne** s'il trouve toutes les lettres.
7. Le joueur **perd** si le pendu est entièrement dessiné.
8. Une fois la partie terminée, une nouvelle partie peut être lancée.
9. Le **meilleur score** est automatiquement sauvegardé et affiché.

---

 ## 📁 Structure du projet

```
HANGMAN-PYGAME/
├── hangman-gui.py
├── my_wordlist.txt
├── .venv/
└── README.md
```

---

 ## 🏆 Système de score

 Le jeu possède un système de **meilleur score**.

 Le score est sauvegardé automatiquement et peut être affiché lors des prochaines parties.

---

 ## 🧑‍💻 Technologies utilisées

 - 🐍 **Python 3.12**
- 🎮 **Pygame**
- 📝 Fichier texte pour la liste de mots
- 💾 Sauvegarde du meilleur score

---

 ## 📜 Licence

 Projet réalisé dans le cadre d'un projet **Epitech**.

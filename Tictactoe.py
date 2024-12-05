import random

""" 
Jeu de Tic Tac Toe 
Ce programme permet de jouer au jeu de Tic Tac Toe en mode console. 
Deux joueurs s'affrontent tour à tour en choisissant une case sur une grille de 3x3. 
Le premier joueur à aligner trois de ses symboles (horizontalement, verticalement ou en diagonale) 
gagne la partie. En cas de grille pleine sans victoire, la partie se termine par un match nul. 
Fonctions : 
- intro() : Affiche le message de bienvenue. 
- initialiser_grille() : Initialise une grille de jeu vide pour le Tic Tac Toe. 
- afficher_grille(grille) : Affiche la grille actuelle du jeu. 
- verifier_lignes(grille, symbole) : Vérifie si une des lignes de la grille est gagnante. 
- verifier_colonnes(grille, symbole) : Vérifie si une des colonnes de la grille est gagnante. 
- verifier_diagonales(grille, symbole) : Vérifie si une des diagonales de la grille est gagnante. 
- verifier_victoire(grille, symbole) : Vérifie si le joueur actuel a gagné. 
- grille_pleine(grille) : Vérifie si la grille est pleine. 
- saisir_coup(joueur, grille) : Demande au joueur de saisir son coup et met à jour la grille. 
- morpion() : Fonction principale du jeu Tic Tac Toe. 

Lancer le jeu :
- morpion() : Démarre le jeu Tic Tac Toe. 

"""

# Initialisation de la grille
def initialiser_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def afficher_grille(grille):
    print("\n+---+---+---+")
    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")
        print("+---+---+---+")

# Vérification des lignes
def verifier_lignes(grille, symbole):
    for ligne in grille:
        if ligne == [symbole, symbole, symbole]:
            return True
    return False

# Vérification des colonnes
def verifier_colonnes(grille, symbole):
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == symbole:
            return True
    return False

# Vérification des diagonales
def verifier_diagonales(grille, symbole):
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True
    return False

# Vérification de la victoire
def verifier_victoire(grille, symbole):
    return verifier_lignes(grille, symbole) or verifier_colonnes(grille, symbole) or verifier_diagonales(grille, symbole)

# Vérifier si la grille est pleine
def grille_pleine(grille):
    return all(cell != " " for ligne in grille for cell in ligne)

# Demander le choix du joueur
def saisir_coup(joueur, grille):
    while True:
        try:
            choix = int(input(f"Joueur {joueur}, entrez un numéro de case (1-9) : ")) - 1
            x, y = divmod(choix, 3)  # Calculer les indices ligne et colonne
            if grille[x][y] == " ":
                grille[x][y] = joueur
                break
            else:
                print("Cette case est déjà prise. Essayez une autre.")
        except (ValueError, IndexError):
            print("Entrée invalide. Entrez un numéro entre 1 et 9.")

# Boucle principale du jeu
def morpion():

    # Intro du jeu
    def intro():
        print('Bienvenue sur Tic Tac Toe ! Le premier joueur peut commencer. Que le meilleur gange..')

    intro()

    grille = initialiser_grille()
    afficher_grille(grille)
    joueur_actuel = "X"
    
    while True:
        saisir_coup(joueur_actuel, grille)
        afficher_grille(grille)
        
        if verifier_victoire(grille, joueur_actuel):
            print(f"Félicitations, le joueur {joueur_actuel} a gagné !")
            break
        
        if grille_pleine(grille):
            print("Match nul ! Merci d'avoir joué.")
            break
        
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancer le jeu
morpion()

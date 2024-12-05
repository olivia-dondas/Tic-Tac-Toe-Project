import random

""" 
Jeu de Tic Tac Toe 
Ce programme permet de jouer au jeu de Tic Tac Toe en mode console. 
Deux joueurs s'affrontent tour à tour en choisissant une case sur une grille de 3x3. 
Le premier joueur à aligner trois de ses symboles (horizontalement, verticalement ou en diagonale) 
gagne la partie. En cas de grille pleine sans victoire, la partie se termine par un match nul. 
Fonctions : 
- initialiser_grille() : Initialise une grille de jeu vide pour le Tic Tac Toe. 
- afficher_grille(grille) : Affiche la grille actuelle du jeu. 
- afficher_grille_numerique() : Affiche la grille avec les numéros pour indiquer les positions possibles. 
- verifier_lignes(grille, symbole) : Vérifie si une des lignes de la grille est gagnante. 
- verifier_colonnes(grille, symbole) : Vérifie si une des colonnes de la grille est gagnante. 
- verifier_diagonales(grille, symbole) : Vérifie si une des diagonales de la grille est gagnante. 
- verifier_victoire(grille, symbole) : Vérifie si le joueur actuel a gagné. 
- grille_pleine(grille) : Vérifie si la grille est pleine. 
- saisir_coup(joueur, grille) : Demande au joueur de saisir son coup et met à jour la grille. 
- morpion() : Fonction principale du jeu Tic Tac Toe. 
- intro() : Affiche le message de bienvenue. 

Lancer le jeu :
- morpion() : Démarre le jeu Tic Tac Toe. 
"""

# Initialisation de la grille
def initialiser_grille():
    return [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def afficher_grille(grille):
    lignes = ["+---+---+---+"]
    for ligne in grille:
        lignes.append("| " + " | ".join(ligne) + " |")
        lignes.append("+---+---+---+")
    return lignes

# Fonction de l'affichage de la grille avec chiffres
def afficher_grille_numerique():
    lignes = ["+---+---+---+"]
    for i in range(0, 9, 3):
        lignes.append(f"| {i+1} | {i+2} | {i+3} |")
        lignes.append("+---+---+---+")
    return lignes

# Fonction pour afficher les deux grilles côte à côte
def afficher_grilles_cote_a_cote(grille):
    grille_jeu = afficher_grille(grille)
    grille_chiffres = afficher_grille_numerique()
    for ligne_jeu, ligne_chiffre in zip(grille_jeu, grille_chiffres):
        print(ligne_jeu, "  ", ligne_chiffre)

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
            choix = int(input(f"Joueur {joueur}, choisis un numéro de case entre 1 et 9 : ")) - 1
            x, y = divmod(choix, 3)  # Calculer les indices ligne et colonne
            if grille[x][y] == " ":
                grille[x][y] = joueur
                break
            else:
                print("Too bad! Cette case est déjà prise. Essaies en une autre.")
        except (ValueError, IndexError):
            print("Entrée invalide. -_- Choisis un numéro entre 1 et 9.")

# Boucle principale du jeu
def morpion():
    # Intro du jeu
    def intro():
        print('Bienvenue sur Tic Tac Toe ! Le premier joueur peut commencer. Le premier joueur qui aligne 3 symboles remporte la partie. Que le meilleur gagne.')

    intro()

    grille = initialiser_grille()
    afficher_grilles_cote_a_cote(grille)
    joueur_actuel = "X"
    
    while True:
        saisir_coup(joueur_actuel, grille)
        afficher_grilles_cote_a_cote(grille)
        
        if verifier_victoire(grille, joueur_actuel):
            print(f"Bravooo champion! C'est le joueur {joueur_actuel} qui a gagné !")
            break
        
        if grille_pleine(grille):
            print("Match nul... comme vous les LOSERS! Merci quand même d'avoir joué.")
            break
        
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancer le jeu
morpion()


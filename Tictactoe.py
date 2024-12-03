import random

#Intro du jeu 
print('Bienvenue sur Tic Tac Toe ! Arriveras-tu à me battre?')

# Grille
grille = [[" " for _ in range(3)] for _ in range(3)]

# Fonction pour afficher la grille
def afficher_grille(grille):
    print("\n+---+---+---+")
    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")
        print("+---+---+---+")

# Vérification des conditions de victoire
def verifier_victoire(grille, symbole):
    # Vérifier les lignes
    for ligne in grille:
        if ligne == [symbole, symbole, symbole]:
            return True
    # Vérifier les colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == symbole:
            return True
    # Vérifier les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0]:
        return True
    return False   
# Vérifier si la grille est pleine
def grille_pleine(grille):
    for ligne in grille:
        if " " in ligne:
            return False
    return True
     

# Demander le choix du joueur
def jouer_tour(joueur):
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


# Jeu principal
def morpion():
    afficher_grille(grille)
    joueur_actuel = "X"
    
    while True:
        # Jouer le tour
        jouer_tour(joueur_actuel)
        afficher_grille(grille)
        
        # Vérifier la victoire
        if verifier_victoire(grille, joueur_actuel):
            print(f"Félicitations, le joueur {joueur_actuel} a gagné !")
            break
        
        # Vérifier l'égalité
        if grille_pleine(grille):
            print("Match nul ! Merci d'avoir joué.")
            break
        
        # Changer de joueur
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Vérification des conditions de victoire
def verifier_victoire(grille, symbole):
    # Vérifier les lignes
    for ligne in grille:
        if ligne == [symbole, symbole, symbole]:
            return True
    # Vérifier les colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == symbole:
            return True
    # Vérifier les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0]:
        return True
    return False

# Demander le choix du joueur
def jouer_tour(joueur):
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



#les conditions pour gagner : 
def lignehorizontle(plateau):
    global gagnant
    if plateau[0] == plateau[1] == plateau[2] and plateau[0] != "-":
        gagnant = plateau[0]
        return True
    elif plateau[3] == plateau[4] == plateau[5] and plateau[3] != "-":
        gagnant = plateau[3]
        return True
    elif plateau[6] == plateau[7] == plateau[8] and plateau[6] != "-":
        gagnant = plateau[6]
        return True


def morpion():
    afficher_grille(grille)
    joueur_actuel = "X"
    
    while True:
        # Jouer le tour
        jouer_tour(joueur_actuel)
        afficher_grille(grille)
        
        # Vérifier la victoire
        if verifier_victoire(grille, joueur_actuel):
            print(f"Félicitations, le joueur {joueur_actuel} a gagné !")
            break
        
        # Vérifier l'égalité
        if grille_pleine(grille):
            print("Match nul ! Merci d'avoir joué.")
            break
        
        # Changer de joueur
        joueur_actuel = "O" if joueur_actuel == "X" else "X"

# Lancer le jeu
morpion()
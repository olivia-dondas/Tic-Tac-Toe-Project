
                                                                        #Variable de base 


grille = ["-","-","-","-","-","-","-","-","-",]

joueur_actuel = ""
fin_jeu = False
gagnant = ""

                                                                #Fonction de toutes les fonctions
def jouer():
    choix_joueur()
    affichage_grille()
    while fin_jeu == False :
        tour(joueur_actuel)
        verifier_fin_jeu()
        joueur_suivant()
    resultat()

                                                            #Fonction pour le choix du joueur 
def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O): " )
    while True : 
        joueur_actuel = joueur_actuel.upper()
        if joueur_actuel == "X" :
            print ("Vous avez choisi X, le joueur 2 aura O")
            break
        
        elif joueur_actuel == "O":
            print("Vous avez choisi O, le joueur 2 aura X")
            break

        else : 
            joueur_actuel = input("Veuillez choisir soit une croix (X), soit un rond (O) " )

                                            #Fonction de l'affichage de grille
def affichage_grille():
    print("\n")
    print("-----------------")
    print("|", grille[0], "|","|", grille[1], "|","|", grille[2], "|                |   1   |   2   |   3   |")
    print("-----------------")
    print("|", grille[3], "|","|", grille[4], "|","|", grille[5], "|                |   4   |   5   |   6   |")
    print("-----------------")
    print("|", grille[6], "|","|", grille[7], "|","|", grille[8], "|                |   7   |   8   |   9   |")
    print("-----------------")

                                                                        #Fonction des tours des joueurs

def tour(joueur) :
    print("C'est le tour dur joueur : ", joueur )
    pos = input ("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : " )

    valide = False
    while valide == False :

        while pos not in ["1", "2", "3","4", "5", "6","7", "8", "9"] :                  #Définir qu'il faut choisir une position compris entre 1 et 9
            pos = input ("Veuillez sélectionner un espace vide sur la grille entre 1 et 9 : " )
        pos = int(pos) - 1

        if grille [pos] == "-" :
            valide = True

        else :
            print("Vous ne pouvrez pas accéder à cette position")       #Print un message d'erreur quand l'on ne choisit pas une position connue

        grille[pos] = joueur
        affichage_grille()

def verifier_fin_jeu():
    verifier_victoire()                                                         # Fonction qui vérifie la fin de jeu
    verifier_match_nul()

def verifier_victoire() :
                                                    #Global = Décris une variable comme "Global", peut étre accessible et changer au fur et a mesure du programme
    global fin_jeu
    global gagnant                                                                                                          

                                                                                            #Vérification de victoire en vertical 
    if grille[0] == grille [1] == grille [2] and grille[2] != "-" :
        fin_jeu = True
        gagnant = grille[1]
    if grille[3] == grille [4] == grille [5] and grille[5] != "-" :
        fin_jeu = True
        gagnant = grille[2]
    if grille[6] == grille [7] == grille [8] and grille[8] != "-" :
        fin_jeu = True
        gagnant = grille[8]
    if grille[0] == grille [3] == grille [6] and grille[2] != "-" :
        fin_jeu = True
        gagnant = grille[6]
    if grille[1] == grille [4] == grille [7] and grille[7] != "-" :
        fin_jeu = True
        gagnant = grille[7]
    if grille[2] == grille [5] == grille [8] and grille[8] != "-" :
        fin_jeu = True
        gagnant = grille[8]

                                                                                            #Vérification de victoire en Diagonale
    if grille[0] == grille [4] == grille [4] and grille[8] != "-" :
        fin_jeu = True                                                                        
        gagnant = grille[8]
    if grille[2] == grille [4] == grille [6] and grille[6] != "-" :
        fin_jeu = True
        gagnant = grille[6]

def verifier_match_nul() :                                          #CONDITION DE MATCH NUL
    global fin_jeu
    if "-" not in grille :
        fin_jeu = True

def joueur_suivant() :                                              #Fonction qui permet de définir quelle joueur doit jouer
    global joueur_actuel
    if joueur_actuel == "X" :
        joueur_actuel = "O"
    else :
        joueur_actuel = "X"

def resultat () :                                                                #Permet de donner un résultat si les condition sont réunis
    if gagnant == "X" or gagnant == "O" :
        print("Le joueur : ", gagnant, "a gagné")
    else :
        print("Match nul. " )



jouer()                 #Appeler la fonction jouer














                            # Morpion SCOTT ET SAMMY
# from random import *

# """L'ultime grille (buggé)"""


# """Séléction du mode de jeu."""


# #Début de la "boucle de démarrage"
# status = False

# while status != True:

#     print( 
#         "Séléctionnez le mode de jeu : " "\n"
#         "1 : Joueur contre Joueur." "\n"
#         "2 : Joueur contre IA" "\n"
#     )

#     #Séléction du mode
#     select = int(input("Mode choisi : "))
    
#     """MODE JOUEUR CONTRE JOUEUR"""

#     if select == 1: #Joueur contre Joueur

#         """Séléction camp"""

#         print(
#             "\n"
#             "Veuillez séléctionner votre camp : " "\n"
#             "Croix = O" "\n"
#             "Ronds = X"
#         )

#         joueur_1 = input("Joueur 1 : ")
#         joueur_2 = None

#         if joueur_1 == "X":
#             joueur_2 = "O"

#         if joueur_1 == "O":
#             joueur_2 = "X"
#         print("Joueur 2 :",joueur_2)
    

#     """MODE JOUEUR CONTRE AI"""

#     if select == 2: #Joueur contre AI
           
#         """Selection camp"""

#         print(
#             "\n"
#             "Veuillez séléctionner votre camp : " "\n"
#             "Croix = O" "\n"
#             "Ronds = X"
#         )

#         Humain = input("Joueur 1 : ")
#         Ai = None

#         if Humain == "X":
#             Ai = "O"

#         if Humain == "O":
#             Ai = "X"
#         print("AI :", Ai)

#         print("En développement. L'AI est très space...")
#         break

#     status = True #Fin de la boucle de séléction


# """Formation de la grille"""


# #Création de la grille
# grille = [0,1,2,3,4,5,6,7,8]

# def morpionnage(liste:list):
#     """Formatte la liste grille afin d'avoir 
#     un morpion affiché dans le terminal."""
#     print(
#     f"{liste[6]} | {liste[7]} | {liste[8]}" "\n"
#     "---------" "\n"
#     f"{liste[3]} | {liste[4]} | {liste[5]}" "\n"
#     "---------" "\n"
#     f"{liste[0]} | {liste[1]} | {liste[2]}" "\n"
#     )


# """Gestion de la partie"""

# tour = 1 #Note : il y a 9 tours

# """JOUEUR CONTRE JOUEUR"""


# if select == 1: #Boucle de jeu Joueur contre Joueur
#     i = 1
#     while i < 10:

#         """Au tour du joueur 1"""

#         print(morpionnage(grille))

#         j1 = int(input("Joueur 1, position : "))
    
#         for c in grille:
#             if j1 == c:
#                 grille[c] = joueur_1
        
#         #VICTOIRES LIGNES VERTICALES

#         if grille[0] == joueur_1 and grille[3] == joueur_1 and grille[6] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break
    
#         if grille[1] == joueur_1 and grille[4] == joueur_1 and grille[7] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break
    
#         if grille[2] == joueur_1 and grille[5] == joueur_1 and grille[8] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break

#         #VICTOIRES LIGNES HORIZONTALES

#         if grille[0] == joueur_1 and grille[1] == joueur_1 and grille[2] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break
    
#         if grille[3] == joueur_1 and grille[4] == joueur_1 and grille[5] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break

#         if grille[6] == joueur_1 and grille[7] == joueur_1 and grille[8] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break

#         #VICTOIRES LIGNES DIAGONALES

#         if grille[2] == joueur_1 and grille[4] == joueur_1 and grille[6] == joueur_1:
#             print("\n""joueur 1 a gagné")
#             break

#         if grille[0] == joueur_1 and grille[4] == joueur_1 and grille[8] == joueur_1:
#             print("\n""Joueur 1 a gagné")
#             break

#         """Au tour du joueur 2"""

#         print(morpionnage(grille))

#         j2 = int(input("Joueur 2, position : "))
    
#         for r in grille:
#             if j2 == r:
#                 grille[r] = joueur_2

#         """E N D I N G S  R O N D"""

#         #VICTOIRES LIGNES VERTICALES

#         if grille[0] == joueur_2 and grille[3] == joueur_2 and grille[6] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break
    
#         if grille[1] == joueur_2 and grille[4] == joueur_2 and grille[7] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break
    
#         if grille[2] == joueur_2 and grille[5] == joueur_2 and grille[8] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break

#         #VICTOIRES LIGNES HORIZONTALES

#         if grille[0] == joueur_2 and grille[1] == joueur_2 and grille[2] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break
    
#         if grille[3] == joueur_2 and grille[4] == joueur_2 and grille[5] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break

#         if grille[6] == joueur_2 and grille[7] == joueur_2 and grille[8] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break

#         #VICTOIRES LIGNES DIAGONALES

#         if grille[2] == joueur_2 and grille[4] == joueur_2 and grille[6] == joueur_2:
#             print("\n""joueur 2 a gagné")
#             break

#         if grille[0] == joueur_2 and grille[4] == joueur_2 and grille[8] == joueur_2:
#             print("\n""Joueur 2 a gagné")
#             break

#         i += 1
#         if i >= 9:
#             print("Match nul. c'est nul.")



# """JOUEUR CONTRE INTELIGENCE ARTIFICIELLE IDIOTE"""

# grille = [0,1,2,3,4,5,6,7,8,9]

# disponible = [0,1,2,3,4,5,6,7,8,9]

# if select == 2:

#     """     Deroulement : comment l'ia fonctionne

# Donc on a deux listes :
# grille : la ou on joue
# available : places libres dans la liste

# Qu'on soit d'accord, les croix et les ronds sont des strings.("X" et "O")
# Ca veut dire que l'ia va choisir un entier entre 1 et 8 dans la liste available.
# Si l'entier est présent dans la liste
# alors il place sa croix/rond
# Pour éviter les conflits, chaque place choisi par l'ia et le joueur sera supprimé
# de la liste available grâce à la fonction del
# *Note marrante : En voulant éviter ce conflit j'ai créer d'autres conflits    
#     """
    
#     tour = 0
    
#     while disponible != []:
        
#         """Au tour du joueur"""

#         #print(morpionnage(grille))
        
#         #print(available)

#         print(morpionnage(grille))

#         Choix_Joueur = int(input("Choisissez une place disponible : "))
        
#         if Choix_Joueur in grille:
#             #print("Il est la le frère.")
#             grille[Choix_Joueur] = Humain
#             #print(morpionnage(grille))
#             del(disponible[Choix_Joueur-tour])
#             #print(disponible)
            
#             #print("Tour = ", tour)
            

#         #VICTOIRES LIGNES VERTICALES

#         if grille[0] == Humain and grille[3] == Humain and grille[6] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break
    
#         if grille[1] == Humain and grille[4] == Humain and grille[7] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break
    
#         if grille[2] == Humain and grille[5] == Humain and grille[8] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break

#         #VICTOIRES LIGNES HORIZONTALES

#         if grille[0] == Humain and grille[1] == Humain and grille[2] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break
    
#         if grille[3] == Humain and grille[4] == Humain and grille[5] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break

#         if grille[6] == Humain and grille[7] == Humain and grille[8] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break

#         #VICTOIRES LIGNES DIAGONALES

#         if grille[2] == Humain and grille[4] == Humain and grille[6] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break

#         if grille[0] == Humain and grille[4] == Humain and grille[8] == Humain:
#             print("\n""L'Humain a gagné. Logique...")
#             break

#         tour += 1
            

#         """Au tour de l'IA"""


#         #print(morpionnage(grille))

#         Choix_ia = choice(disponible)
#         #print("L'ia a choisi : ",Choix_ia)
#         if Choix_ia in disponible:
#             grille[Choix_ia-tour] = Ai
#             del(disponible[Choix_ia-tour])

#         tour += 1

#         #VICTOIRES LIGNES VERTICALES

#         if grille[0] == Ai and grille[3] == Ai and grille[6] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break
    
#         if grille[1] == Ai and grille[4] == Ai and grille[7] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break
    
#         if grille[2] == Ai and grille[5] == Ai and grille[8] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break

#         #VICTOIRES LIGNES HORIZONTALES

#         if grille[0] == Ai and grille[1] == Ai and grille[2] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break
    
#         if grille[3] == Ai and grille[4] == Ai and grille[5] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break

#         if grille[6] == Ai and grille[7] == Ai and grille[8] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break

#         #VICTOIRES LIGNES DIAGONALES

#         if grille[2] == Ai and grille[4] == Ai and grille[6] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break

#         if grille[0] == Ai and grille[4] == Ai and grille[8] == Ai:
#             print("\n""L'intelligence artificielle a gagné, un exploit.")
#             break

        

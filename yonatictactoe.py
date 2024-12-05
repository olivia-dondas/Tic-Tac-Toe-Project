# import de tkinter
import tkinter
from tkinter import messagebox

# init de ma fenetre graphique
root = tkinter.Tk()
root.title("Tic Tac Toe ✅")
root.resizable(False, False)
root.geometry("600x600")

# variables
joueur_actuel = "X"
joueur_1_prenom = ""
joueur_2_prenom = ""
symbol_joueur_1 = ""
symbol_joueur_2 = ""
tableau = [["" for _ in range(3)] for _ in range(3)]

# init des users par leurs nom et choix symbole 
def config_des_joueurs():
    global joueur_1_prenom, joueur_2_prenom, joueur_actuel, symbol_joueur_1, symbol_joueur_2

    joueur_1_prenom = input("Entrer le nom du premier joueur:")
    joueur_2_prenom = input("Entrer le nom du deuxième joueurs: ")

    if not joueur_1_prenom or not joueur_2_prenom:
        print("Erreur: Veuillez entrer les noms des joeurs")
        config_des_joueurs()

    choix_symbol = input(f"{joueur_1_prenom}, Veuillez choisir le symbol (X or O): ").upper()
    if choix_symbol == "X":
        symbol_joueur_1 = "X"
        symbol_joueur_2 = "O"
    elif choix_symbol == "O":
        symbol_joueur_1 = "O"
        symbol_joueur_1 = "X"
    else:
        print("Erreur: Veuillez entrer un symbole entre le X ou O.")
        config_des_joueurs()

    joueur_actuel = symbol_joueur_1

# au click d'un bouton on appel cette fonction
def clic_sur_bouton(lignes, colonnes, button):
    global joueur_actuel

    if tableau[lignes][colonnes] == "":
        tableau[lignes][colonnes] = joueur_actuel
        button.config(text=joueur_actuel, state="disabled")
        gagnant = verifier_victoire()
        if gagnant:
            nom_gagnant = obtenir_le_nom_du_joueur_gagnant(gagnant)
            messagebox.showinfo("Victoire", f"joueurs {nom_gagnant} gagné!")
            root.quit()
        elif all(all(cell != "" for cell in row) for row in tableau):
            messagebox.showinfo("Egalité : C'est une égalité!")
            root.quit()
        else:
            joueur_actuel = symbol_joueur_2 if joueur_actuel == symbol_joueur_1 else symbol_joueur_1

# sert dans la fonction click_sur_bouton, en cas de victoire permet d'avoir le nom du joueur en fonction de son symbole
def obtenir_le_nom_du_joueur_gagnant(symbole):
    if symbole == symbol_joueur_1:
        return joueur_1_prenom
    else:
        return joueur_2_prenom

# sert aussi dans la fonction click_sur_bouton, sert à verifier toutes les combinaisons de victoire
def verifier_victoire():
    for lignes in tableau:
        if lignes[0] == lignes[1] == lignes[2] != "":
            return lignes[0]
    for colonnes in range(3):
        if tableau[0][colonnes] == tableau[1][colonnes] == tableau[2][colonnes] != "":
            return tableau[0][colonnes]
    if tableau[0][0] == tableau[1][1] == tableau[2][2] != "":
        return tableau[0][0]
    if tableau[0][2] == tableau[1][1] == tableau[2][0] != "":
        return tableau[0][2]
    return None

# sert à afficher 3 lignes de 3 boutons sur ma fenetre
for row in range(3):
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(row, weight=1)

    for col in range(3):
        btn = tkinter.Button(root, font=("Arial", 36))
        btn.grid(row=row, column=col, sticky="nsew")
        btn.config(command=lambda r=row, c=col, b=btn: clic_sur_bouton(r, c, b))

config_des_joueurs()
root.mainloop()

import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Tic Tac Toe")

# Configuration de la grille de boutons
buttons = [[None for _ in range(3)] for _ in range(3)]  # Grille 3x3

def on_click(row, col):
    buttons[row][col].config(text="X")  # Exemple : placer un X au clic
    buttons[row][col].config(text=("Y"))



# Création des boutons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j)  # Positionner les boutons sur la grille

# Démarrer la boucle d'événements
root.mainloop()

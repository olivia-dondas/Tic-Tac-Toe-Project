import tkinter
import tkinter as tk

def draw_grid():
    button = tkinter.Button(root)
    button.pack()

 #creer la fenêtre de jeu
root = tk.Tk()

#perso de la fenetre
root.title("Tic Tac Toe")
root.minsize(500, 500)

draw_grid()
root.mainloop()






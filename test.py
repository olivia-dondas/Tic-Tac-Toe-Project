import tkinter
import tkinter as tk

def draw_grid():
    for column in range(3):
        for row in range(3):
            button = tkinter.Button(root)
            button.grid(row=row, column=column)

 #creer la fenêtre de jeu
root = tk.Tk()

#perso de la fenetre
root.title("Tic Tac Toe")
root.minsize(500, 500)

draw_grid()
root.mainloop()






import tkinter
from tkinter import messagebox

# init window
root = tkinter.Tk()
root.title("Tic Tac Toe ✅")
root.resizable(False, False)
root.geometry("600x600")

# globals
current_player = "X"
player_1_name = ""
player_2_name = ""
board = [["" for _ in range(3)] for _ in range(3)]  # 3x3

# Function to ask for the names and symbols via the terminal
def setup_players():
    global player_1_name, player_2_name, current_player

    # Ask name players by the terminal
    player_1_name = input("Enter the player's name 1:")
    player_2_name = input("Enter the player's name 2:")

    # verify names register
    if not player_1_name or not player_2_name:
        print("Error: Please enter the names of both players")
        setup_players()  # Relaunch the function if a name is missing

     # ask players to choose symbols
    symbol_choice = input(f"{player_1_name}, Choose your symbol (X ou O): ").upper()
    if symbol_choice == "X":
        current_player = "X"
    elif symbol_choice == "O":
        current_player = "O"
    else:
        print("Erreur: The symbol must be. X ou O.")
        setup_players()  # Relaunch the function if an incorrect symbol is chosen

# ask info players
setup_players()

# verify winner
def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None  # No winner

# Function when the player clicks on a button
def on_button_click(row, col, button):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        button.config(text=current_player, state="disabled")  # disabled button if clicked
        winner = check_winner()
        if winner:
            messagebox.showinfo("Victory", f"Player {winner} win")
            root.quit()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Egual", "No winner")
            root.quit()
        else:  # else next player
            current_player = "O" if current_player == "X" else "X"


# init board
for row in range(3):  # 3 lines

    # grid takes all the size of the window
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(row, weight=1)

    for col in range(3):  # 3 rows
        btn = tkinter.Button(root, font=("Arial", 36))
        btn.grid(row=row, column=col, sticky="nsew")  # sticky : each button takes the available space
        btn.config(command=lambda r=row, c=col, b=btn: on_button_click(r, c, b)) # lambda : wait event

# important, dont delete
root.mainloop()

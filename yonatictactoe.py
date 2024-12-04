import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Tic Tac Toe ✅")
root.resizable(False, False)
root.geometry("600x600")

current_player = "X"
player_1_name = ""
player_2_name = ""
symbol_player_1 = ""
symbol_player_2 = ""
board = [["" for _ in range(3)] for _ in range(3)]


def setup_players():
    global player_1_name, player_2_name, current_player, symbol_player_1, symbol_player_2

    player_1_name = input("Enter the player's name 1: ")
    player_2_name = input("Enter the player's name 2: ")

    if not player_1_name or not player_2_name:
        print("Error: Please enter the names of both players")
        setup_players()

    symbol_choice = input(f"{player_1_name}, Choose your symbol (X or O): ").upper()
    if symbol_choice == "X":
        symbol_player_1 = "X"
        symbol_player_2 = "O"
    elif symbol_choice == "O":
        symbol_player_1 = "O"
        symbol_player_2 = "X"
    else:
        print("Error: The symbol must be either X or O.")
        setup_players()

    current_player = symbol_player_1


setup_players()


def get_player_name(symbol):
    if symbol == symbol_player_1:
        return player_1_name
    else:
        return player_2_name


def check_winner():
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
    return None


def on_button_click(row, col, button):
    global current_player

    if board[row][col] == "":
        board[row][col] = current_player
        button.config(text=current_player, state="disabled")
        winner = check_winner()
        if winner:
            winner_name = get_player_name(winner)
            messagebox.showinfo("Victory", f"Player {winner_name} wins!")
            root.quit()
        elif all(all(cell != "" for cell in row) for row in board):
            messagebox.showinfo("Draw", "It's a draw!")
            root.quit()
        else:
            current_player = symbol_player_2 if current_player == symbol_player_1 else symbol_player_1


for row in range(3):
    root.grid_rowconfigure(row, weight=1)
    root.grid_columnconfigure(row, weight=1)

    for col in range(3):
        btn = tkinter.Button(root, font=("Arial", 36))
        btn.grid(row=row, column=col, sticky="nsew")
        btn.config(command=lambda r=row, c=col, b=btn: on_button_click(r, c, b))

root.mainloop()

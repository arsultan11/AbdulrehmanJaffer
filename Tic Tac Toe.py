import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9
buttons = []
game_over = False

def create_window():
    window = tk.Tk()
    window.title("TIC TAC TOE")
    window.geometry("400x450")
    window.resizable(False, False)
    return window

def create_game_board(window):
    global buttons
    board_frame = tk.Frame(window)
    board_frame.pack(pady=10)

    for i in range(9):
        row = i // 3
        col = i % 3
        button = tk.Button(
            board_frame,
            text="",
            width=6,
            height=3,
            font=("Arial", 20, "bold"),
            command=lambda pos=i: button_click(pos)
        )
        button.grid(row=row, column=col, padx=2, pady=2)
        buttons.append(button)

    # Control buttons (New Game, Exit)
    control_frame = tk.Frame(window)
    control_frame.pack(pady=15)

    new_game_btn = tk.Button(control_frame, text="New Game", font=("Arial", 12), command=reset_game, width=12)
    new_game_btn.grid(row=0, column=0, padx=10)

    exit_btn = tk.Button(control_frame, text="Exit", font=("Arial", 12), command=window.quit, width=12)
    exit_btn.grid(row=0, column=1, padx=10)

def button_click(position):
    global current_player, game_over

    if game_over or board[position] != "":
        return

    board[position] = current_player
    buttons[position].config(text=current_player, state="disabled")

    winner_combo = check_winner()
    if winner_combo:
        for idx in winner_combo:
            buttons[idx].config(bg="lightgreen")
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        game_over = True
        return
    elif "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        game_over = True
        return

    current_player = "O" if current_player == "X" else "X"

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return combo
    return None

def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    for button in buttons:
        button.config(text="", bg="SystemButtonFace", state="normal")

# Run the game
window = create_window()
create_game_board(window)
window.mainloop()
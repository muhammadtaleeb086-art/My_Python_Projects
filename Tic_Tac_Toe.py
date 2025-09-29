import tkinter as tk
from tkinter import messagebox

# Function to check winner after each move
def check_winner():
    global winner
    # All possible winning combinations (rows, cols, diagonals)
    for combo in [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]:
        # If all 3 buttons in this combo have the same text and are not empty
        if (buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != ""):
            # Highlight winning buttons in green
            for i in combo:
                buttons[i].config(bg="green")
            # Show popup message for winner
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True  # Stop further moves
            return

    # If all buttons filled and no winner, declare draw
    if all(button['text'] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True


# Function triggered when a button is clicked
def button_click(index):
    global winner
    # Only allow click if button is empty and no winner yet
    if buttons[index]["text"] == "" and not winner:
        # Mark current player's symbol on the button
        buttons[index]["text"] = current_player
        # Check if this move caused a win/draw
        check_winner()
        # If still no winner, switch player
        if not winner:
            toggle_player()


# Function to switch turn between X and O
def toggle_player():
    global current_player
    # Flip the player symbol
    current_player = "X" if current_player == "O" else "O"
    # Update label text for next player's turn
    label.config(text=f"Player {current_player}'s turn")


# ---------------------- GUI Setup ----------------------

root = tk.Tk()             # Create main window
root.title("Tic-Tac-Toe")  # Set window title

# Create 9 buttons for the tic-tac-toe board and store them in a list
buttons = [
    tk.Button(root, text="", font=('normal', 25), width=6, height=2,
              command=lambda i=i: button_click(i))   # Each button calls button_click with its index
    for i in range(9)
]

# Place the buttons in a 3x3 grid layout
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"  # Player X starts the game
winner = False        # No winner initially

# Label to show which player's turn it is
label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)  # Span across 3 columns below the board

root.mainloop()  # Run the Tkinter main event loop (keeps window open)


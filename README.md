Tic Tac Toe (Python Tkinter)
A simple Tic Tac Toe game built using Python's Tkinter library.
Two players can play alternately (X and O) on a 3x3 board. The game detects wins, draws, and allows restarting the game.

1. How to Run the Game
Requirements
Python 3.x installed on your system

Tkinter (comes pre-installed with Python on most systems)

Steps to Run
Save the code in a file named, for example:

Copy
Edit
tic_tac_toe.py
Open a terminal or command prompt in the folder where the file is saved.

Run the program using:

bash
Copy
Edit
python tic_tac_toe.py
The Tic Tac Toe window will appear.

2. How to Play
Player X always starts the game.

Click on any empty square to place your mark.

The game automatically switches turns between X and O.

A green highlight will appear on the winning combination if someone wins.

Use the New Game button to reset the board.

Click Exit to close the game.

3. Common Problems & Solutions
Problem	Cause	Solution
Window does not open when running the script	Python or Tkinter not installed properly	Ensure Python 3.x is installed. Tkinter comes by default. Run python --version to check.
Error: No module named 'tkinter'	Tkinter is missing on some Linux distributions	Install Tkinter:
Ubuntu/Debian: sudo apt install python3-tk
Fedora: sudo dnf install python3-tkinter
Game buttons are not clickable after first win	This is by design to prevent moves after game over	Click New Game to reset the board.
Window looks small or text overlaps	Screen scaling issue	Increase window.geometry("400x450") to a larger size.

4. Example Screenshot (Optional)
(You can add a screenshot of the running game here if you like.)

If you want, I can also add a Troubleshooting Tips section for Windows, Mac, and Linux separately to make it even more beginner-friendly.

Do you want me to add that?

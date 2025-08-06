# Tic Tac Toe (Python Tkinter)

A simple **Tic Tac Toe game** built using **Python's Tkinter** library.  
Two players can play alternately (X and O) on a 3x3 board. The game detects wins, draws, and allows restarting the game.

---

## 1. How to Run the Game

### **Requirements**
- Python 3.x installed on your system
- Tkinter (comes pre-installed with Python on most systems)

### **Steps to Run**
1. Save the code in a file named, for example:  
   ```
   tic_tac_toe.py
   ```
2. Open a terminal or command prompt in the folder where the file is saved.
3. Run the program using:
   ```bash
   python tic_tac_toe.py
   ```
4. The Tic Tac Toe window will appear.  

---

## 2. How to Play
1. Player **X** always starts the game.
2. Click on any empty square to place your mark.
3. The game automatically switches turns between **X** and **O**.
4. A **green highlight** will appear on the winning combination if someone wins.
5. Use the **New Game** button to reset the board.
6. Click **Exit** to close the game.

---

## 3. Common Problems & Solutions

| **Problem**                                   | **Cause**                                     | **Solution**                                      |
|-----------------------------------------------|-----------------------------------------------|---------------------------------------------------|
| Window does not open when running the script   | Python or Tkinter not installed properly       | Ensure Python 3.x is installed. Tkinter comes by default. Run `python --version` to check. |
| Error: `No module named 'tkinter'`             | Tkinter is missing on some Linux distributions | Install Tkinter: <br> **Ubuntu/Debian:** `sudo apt install python3-tk` <br> **Fedora:** `sudo dnf install python3-tkinter` |
| Game buttons are not clickable after first win | This is by design to prevent moves after game over | Click **New Game** to reset the board. |
| Window looks small or text overlaps            | Screen scaling issue                           | Increase `window.geometry("400x450")` to a larger size. |

---

## 4. Example Screenshot (Optional)
*(You can add a screenshot of the running game here if you like.)*

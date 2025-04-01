Mancala

A Python implementation of the classic board game Mancala, built using Pygame for our CS105 final project. This 2-player strategy game features a graphical user interface, capturing mechanics, and turn-based logic.

🧠 About the Game:

    Mancala is one of the oldest known board games. Players move stones around a board with the goal of collecting the most stones in their store. We implemented the "capture" mode, where players can capture stones from their opponent's side if certain conditions are met.

🛠️ How It Works:

    - The game board is stored as a Python dictionary, mapping hole names to stone counts.

    - Turn logic is handled in turns.py, which:

      - Validates legal moves

      - Handles stone distribution across the board

      - Tracks bonus moves and updates player stores

      - Implements the stealing mechanic
  
    - A command-line version of the game can be run using ASCII art from UI.py.

    - The interactive graphical interface uses Pygame, with clickable holes and real-time updates.

🧪 Challenges Faced:

    - Coding the circular movement of stones across the board for each player required a separate next_hole function.
    
    - Debugging the stealing logic revealed bugs in checking the opposite hole's content.
    
    - Learning the Pygame library from scratch, including how to handle mouse input and draw dynamic visuals.

📁 Files:

    - main.py: Controls game flow

    - turns.py: Handles player turns, logic, and capture rules

    - UI.py: Command-line UI for debugging

    - README.md: Project overview

🎮 Technologies Used:
  
    - Python 3

    - Pygame (for GUI)

👩‍💻 Contributors:

    - Lindsey Turner

    - Carter 

    - Emma

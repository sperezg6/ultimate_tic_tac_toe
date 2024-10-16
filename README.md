# Ultimate Tic-Tac-Toe

## Introduction
Ultimate Tic-Tac-Toe is an advanced version of the classic Tic-Tac-Toe game, implemented in Python. This implementation features a player versus AI gameplay, where the AI uses the Minimax algorithm with Alpha-Beta pruning to make intelligent moves.

## Features
- 3x3 grid of 3x3 Tic-Tac-Toe boards (9 sub-boards in total)
- Player vs AI gameplay
- Intelligent AI using Minimax algorithm with Alpha-Beta pruning
- Dynamic difficulty adjustment based on game state
- Graphical representation of the game board in the console

## Prerequisites
- Python 3.6 or higher

## Installation
1. Clone this repository or download the `tablero2.py` file.
2. Ensure you have Python installed on your system.

## How to Play
1. Run the script using Python:
   ```
   python tablero2.py
   ```
2. The game alternates between the human player (O) and the AI (X).
3. On your turn, you'll be prompted to enter coordinates for your move.
4. The game continues until one player wins or the game ends in a draw.

## Game Rules
1. The game is played on a 3x3 grid of 3x3 Tic-Tac-Toe boards.
2. Each turn, you must play in the sub-board corresponding to the cell of the previous move.
3. If a sub-board is won or full, you can choose any available sub-board for your next move.
4. To win the game, you must win three sub-boards in a row (horizontally, vertically, or diagonally).

## AI Implementation
The AI in this game uses the Minimax algorithm with Alpha-Beta pruning to determine the best move. Here's an overview of the key components:

1. **Minimax Algorithm**: This is a recursive algorithm that simulates all possible game states to determine the best move. It alternates between maximizing the AI's score and minimizing the player's score.

2. **Alpha-Beta Pruning**: This optimization technique reduces the number of nodes evaluated by the Minimax algorithm, making the AI faster and more efficient.

3. **Heuristic Evaluation**: The AI evaluates the game state using a heuristic function that considers:
   - The state of each sub-board
   - The overall state of the global board
   - Strategic positions (corners and center are valued higher)
   - Potential winning lines

4. **Depth-Limited Search**: The AI looks ahead a certain number of moves (default is 4) to balance between performance and decision quality.

## Functions Overview
- `imprimirTablero()`: Displays the current game state.
- `obtener_casilla(letra)`: Converts a letter input to a board position.
- `ha_ganado(subtablero, jugador)`: Checks if a player has won a sub-board.
- `actualizar_tablero_global(tablero_global, tableros)`: Updates the global board state.
- `mandar_coordenadas(macro, micro, jugador, tablero_global, tableros)`: Processes a move and updates the game state.
- `tablero_lleno(restriccion)`: Checks if a sub-board is full.
- `determinar_jugador(turno)`: Alternates between players based on the turn number.
- `minimax_alpha_beta(...)`: Implements the Minimax algorithm with Alpha-Beta pruning.
- `get_best_move(...)`: Determines the AI's best move.
- `heuristic_evaluation(...)`: Evaluates the game state for the AI.
- `jugar(tablero_global)`: Main game loop that manages the gameplay.

## Customization
You can adjust the AI's difficulty by modifying the `depth` parameter in the `get_best_move` function call within the `jugar` function. A higher depth will make the AI stronger but slower.

## Contributing
Contributions to improve the game or extend its features are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is open-source and available under the MIT License.

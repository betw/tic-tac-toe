Credit: CS50 staff (students implement "AI" tic-tac-toe agent that plays optimally)

This Tic Tac Toe game implementation in Python uses the Minimax algorithm to make optimal decisions for the two players, X and O. The game board is represented as a 3x3 grid, where each position can either be empty, marked by "X", or marked by "O". The game supports standard gameplay mechanics, including checking for horizontal, vertical, and diagonal wins, and detecting a full board, which results in a draw.

The minimax function drives the AI for both players, ensuring that "X" maximizes its chances of winning, while "O" minimizes "X"'s chances. The AI can play against itself or be used to challenge a human player. For added unpredictability, "O" can occasionally make random moves, though this randomness can be adjusted for a fully optimal gameplay experience.

Example usage:

```
board = initial_state()
while not terminal(board):
    move = minimax(board)
    board = result(board, move)
    print(board)
```
This code will simulate a game where the AI alternates between "X" and "O" making optimal moves. The minimax function ensures that the AI always plays the best possible move based on the current board state.


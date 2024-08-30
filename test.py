from tictactoe import player, actions, result, winner, terminal
import random

games = []

def make_game(games):
    game = [[None, None, None],
            [None, None, None],
            [None, None,None]]
    for r in range(len(game)):
        for c in range(len(game[0])):
            selected = random.randint(0,1)
            if selected == 0:
                game[r][c] = "X"
            elif selected == 1:
                game[r][c] = "O"
            #else:
             #   game[r][c] = None
    games.append(game)

for i in range(5):
    make_game(games)
games[1][2][0] = None
for i in range(len(games)):
    print(f"TEST {i}")
    print(games[i])
    print(terminal(games[i]))


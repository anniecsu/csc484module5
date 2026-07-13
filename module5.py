import numpy as np

# create 3 x 3 matrix
board = np.full((3, 3), " ")

# set player 1 as X and set how many moves are allowed
player = "X"
moves = 9

# create function to check for a win
def check_win(player):

    # check rows for win
    for row in board:
        if np.all(row == player):
            return True

    # check columns for win
    for col in board.T:
        if np.all(col == player):
            return True

    # check diagonals for win
    if np.all(np.diag(board) == player):
        return True

    if np.all(np.diag(np.fliplr(board)) == player):
        return True

    # return false if no win
    return False

# while 9 spots are not filled, continue the game
while moves > 0:
    print(board)

    # prompt player to put their move
    row = int(input(f"Which row for Player {player} (0-2)? "))
    col = int(input(f"Which column for Player {player} (0-2)? "))

    # check that the spot is empty before placing the move
    if board[row][col] != " ":
        print("Spot is taken, please try again")
        continue

    # remove one move
    board[row][col] = player
    moves -= 1

    # check if any player has won the game
    if check_win(player):
        print(board)
        print(f"Player {player} wins this game")
        break

    # if not winning yet, change the player
    if player == "X":
        player = "O"
    else:
        player = "X"

# check for a draw
if moves == 0 and not check_win("X") and not check_win("O"):
    print(board)
    print("Game is a draw")
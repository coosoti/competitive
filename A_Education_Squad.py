def count_victories(board):
    # Count individual victories and team victories
    individual_victories = 0
    team_victories = 0

    # Check rows and columns for individual and team victories
    for i in range(3):
        if len(set(board[i])) == 1:  # Individual victory
            individual_victories += 1
        if len(set([board[0][i], board[1][i], board[2][i]])) == 2:  # Team victory in column
            team_victories += 1
        if len(set([board[i][0], board[i][1], board[i][2]])) == 2:  # Team victory in row
            team_victories += 1

    # Check diagonals for team victories
    if len(set([board[0][0], board[1][1], board[2][2]])) == 2:  # Team victory in diagonal
        team_victories += 1
    if len(set([board[0][2], board[1][1], board[2][0]])) == 2:  # Team victory in diagonal
        team_victories += 1

    return individual_victories, team_victories


if __name__ == "__main__":
    # Read the board
    board = [input() for _ in range(3)]

    # Count individual and team victories
    individual_victories, team_victories = count_victories(board)

    # Print the results
    print(individual_victories)
    print(team_victories)

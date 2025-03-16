#!/usr/bin/python3

def print_board(board):
    # Print the current board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Initialize an empty board
    player = "X"

    # Game loop continues until there is a winner
    while not check_winner(board):
        print_board(board)

        # Handle input validation for row
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2]:
                print("Invalid row. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number for row.")
            continue

        # Handle input validation for column
        try:
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if col not in [0, 1, 2]:
                print("Invalid column. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number for column.")
            continue

        # Check if the spot is empty and place the mark
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):  # Check if this move wins the game
                break
            player = "O" if player == "X" else "X"  # Switch player
        else:
            print("That spot is already taken! Try again.")

    # Final board and winner announcement
    print_board(board)
    print("Player " + player + " wins!")

# Start the game
tic_tac_toe()


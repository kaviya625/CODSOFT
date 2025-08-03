import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    return (board[0][0] == board[1][1] == board[2][2] == player or
            board[0][2] == board[1][1] == board[2][0] == player)

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O.")
    print_board(board)

    while True:
        row = int(input("Enter your row (0-2): "))
        col = int(input("Enter your col (0-2): "))
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"

        print_board(board)

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()

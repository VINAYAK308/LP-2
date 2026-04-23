def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve(row, board, n):
    # Base case: all queens placed
    if row == n:
        for r in board:
            print("".join(r))
        print("------------------")
        return

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'   # place queen
            solve(row + 1, board, n)
            board[row][col] = '.'   # backtrack


def main():
    n = 4
    board = [['.' for _ in range(n)] for _ in range(n)]

    solve(0, board, n)


if __name__ == "__main__":
    main()

# python3 Assignment4.py
# .Q..
# ...Q
# Q...
# ..Q.
# ------------------
# ..Q.
# Q...
# ...Q
# .Q..
# ------------------
 
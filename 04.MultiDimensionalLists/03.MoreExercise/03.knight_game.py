def count_attacks(matrix, row, col, size):
    moves = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    return sum(
        1 for dr, dc in moves if 0 <= row + dr < size and 0 <= col + dc < size and matrix[row + dr][col + dc] == "K")


n = int(input())  
board = [list(input()) for _ in range(n)]
removed_knights = 0

while True:
    max_attacks = 0
    best_position = None

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                attacks = count_attacks(board, r, c, n)
                if attacks > max_attacks:
                    max_attacks = attacks
                    best_position = (r, c)

    if max_attacks == 0:
        break

    r, c = best_position
    board[r][c] = "0"
    removed_knights += 1

print(removed_knights)

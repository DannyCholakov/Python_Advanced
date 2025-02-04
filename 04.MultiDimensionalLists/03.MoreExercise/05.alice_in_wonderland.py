def find_position(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol:
                return row, col
    return None

def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size

n = int(input())
matrix = [list(input().split()) for _ in range(n)]

alice_row, alice_col = find_position(matrix, 'A')
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix[alice_row][alice_col] = '*'

while tea_bags < 10:
    command = input()

    if command not in directions:
        continue

    move_row, move_col = directions[command]
    new_row, new_col = alice_row + move_row, alice_col + move_col

    if not is_valid_position(new_row, new_col, n):
        break

    cell = matrix[new_row][new_col]

    if cell == 'R':
        matrix[new_row][new_col] = '*'
        break

    elif cell.isdigit():
        tea_bags += int(cell)

    matrix[new_row][new_col] = '*'
    alice_row, alice_col = new_row, new_col

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(" ".join(row))

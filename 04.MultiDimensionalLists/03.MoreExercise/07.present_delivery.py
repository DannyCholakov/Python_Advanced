def find_position(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol:
                return row, col
    return None

def is_valid_position(row, col, size):
    return 0 <= row < size and 0 <= col < size

def deliver_presents(row, col):
    global presents
    for dr, dc in directions.values():
        new_row, new_col = row + dr, col + dc
        if is_valid_position(new_row, new_col, size) and matrix[new_row][new_col] in {"V", "X"}:
            if matrix[new_row][new_col] == "V":
                nice_kids_with_presents.add((new_row, new_col))
            matrix[new_row][new_col] = "-"
            presents -= 1
            if presents == 0:
                return

presents = int(input())
size = int(input())
matrix = [input().split() for _ in range(size)]

santa_pos = find_position(matrix, "S")
matrix[santa_pos[0]][santa_pos[1]] = "-"

total_nice_kids = sum(row.count("V") for row in matrix)
nice_kids_with_presents = set()

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    move_row, move_col = directions[command]
    santa_pos = (santa_pos[0] + move_row, santa_pos[1] + move_col)
    row, col = santa_pos

    if matrix[row][col] == "V":
        nice_kids_with_presents.add((row, col))
        presents -= 1

    elif matrix[row][col] == "C":
        deliver_presents(row, col)

    matrix[row][col] = "-"

    if presents == 0:
        break

matrix[santa_pos[0]][santa_pos[1]] = "S"

if presents == 0 and len(nice_kids_with_presents) < total_nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if len(nice_kids_with_presents) == total_nice_kids:
    print(f"Good job, Santa! {len(nice_kids_with_presents)} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - len(nice_kids_with_presents)} nice kid/s.")

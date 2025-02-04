def find_position(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol:
                return row, col
    return None


def is_valid_position(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def move(position, direction, steps):
    row, col = position
    dr, dc = directions[direction]
    for _ in range(steps):
        new_row, new_col = row + dr, col + dc
        if not is_valid_position(new_row, new_col) or matrix[new_row][new_col] != ".":
            return row, col  # Stop moving if out of bounds or blocked
        row, col = new_row, new_col
    return row, col


def shoot(position, direction):
    row, col = position
    dr, dc = directions[direction]
    while is_valid_position(row + dr, col + dc):
        row += dr
        col += dc
        if matrix[row][col] == "x":
            matrix[row][col] = "."  # Mark target as hit
            return [row, col]
    return None


matrix = [input().split() for _ in range(5)]
n = int(input())

player_pos = find_position(matrix, "A")
matrix[player_pos[0]][player_pos[1]] = "."

directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

total_targets = sum(row.count("x") for row in matrix)
hit_targets = []

for _ in range(n):
    command = input().split()
    action, direction = command[0], command[1]

    if action == "move":
        steps = int(command[2])
        player_pos = move(player_pos, direction, steps)

    elif action == "shoot":
        target_hit = shoot(player_pos, direction)
        if target_hit:
            hit_targets.append(target_hit)
            total_targets -= 1
            if total_targets == 0:
                break

if total_targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

for target in hit_targets:
    print(target)

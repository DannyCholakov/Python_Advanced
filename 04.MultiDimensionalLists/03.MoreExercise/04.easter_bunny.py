def find_bunny(field, size):
    for r in range(size):
        for c in range(size):
            if field[r][c] == "B":
                return r, c


def collect_eggs(field, start_r, start_c, direction, size):
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    eggs = 0
    path = []
    dr, dc = moves[direction]
    r, c = start_r + dr, start_c + dc

    while 0 <= r < size and 0 <= c < size and field[r][c] != "X":
        eggs += int(field[r][c])
        path.append([r, c])
        r += dr
        c += dc

    return eggs, path


size = int(input())
field = [input().split() for _ in range(size)]
bunny_r, bunny_c = find_bunny(field, size)

best_direction = None
max_eggs = 0
best_path = []

for direction in ["up", "down", "left", "right"]:
    eggs, path = collect_eggs(field, bunny_r, bunny_c, direction, size)
    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_path = path

print(best_direction)
for pos in best_path:
    print(pos)
print(max_eggs)

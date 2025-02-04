def read_matrix(n):
    return [list(map(int, input().split())) for _ in range(n)]


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


n = int(input())
matrix = read_matrix(n)

while True:
    command = input()
    if command == "END":
        break
    parts = command.split()
    action, row, col, value = parts[0], int(parts[1]), int(parts[2]), int(parts[3])

    if 0 <= row < n and 0 <= col < n:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

print_matrix(matrix)

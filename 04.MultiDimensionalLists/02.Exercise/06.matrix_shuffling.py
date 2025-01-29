rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    parts = command.split()
    if parts[0] != "swap" or len(parts) != 5:
        print("Invalid input!")
        continue
    r1, c1, r2, c2 = map(int, parts[1:])
    if not (0 <= r1 < rows and 0 <= c1 < cols and 0 <= r2 < rows and 0 <= c2 < cols):
        print("Invalid input!")
        continue

    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
    for row in matrix:
        print(" ".join(row))
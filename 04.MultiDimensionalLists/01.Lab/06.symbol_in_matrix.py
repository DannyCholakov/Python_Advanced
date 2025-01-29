n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()

found = False

for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break
else:
    print(f"{symbol} does not occur in the matrix")

rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = float('-inf')
best_square = []

for r in range(rows - 2):
    for c in range(cols - 2):
        square = [matrix[r][c:c+3], matrix[r+1][c:c+3], matrix[r+2][c:c+3]]
        current_sum = sum(sum(row) for row in square)
        if current_sum > max_sum:
            max_sum = current_sum
            best_square = square

print(f"Sum = {max_sum}")
for row in best_square:
    print(" ".join(map(str, row)))
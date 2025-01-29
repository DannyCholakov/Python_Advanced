rows, cols = map(int, input().split(", "))

matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

max_sum = float('-inf')
best_submatrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        submatrix = [
            [matrix[row][col], matrix[row][col + 1]],
            [matrix[row + 1][col], matrix[row + 1][col + 1]]
        ]
        submatrix_sum = sum(sum(submatrix, []))  # Flatten and sum

        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            best_submatrix = submatrix

for row in best_submatrix:
    print(*row)

print(max_sum)

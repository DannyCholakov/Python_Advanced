rows, cols = map(int, input().split(", "))

matrix = [list(map(int, input().split())) for _ in range(rows)]

for col in range(cols):
    column_sum = sum(matrix[row][col] for row in range(rows))
    print(column_sum)

rows, cols = map(int, input().split(", "))

matrix = []
total_sum = 0

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    total_sum += sum(row)
    matrix.append(row)

print(total_sum)
print(matrix)

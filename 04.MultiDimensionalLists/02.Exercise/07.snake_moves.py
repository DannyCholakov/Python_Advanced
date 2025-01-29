rows, cols = map(int, input().split())
snake = input()

matrix = []
index = 0
for r in range(rows):
    row = [snake[index % len(snake)] for index in range(index, index + cols)]
    if r % 2 == 1:
        row.reverse()
    matrix.append(row)
    index += cols

for row in matrix:
    print("".join(row))

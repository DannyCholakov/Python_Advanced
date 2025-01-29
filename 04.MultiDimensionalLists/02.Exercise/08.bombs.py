def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def detonate_bombs(matrix, bombs, n):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for bomb in bombs:
        r, c = map(int, bomb.split(","))
        if matrix[r][c] > 0:
            power = matrix[r][c]
            matrix[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc, n) and matrix[nr][nc] > 0:
                    matrix[nr][nc] -= power


def count_alive_cells(matrix):
    alive_cells = sum(1 for row in matrix for cell in row if cell > 0)
    sum_of_alive = sum(cell for row in matrix for cell in row if cell > 0)
    return alive_cells, sum_of_alive


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs = input().split()

detonate_bombs(matrix, bombs, n)
alive_cells, sum_of_alive = count_alive_cells(matrix)

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive}")
for row in matrix:
    print(" ".join(map(str, row)))

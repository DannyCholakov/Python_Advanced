n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

diagonal_sum = sum(matrix[i][i] for i in range(n))

print(diagonal_sum)

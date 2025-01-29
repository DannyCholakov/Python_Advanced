rows = int(input())

flattened = [
    num
    for _ in range(rows)
    for num in map(int, input().split(", "))
]

print(flattened)

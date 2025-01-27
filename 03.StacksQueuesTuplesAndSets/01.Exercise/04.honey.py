from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectar:
    bee = bees[0]
    nectar_amount = nectar.pop()

    # If nectar is not enough, skip this iteration
    if nectar_amount < bee:
        continue

    # Remove the bee after nectar is enough
    bees.popleft()
    symbol = symbols.popleft()

    # Perform the operation based on the symbol
    if symbol == "+":
        total_honey += abs(bee + nectar_amount)
    elif symbol == "-":
        total_honey += abs(bee - nectar_amount)
    elif symbol == "*":
        total_honey += abs(bee * nectar_amount)
    elif symbol == "/":
        if nectar_amount != 0:
            total_honey += abs(bee // nectar_amount)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")

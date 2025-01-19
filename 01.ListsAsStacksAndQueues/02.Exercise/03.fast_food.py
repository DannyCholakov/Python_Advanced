food_quantity = int(input())
orders = list(map(int, input().split()))
queue = orders[:]

print(max(orders))

while queue:
    if food_quantity >= queue[0]:
        food_quantity -= queue.pop(0)
    else:
        break

if not queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, queue))}")

from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pumps.append(tuple(map(int, input().split())))

for i in range(n):
    fuel = 0
    completed = True
    for petrol, distance in pumps:
        fuel += petrol - distance
        if fuel < 0:
            completed = False
            break
    if completed:
        print(i)
        break
    pumps.append(pumps.popleft())

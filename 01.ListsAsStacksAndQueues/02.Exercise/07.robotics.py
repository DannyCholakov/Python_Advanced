from collections import deque
from datetime import datetime, timedelta

robots_input = input().split(';')
start_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

robots = []
for robot in robots_input:
    name, time = robot.split('-')
    robots.append({'name': name, 'time': int(time), 'available_at': start_time})

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_time = start_time

while products:
    current_time += timedelta(seconds=1)
    product = products.popleft()

    free_robot = None
    for robot in robots:
        if robot['available_at'] <= current_time:
            free_robot = robot
            break

    if free_robot:
        free_robot['available_at'] = current_time + timedelta(seconds=free_robot['time'])
        print(f"{free_robot['name']} - {product} [{current_time.strftime('%H:%M:%S')}]")
    else:
        products.append(product)

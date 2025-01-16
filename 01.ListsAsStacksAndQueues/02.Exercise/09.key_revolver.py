from collections import deque
from datetime import datetime, timedelta


def robotics_simulation(robots_data, start_time, products):
    robots = []
    busy_until = {}

    for data in robots_data.split(";"):
        name, time = data.split("-")
        robots.append((name, int(time)))
        busy_until[name] = datetime.strptime(start_time, "%H:%M:%S")

    queue = deque(products)
    current_time = datetime.strptime(start_time, "%H:%M:%S")

    while queue:
        current_time += timedelta(seconds=1)
        product = queue.popleft()

        for name, time in robots:
            if current_time >= busy_until[name]:
                busy_until[name] = current_time + timedelta(seconds=time)
                print(f"{name} - {product} [{current_time.strftime('%H:%M:%S')}]")
                break
        else:
            queue.append(product)


# Example usage:
robots_data = "ROB-15;SS2-10;NX8000-3"
start_time = "08:00:00"
products = ["detail", "glass", "wood", "apple", "End"]
robotics_simulation(robots_data, start_time, [p for p in products if p != "End"])

from collections import deque

def water_dispenser():
    water_quantity = int(input())
    queue = deque()

    while True:
        command = input()
        if command == "Start":
            break
        queue.append(command)

    while True:
        command = input()
        if command == "End":
            print(f"{water_quantity} liters left")
            break

        if command.startswith("refill"):
            _, liters = command.split()
            water_quantity += int(liters)
        else:
            liters = int(command)
            person = queue.popleft()
            if liters <= water_quantity:
                water_quantity -= liters
                print(f"{person} got water")
            else:
                print(f"{person} must wait")

water_dispenser()

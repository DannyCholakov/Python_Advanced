from collections import deque

def traffic_simulation():
    green_light_duration = int(input())
    free_window_duration = int(input())

    car_queue = deque()
    total_cars_passed = 0

    while True:
        command = input()
        if command == "END":
            print("Everyone is safe.")
            print(f"{total_cars_passed} total cars passed the crossroads.")
            break

        if command == "green":
            current_green = green_light_duration

            while car_queue and current_green > 0:
                car = car_queue.popleft()

                if len(car) <= current_green:
                    current_green -= len(car)
                    total_cars_passed += 1
                else:
                    remaining_time = current_green + free_window_duration
                    if len(car) <= remaining_time:
                        total_cars_passed += 1
                        break
                    else:
                        crash_index = current_green + free_window_duration
                        print("A crash happened!")
                        print(f"{car} was hit at {car[crash_index]}.")
                        return

        else:
            car_queue.append(command)

traffic_simulation()

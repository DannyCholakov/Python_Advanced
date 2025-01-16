def truck_tour(pumps):
    start_index = 0
    total_petrol = 0
    current_petrol = 0

    for i in range(len(pumps)):
        petrol, distance = pumps[i]
        total_petrol += petrol - distance
        current_petrol += petrol - distance

        if current_petrol < 0:
            start_index = i + 1
            current_petrol = 0

    return start_index

# Example usage:
pumps = [
    (1, 5),
    (10, 3),
    (3, 4)
]
print(truck_tour(pumps))  # Output: 1

pumps = [
    (22, 5),
    (14, 10),
    (52, 7),
    (21, 12),
    (36, 9)
]
print(truck_tour(pumps))  # Output: 0

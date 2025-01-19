clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 1
current_capacity = rack_capacity

while clothes:
    cloth = clothes.pop()
    if current_capacity >= cloth:
        current_capacity -= cloth
    else:
        racks += 1
        current_capacity = rack_capacity - cloth

print(racks)

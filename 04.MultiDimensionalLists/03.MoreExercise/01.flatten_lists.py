data = input().split("|")
flattened_list = []

for sublist in reversed(data):
    numbers = sublist.split()
    flattened_list.extend(numbers)

print(" ".join(flattened_list))

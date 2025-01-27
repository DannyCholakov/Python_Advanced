numbers = list(map(float, input().split()))
occurrences = {}

for num in numbers:
    formatted_num = round(num, 1)
    occurrences[formatted_num] = occurrences.get(formatted_num, 0) + 1

for number, count in occurrences.items():
    print(f"{number} - {count} times")

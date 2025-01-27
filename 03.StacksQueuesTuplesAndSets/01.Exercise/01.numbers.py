first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command_parts = input().split()
    command = command_parts[0] + " " + command_parts[1]
    numbers = map(int, command_parts[2:])

    if command == "Add First":
        first_sequence.update(numbers)
    elif command == "Add Second":
        second_sequence.update(numbers)
    elif command == "Remove First":
        first_sequence.difference_update(numbers)
    elif command == "Remove Second":
        second_sequence.difference_update(numbers)
    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(", ".join(map(str, sorted(first_sequence))))
print(", ".join(map(str, sorted(second_sequence))))

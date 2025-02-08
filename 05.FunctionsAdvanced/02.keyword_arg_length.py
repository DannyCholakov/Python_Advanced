def kwargs_length(**kwargs):
    return len(kwargs)

num_entries = int(input())

dictionary = {}

for _ in range(num_entries):
    key = input()
    value = input()
    dictionary[key] = value

# Call the function and print the result
print(kwargs_length(**dictionary))

def reverse_string_with_stack(input_string):
    stack = []

    for char in input_string:
        stack.append(char)

    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string


input_string = input()

result = reverse_string_with_stack(input_string)

print(result)

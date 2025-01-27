from collections import deque
from math import floor

expression = input().split()
numbers = deque()

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        numbers.append(int(token))
    else:
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()

            if token == "+":
                result = first + second
            elif token == "-":
                result = first - second
            elif token == "*":
                result = first * second
            elif token == "/":
                result = floor(first / second)

            numbers.appendleft(result)

print(numbers[0])

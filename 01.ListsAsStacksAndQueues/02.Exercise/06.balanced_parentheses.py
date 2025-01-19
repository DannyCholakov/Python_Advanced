sequence = input()
stack = []
pairs = {'(': ')', '{': '}', '[': ']'}

balanced = True
for char in sequence:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack or pairs[stack.pop()] != char:
            balanced = False
            break

print("YES" if balanced and not stack else "NO")

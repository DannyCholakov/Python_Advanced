def balanced_parentheses(sequence):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return "NO"
    return "YES" if not stack else "NO"


# Example usage:
sequences = [
    "{[()]}",
    "{[(])}",
    "{{[[(())]]}}"
]
for seq in sequences:
    print(balanced_parentheses(seq))

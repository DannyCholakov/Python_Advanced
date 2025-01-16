def extract_parentheses(expression):
    stack = []
    results = []

    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            start_index = stack.pop()
            results.append(expression[start_index:i + 1])

    return results


expression = input()

parentheses_sets = extract_parentheses(expression)
for parens in parentheses_sets:
    print(parens)

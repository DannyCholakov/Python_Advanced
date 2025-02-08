def math_operations(*numbers, a=0, s=0, d=0, m=0):
    ops = {'a': a, 's': s, 'd': d, 'm': m}
    operations = ['a', 's', 'd', 'm']

    for i, num in enumerate(numbers):
        key = operations[i % 4]  # Cycle through 'a', 's', 'd', 'm'
        if key == 'a':
            ops[key] += num
        elif key == 's':
            ops[key] -= num
        elif key == 'd':
            if num != 0:  # Avoid division by zero
                ops[key] /= num
        elif key == 'm':
            ops[key] *= num

    # Sort by values in descending order, then by keys alphabetically
    sorted_result = sorted(ops.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f"{k}: {v:.1f}" for k, v in sorted_result)

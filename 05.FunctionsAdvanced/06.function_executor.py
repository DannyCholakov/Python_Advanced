def func_executor(*functions):
    results = []
    for func, args in functions:
        result = func(*args)
        results.append(f"{func.__name__} - {result}")
    return "\n".join(results)
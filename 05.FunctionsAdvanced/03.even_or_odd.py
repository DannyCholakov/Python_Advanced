def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    return [n for n in numbers if n % 2 == 0] if command == "even" else [n for n in numbers if n % 2 != 0]

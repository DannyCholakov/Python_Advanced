def even_odd_filter(**kwargs):
    for key in kwargs:
        if key == "even":
            kwargs[key] = [n for n in kwargs[key] if n % 2 == 0]
        elif key == "odd":
            kwargs[key] = [n for n in kwargs[key] if n % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

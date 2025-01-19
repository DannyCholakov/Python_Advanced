def cups_and_bottles():
    cups = list(map(int, input().split()))
    bottles = list(map(int, input().split()))

    wasted_water = 0
    while cups and bottles:
        cup = cups[0]
        bottle = bottles[-1]

        if bottle >= cup:
            wasted_water += bottle - cup
            bottles.pop()
            cups.pop(0)
        else:
            cups[0] -= bottle
            bottles.pop()

    if cups:
        print(f"Cups: {' '.join(map(str, cups))}")
    else:
        print(f"Bottles: {' '.join(map(str, bottles))}")

    print(f"Wasted litters of water: {wasted_water}")

cups_and_bottles()

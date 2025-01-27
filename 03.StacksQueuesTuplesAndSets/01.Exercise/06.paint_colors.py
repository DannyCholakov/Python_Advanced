substrings = input().split()

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
color_requirements = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

found_colors = []

while substrings:
    first = substrings.pop(0)
    last = substrings.pop() if substrings else ""

    color = first + last
    reversed_color = last + first

    if color in main_colors or color in secondary_colors:
        found_colors.append(color)
    elif reversed_color in main_colors or reversed_color in secondary_colors:
        found_colors.append(reversed_color)
    else:
        first = first[:-1]
        last = last[:-1]
        if first:
            substrings.insert(len(substrings) // 2, first)
        if last:
            substrings.insert(len(substrings) // 2, last)

verified_colors = []
for color in found_colors:
    if color in main_colors:
        verified_colors.append(color)
    elif color in secondary_colors:
        if color_requirements[color].issubset(found_colors):
            verified_colors.append(color)

print(verified_colors)

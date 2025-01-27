from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

present_magic = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_presents = {}

while materials and magic:
    material = materials.pop()
    mag = magic.popleft()

    if material == 0 and mag == 0:
        continue
    if material == 0:
        magic.appendleft(mag)
        continue
    if mag == 0:
        materials.append(material)
        continue

    total_magic = material * mag

    if total_magic in present_magic:
        present = present_magic[total_magic]
        crafted_presents[present] = crafted_presents.get(present, 0) + 1
    elif total_magic < 0:
        materials.append(material + mag)
    else:
        materials.append(material + 15)

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
        ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for present, amount in sorted(crafted_presents.items()):
    print(f"{present}: {amount}")

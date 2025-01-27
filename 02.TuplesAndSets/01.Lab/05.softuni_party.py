n = int(input())
reservation_list = set()

for _ in range(n):
    reservation_list.add(input())

while True:
    guest = input()
    if guest == "END":
        break
    reservation_list.discard(guest)

vip_guests = sorted([guest for guest in reservation_list if guest[0].isdigit()])
regular_guests = sorted([guest for guest in reservation_list if not guest[0].isdigit()])

print(len(vip_guests) + len(regular_guests))
print("\n".join(vip_guests + regular_guests))

n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(char) for char in name)
    result = ascii_sum // row

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum == even_sum:
    print(", ".join(map(str, odd_set | even_set)))
elif odd_sum > even_sum:
    print(", ".join(map(str, odd_set - even_set)))
else:
    print(", ".join(map(str, odd_set ^ even_set)))

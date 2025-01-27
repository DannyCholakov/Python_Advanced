text = input()

symbol_count = {}
for char in text:
    symbol_count[char] = symbol_count.get(char, 0) + 1

for char in sorted(symbol_count):
    print(f"{char}: {symbol_count[char]} time/s")

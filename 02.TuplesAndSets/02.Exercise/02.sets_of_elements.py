n, m = map(int, input().split())
set1 = {input() for _ in range(n)}
set2 = {input() for _ in range(m)}

intersection = set1 & set2
print("\n".join(intersection))

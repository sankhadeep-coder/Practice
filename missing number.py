l = list(map(int, input().split()))

n = len(l)

expected = n * (n + 1) // 2
actual = sum(l)

missing = expected - actual

print(missing)
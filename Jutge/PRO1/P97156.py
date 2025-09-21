a, b = map(int, input().split())

while a <= b:
    if a < b:
        print(f"{a},", end="")
    else:
        print(f"{a}", end="")
    a += 1

print()
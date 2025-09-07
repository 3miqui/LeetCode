x, a, b, c, d = map(int, input().split())

if x in range(a, b + 1) or x in range(c, d + 1):
    print("si")
else:
    print("no")

a1, b1, a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    print("=", ",", f"[{a1},{b1}]")
elif a1 >= a2 and b1 <= b2:
    print("1", ",", f"[{a1},{b1}]")
elif a1 <= a2 and b1 >= b2:
    print("2", ",", f"[{a2},{b2}]")
elif max(a1, a2) <= min(b1, b2):
    start = max(a1, a2)
    end = min(b1, b2)
    print("?", ",", f"[{start},{end}]")
else:
    print("?", ",", "[]")

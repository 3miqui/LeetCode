x, y = map(int, input().split())

if y >= x:
    while x <= y:
        print(y)
        y = y - 1
    
else: 
    while y <= x:
        print(x)
        x = x - 1

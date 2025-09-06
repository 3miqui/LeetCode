hores, minuts, segons = map(int, input().split())

segons = segons + 1

if segons > 59:
    minuts = minuts + 1
    segons = 00
    
if minuts > 59:
    hores = hores + 1
    minuts = 00
    
    
if hores > 23:
    hores = 00
    
    print(f"{hores:02}:{minuts:02}:{segons:02}")
    
else:  
    print(f"{hores:02}:{minuts:02}:{segons:02}")
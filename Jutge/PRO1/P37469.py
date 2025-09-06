segons = int(input())

minuts = segons // 60
residu = segons % 60

if minuts >= 60:
    hores = minuts // 60
    residu2 = minuts % 60
    print(hores, residu2, residu)
else:
    hores = 0
    print(hores, minuts, residu)
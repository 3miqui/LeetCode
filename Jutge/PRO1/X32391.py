d, n, t = map(int, input().split())

saldo_acumulat = 0
comptador = 0

for _ in range(t):
    a = int(input())  
    saldo_acumulat += (a - d)  
    if saldo_acumulat + n > 0:
        comptador += 1

print(comptador)
n = int(input())
suma = 0
cont = 0

while n // 10 > 0:
    if n % 10 == 0 and suma == 0:
        cont += 1
    suma += n % 10
    suma = suma * 10 
    n = n // 10

suma += n

for i in range(0, cont):
    print("0", end="")
    
print(suma)
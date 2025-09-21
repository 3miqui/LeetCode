n = int(input())
original = n
contador = 0

for i in range(100):
    if n == 0 and contador == 0:
        contador = 1
        break
    elif n == 0:
        break
    n = n // 10
    contador += 1

print("El nombre de digits de", original, "es", str(contador) + ".", sep=" ")

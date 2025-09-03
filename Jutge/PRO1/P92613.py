y = float(input())

entero_menor = int(y)
entero_mayor = 0
redondeo = 0

if (y - entero_menor > 0):
    entero_mayor = entero_menor + 1
else:
    entero_mayor = entero_menor

if (y - entero_menor) >= 0.5:
    redondeo = entero_mayor
else:
    redondeo = entero_menor
    
print(entero_menor, entero_mayor, redondeo)
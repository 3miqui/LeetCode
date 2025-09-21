k = int(input())
base_max = 16  

for base in range(2, base_max + 1):
    aux = k
    contador = 0

    if aux == 0:
        contador = 1
    else:
        while aux > 0:
            aux = aux // base
            contador += 1

    print(f"Base {base}: {contador} cifras.")

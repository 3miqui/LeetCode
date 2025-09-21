import math

cantidad = int(input())

entradas = [input() for _ in range(cantidad)]

i = 0
while i < cantidad:
    entrada = entradas[i]
    partes = entrada.split()

    if partes[0] == "cercle":
        n = float(partes[1])
        while True:
            n = n ** 2
            n = n * math.pi
            print("%.6f" % n)
            break

    elif partes[0] == "rectangle":
        n = float(partes[1])
        t = float(partes[2])
        while True:
            resultado = n * t
            print("%.6f" % resultado)
            break

    i += 1
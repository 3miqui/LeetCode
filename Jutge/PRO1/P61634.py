año = int(input())

# año % 4 == 0 and año % 100 != 0 -> Los dos ultimos numeros son 0 y es divisible por 4.
# Si el residuo de un número / 100 = 0, entonces acaba siempre por dos 0.
# Si el residuo de un número / 4 = 0, entonces el número es divisible por 4.

# año / 100 % 4 -> El número acaba con dos 0s, pero lo que sigue es divisible por 4.
# Un numero / 100 da como resultado ese número sin los dos ultimos digitos.
# Lo que queda se divide entre 4, si el residuo = 0 entonces es divisible por 4.

# El año 2000 deberia no ser viciesto, pero lo pone en el enunciado que si que es.

if (año % 4 == 0 and año % 100 != 0) or (año / 100 % 4 == 0) or año == 2000: 
    print("YES")
else:
    print("NO")


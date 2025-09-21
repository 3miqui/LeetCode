numero = int(input())


invertido = 0
temp = numero
while temp > 0:
    digito = temp % 10
    invertido = invertido * 10 + digito
    temp = temp // 10


binario = ""
if invertido == 0:
    binario = "0"
else:
    while invertido > 0:
        resto = invertido % 2
        binario = str(resto) + binario
        invertido = invertido // 2

print(binario)


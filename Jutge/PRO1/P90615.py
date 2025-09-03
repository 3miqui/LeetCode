number1, number2, number3 = map(int, input().split())

if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else: 
    print(number3)
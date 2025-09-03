first_number, second_number = map(float, input().split())

average = (first_number + second_number) / 2
if average.is_integer():
    print(int(average))
else:
    print(average)
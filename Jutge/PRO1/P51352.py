input1, input2 = input().split()

if input1 == "A" and input2 == "P":
    print("1")
elif input1 == "P" and input2 == "V":
     print("1")
elif input1 == "V" and input2 == "A":
     print("1")
elif input2 == "A" and input1 == "P":
    print("2")
elif input2 == "P" and input1 == "V":
    print("2")
elif input2 == "V" and input1 == "A":
    print("2")
else: 
    print("-")
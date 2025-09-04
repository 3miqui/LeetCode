letter = input()

if letter.isupper():
    print("majuscula")
elif letter.islower():
    print("minuscula")
    
if letter in ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U"):
    print("vocal")
else:
    print("consonant")

word1 = input()
word2 = input()

if len(word1) > len(word2):
    print(word1,">",word2)
elif len(word1) < len(word2):
    print(word1,"<",word2)
else:
    print(word1,"=",word2)

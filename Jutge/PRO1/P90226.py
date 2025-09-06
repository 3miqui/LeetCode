word1, word2 = input().split()

if word1 > word2:
    print(word1, ">", word2)
elif word1 < word2:
    print(word1, "<", word2)
else:
    print(word1, "=", word2)

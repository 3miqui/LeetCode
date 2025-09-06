anys, dies, hores, minuts, segons = map(int, input().split())

print(anys * 31536000 + dies * 86400 + hores * 3600 + minuts * 60 + segons * 1)
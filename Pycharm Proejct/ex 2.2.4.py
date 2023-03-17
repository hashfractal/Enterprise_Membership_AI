res = 0

while(True):
    n = int(input())
    if n >= 0:
        res += n
    else:
        break

print(res)
n = int(input())
i = 0
height = 100
while(i < n):
    height = height * 0.6
    print(i + 1, round(height, 4))
    i += 1
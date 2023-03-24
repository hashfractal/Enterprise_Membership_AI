n = int(input())
count = 0
res = []

for i in range(2, n + 1):
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1

    if count == 1:
        res.append(i)
    count = 0

print(res)
def sumOfDigits(num):
    res = 0
    for i in str(num):
        res += int(i)

    print(res)

sumOfDigits(643)
sumOfDigits(47253)
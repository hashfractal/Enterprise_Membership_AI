n = int(input())
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("윤년")
        else:
            print("평년")
    else:
        print("평년")
else:
    print("평년")
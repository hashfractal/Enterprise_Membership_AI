from datetime import datetime

def korean_age(n):
    strs = input("Are you Korean?(y/n): ").lower()
    mm = int(input("Input your birthday montn(MM): "))
    dd = int(input("Input your birthday day(DD): "))
    match strs:
        case "y":
            return datetime.today().year - n + 1
        case "n":
            return  (datetime(1,1,1) + (datetime.today() - datetime(n, mm, dd))).year - 1

print(korean_age(2021))
from datetime import datetime

def korean_age(n):
    return datetime.today().year - n + 1

print(korean_age(1992))
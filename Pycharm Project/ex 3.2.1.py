def korean_number(n):
    match(n):
        case (1):
            print("일")
        case (2):
            print("이")
        case (3):
            print("삼")
        case (4):
            print("사")
        case (5):
            print("오")
        case (6):
            print("륙")
        case (7):
            print("칠")
        case (8):
            print("팔")
        case (9):
            print("구")
        case (10):
            print("십")

for i in range(1, 11):
    korean_number(i)
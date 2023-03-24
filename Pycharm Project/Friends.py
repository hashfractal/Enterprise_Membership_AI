def solution(m:int, n:int, board:[str]):
    lists = []
    for i in board:
        lists.append(list(i))
    count = 0
    while True:
        for y in range(m):
            for x in range(n):
                print(lists[y][x],end=" ")
            print()
        print("\n\n")
        change = 0

        for y in range(m - 1):
            for x in range(n - 1):
                if lists[y][x] == lists[y + 1][x] == lists[y][x + 1] == lists[y + 1][x + 1] and lists[y][x] != "_":
                    lists[y][x] = lists[y + 1][x] = lists[y][x + 1] = lists[y + 1][x + 1] = "_"

        for y in range(m):
            for x in range(n):
                print(lists[y][x],end=" ")
            print()
        print("\n\n")
        change = 0
        for y in range(1, m):
            for x in range(n):
                if lists[y][x] == "_" and lists[y - 1][x] != "_":
                    lists[y][x] = lists[y - 1][x]
                    lists[y - 1][x] = "_"
                    change += 1

        for y in range(m):
            for x in range(n):
                print(lists[y][x],end=" ")
            print()
        print("\n\n")

        if change == 0:
            for y in range(m):
                for x in range(n):
                    if lists[y][x] == "_":
                        count += 1
            break
    return count

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
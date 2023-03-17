year = int(input("year: "))

if year != 1955:
    kor = input("korean?(y/n): ").lower()[0]
else:
     kor = "n"

if year <= 1924:
    print("Greate")
elif year <= 1945 and kor == "n":
    print("Slient")
elif year <= 1954 and kor == "y":
    print("Slient")
elif year <= 1963 and kor == "y":
    print("Baby")
elif year <= 1964 and kor == "n":
    print("Baby")
elif year <= 1980:
    print("X")
elif year<= 1996:
    print("M")
else:
    print("Z")
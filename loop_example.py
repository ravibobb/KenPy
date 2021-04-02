s = 0
ef = input("How long: ")
e = int(ef)
while s < e:
    num = int(input("Enter number: "))
    if (num % 2) == 0:
        print("Even")
    else:
        print("ODD")

    s = s + 1
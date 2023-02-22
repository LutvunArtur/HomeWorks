def summa(a, b):
    return a + b


def minus(a, b):
    return a - b


def dil(a, b):
    return a / b


def mn(a, b):
    return a * b


res = 0
again = 0
while again == 0:
    try:
        num_1 = float(input("Enter first num :"))
        num_2 = float(input("Enter second num:"))
        func = int(input("What opperation do u want to do ? \n 1 '+' \n 2 '-' \n 3 '*' \n 4 '/' \n Your Answer:"))
        if func == 1:
            res = summa(num_1, num_2)
        elif func == 2:
            res = minus(num_1, num_2)
        elif func == 3:
            res = mn(num_1, num_2)
        elif func == 4:
            res = dil(num_1, num_2)
        else:
            print("Please enter only the numbers shown")
            continue
        print("Reasult = ", res)
    except (ValueError, ZeroDivisionError):
        print("Sorry invalid request, please try again :<")
        continue

    reapeat = int(input("if you want to do another op \n 1 yea \n 2 no \n print here:"))
    try:
        if reapeat == 1:
            continue
        elif reapeat == 2:
            print("Okey, have a good day, bye !!!")
            break
        else:
            print("Enter only shown nums3.3")
            reapeat = False
            while reapeat:
                reapeat = int(input("if you want to do another op \n 1 yea \n 2 no \n print here:"))
                if reapeat == 1:
                    continue
                elif reapeat == 2:
                    print("Okey, have a good day, bye !!!")
            break
    except(ValueError):
        print("Please enter shown requests")
    continue
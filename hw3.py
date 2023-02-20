def summa(a, b):
    return a + b

def minus(a, b):
    return a - b


def dil(a, b):
    return a / b


def mn(a, b):
    return a * b


try:
    num_1 = float(input("Enter first num :"))
    num_2 = float(input("Enter second num:"))
    func = int(input("What opperation do u want to do ? \n 1 '+' \n 2 '-' \n 3 '*' \n 4 '/' \n Your Answer:"))
    if func == 1:
        res = summa(num_1, num_2)
    if func == 2:
        res = minus(num_1, num_2)
    if func == 3:
        res = mn(num_1, num_2)
    if func == 4:
        res = dil(num_1, num_2)
    print("Reasult = ", res)
except (ValueError, ZeroDivisionError, NameError):
    print("Sorry invalid request, please try again :<")

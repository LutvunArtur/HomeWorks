def summa(a, b):
    r = a + b
    print("Reasult=", r)
def min(a, b) :
    r = a - b
    print("Reasult=", r)
def dil(a, b) :
    r = a / b
    print("Reasult=", r)
def mn(a, b) :
    r = a * b
    print("Reasult=", r)
try :
    num_1 = float(input("Enter first num :"))
    num_2 = float(input("Enter second num:"))
    func = int(input("What opperation do u want to do ? \n 1 '+' \n 2 '-' \n 3 '*' \n 4 '/' \n Your Answer"))
    print("Sorry invalid request, please try again :<")
    if func == 1:
        summa(num_1, num_2)
    if func == 2:
        min(num_1, num_2)
    if func == 3:
        mn(num_1, num_2)
    if func == 4:
        dil(num_1, num_2)
except ValueError:
    print("Sorry invalid request, please try again :<")

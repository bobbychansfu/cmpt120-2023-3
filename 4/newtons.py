a = float(input("a: "))
x = float(input("x: "))

while(True):
    # print(x)
    y = (x + (a/x)) / 2     # new guess
    if (abs(x-y) < 0.0000001):
        break
    x = y

print(round(x,7))

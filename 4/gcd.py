a = int(input("a: "))
b = int(input("b: "))

r = a % b

while (r != 0):
    a = b
    b = r
    r = a % b

print("gcd:",b)


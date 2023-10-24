'''
  collect 2 integers a,b a>b
  from the user and prints all
  square roots from a down to b
'''

import math

# collect user inputs
print("enter range [b,a]")
a = int(input("a: "))
b = int(input("b: "))

# check if a > b
if (a < b): 
    a,b = b,a   # swap a,b

print("printing sqrts from",b,"to",a)

# print all sqrts from a down to b

for num in range(a,b-1,-1): # [a,a-1,a-2, .... b]
    print("the sqrt of",num,"is",round(math.sqrt(num),3))

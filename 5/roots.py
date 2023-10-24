'''
  write a function called roots(a,b,c)
  gives the roots for ax^2 + bx + c
'''

import math

def roots(a,b,c):
    dis = b**2 - 4*a*c

    if (dis >= 0):
        # are roots
        root1 = (-b + math.sqrt(dis))/(2*a)
        root2 = (-b - math.sqrt(dis))/(2*a)
        return (root1,root2)
    else:
        return None
    

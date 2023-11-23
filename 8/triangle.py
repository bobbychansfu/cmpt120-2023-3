def triangle(n):
    '''
    nth triangle number =
    n + (n-1) + (n-2) ... + 1
    '''
    if n < 1:
        return 0
    else:
        return triangle(n-1) + n

def power(a,n):
    '''
    compute a^n
    a = integer
    n = non-negative integer
    '''
    if n==0:
        return 1
    else:
        return power(a,n-1) * a

def reverse(st):
    if len(st)==0 or len(st)==1:
        return st
    else:
        rev_tail = reverse(st[1:])
        return rev_tail + st[0]


    

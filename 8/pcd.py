def common_divisor(n,m,g):
    if n%g==0 and m%g==0:
        return g
    else:
        return common_divisor(n,m,g-1)

def gcd(n,m):
    return common_divisor(n,m,min(n,m))

def mutually_prime(n,m):
    return common_divisor(n,m,min(n,m)) == 1

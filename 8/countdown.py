import time

def countdown(n):
    if(n==0):
        return
    else:
        print(n)
        time.sleep(1)
        countdown(n-1)
        print(n)

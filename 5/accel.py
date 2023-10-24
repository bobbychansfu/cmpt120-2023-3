GRAVITY_ACCEL = 9.81 # m/s^2

def getInputs():
    print("this program claculates velocity after n secs")
    n = float(input("input n: "))
    return n

def calcVeloc(n):
    global GRAVITY_ACCEL
    velocity = GRAVITY_ACCEL * n
    print("velocity after",n,"seconds is",velocity)
    return

def main():
    n = getInputs()
    calcVeloc(n)
    return

main()



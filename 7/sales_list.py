NUM_DAYS = 5
WEEK = ["Mon","Tues","Wed","Thur","Fri"]

def main():
    sales = [0]*NUM_DAYS
    i = 0
    for w in WEEK:
        sales[i] = float(input("Sales on " + w + ":"))
        i += 1

    print(*sales)

main()

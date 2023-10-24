def change():
    global number
    number = 10
    print(number)
    return

def main():
    change()
    print(number)
    return

number = 5
main()

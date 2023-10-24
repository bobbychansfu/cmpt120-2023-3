inp = input("enter next number (enter 'exit' to quit): ")

if inp.isdigit():
    inp = int(inp)
    minimum = inp
    maximum = inp

    while (inp != 'exit'):
        number = int(inp)
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
        inp = input("enter next number (enter 'exit' to quit): ")

    print("max:",maximum,"min:",minimum)

    # ToDo: make the user keep entering values until valid integer obtained

def main():
    names_list = []
    again = 'y'

    while(again.lower() == 'y'):
        name = input("enter friend: ")
        names_list.append(name)
        again = input("Another friend (y/n)? ")

    print("Names:")
    print(*names_list,sep="\n")

main()

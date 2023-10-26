friends_list = []

while True:
    print("your friends",end=" ")
    print(*friends_list)
    f = input("enter a new friend: ")
    friends_list.append(f)
    again = input("another friend (y/n)? ")
    if (again == 'n'):
        break

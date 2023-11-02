def main():
    food_list = ['pizza','burger','fries']
    print(*food_list,sep='\t')

    try:
        item = input("what do you want to change? ")
        item_index = food_list.index(item)
        new_item = input("what's the new food? ")
        food_list[item_index] = new_item
        print(*food_list,sep='\t')
    except ValueError:
        print("Error, cannot find food")

main()

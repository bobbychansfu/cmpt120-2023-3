##def total_function(value_list):
##    total = 0
##    for n in value_list:
##        total += n
##    return total
##
##def main():
##    numbers = [50,2,88,72,4]
##    print("Total", total_function(numbers))
##    print(numbers)
##main()

def alter(value_list):
    for i in range(len(value_list)):
        value_list[i] *= 2
        
def main():
    numbers = [50,2,88,72,4]
    print(numbers)
    alter(numbers[:])
    print(numbers)
main()

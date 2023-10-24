'''
 add all integers entered by the user
 until a negative number appears
 print total
'''

total = 0

while (True):
    num = int(input("plz enter num: "))

    # check num for neg
    if (num < 0):
        break
        
    total = total + num


print("total:",total)
              

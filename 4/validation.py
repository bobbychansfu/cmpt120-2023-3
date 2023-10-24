'''
 validate the user input to be between
 1 and 3
'''

inp = int(input("enter 1, 2, or 3: "))

while (inp < 1 or inp > 3):
    inp = int(input("enter 1, 2, or 3: "))

## process it

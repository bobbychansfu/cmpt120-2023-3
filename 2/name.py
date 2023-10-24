'''
 takes user's full name via input
 and prints out their first and last names
 i.e. if 'Bobby Chan' is entered, print
 > First name: Bobby
 > Last name: Chan
 Assumptions:
 last space indicates the separation
'''

# collect inputs
fullname = input("Enter full name: ")   # inline

# find the index of the space
sp_index = fullname.rfind(" ")

# split the first name and last name
first_name = fullname[:sp_index]
last_name = fullname[sp_index+1:]

# print onto terminal
print("First name" + first_name)
print("Last name " + last_name)

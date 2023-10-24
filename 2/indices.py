myString = "Jessica Johnson"

# print(myString[10])
# print(myString[3:7]) # [pos1:pos2]
# print(myString[-1])
# print(myString[:7])

sp_index = myString.find(" ")

first_name = myString[:sp_index]
last_name = myString[sp_index+1:]

first_name = first_name.upper()
length = len(first_name) # length of first name

print(first_name)
print(length)
print(last_name)


my_dictionary = { 3:'hello', 'hello':5, 32.1:(99,100) }

phonebook = { 'Chris':'5551111','Bob':'5551234','Mary':'5559999' }

if 'Chris' in phonebook:
    c = phonebook['Chris']

# adding new value
phonebook['Joe'] = '5550123'

# alter value
phonebook['Chris'] = '5554444'

# for loops
##for key in phonebook:
##    print(key, phonebook[key])
##
##print()
##
##for key in phonebook.keys():
##    print(key)

(key,value) = phonebook.popitem()
print(key,value)

# items

for (k,v) in phonebook.items(): # a list of all key/value pairs
                                # [ ('Chris':'5554444'),(),()... ]
    print(k,v)



    

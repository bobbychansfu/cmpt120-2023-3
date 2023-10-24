# ask questions

eat = input("Did you eat? ")
study = input("Did you study? ")
lan = input("Did you do your laundry? ")
gran = input("Did you call grandma? ")

# count the yes

count = 0

if (eat.rstrip().lower() == "yes"):
    count = count + 1

if (study.rstrip().lower() == "yes"):
    count = count + 1

if (lan.rstrip().lower() == "yes"):
    count = count + 1

if (gran.rstrip().lower() == "yes"):
    count = count + 1

# check for count number then output feedback

if (count == 0):
    print("We need to talk.")
elif (count >= 1 and count <= 2):
    print("Ok.")
else:           # count = 3-4
    print("Good!")
    
    

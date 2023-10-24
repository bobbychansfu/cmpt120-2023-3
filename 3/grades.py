'''
 display student's lettergrade
 based on percentage
 >85 A
 >75 B
 >65 C
 >55 D
 <= 55 F
'''

percent = float(input("enter percent: "))

lettergrade = ""

# solution 2

if (percent <= 55):
    lettergrade = "F"
else:
    if (percent <= 65):
        lettergrade = "D"
    else:
        if (percent <= 75):
            lettergrade = "C"
        else:
            if (percent <= 85):
                lettergrade = "B"
            else:
                lettergrade = "A"

print(lettergrade)

'''
# solution 1
if (percent > 85):
    lettergrade = "A"
elif (percent > 75): # percent <= 85
    lettergrade = "B"
elif (percent > 65):
    lettergrade = "C"
elif (percent > 55):
    lettergrade = "D"
else:               # percent <= 55
    lettergrade = "F"

print(lettergrade)
'''
    

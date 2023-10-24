'''
 ask user for input n then
 reads n integers, adding ONLY the positive
 ones
 Then prints the sum of the positives
'''

n = int(input("enter n: "))

positive_sum = 0
count = 1

while (count <= n):
    count = count + 1
    x = int(input("enter next num: "))
    # compare of x < 0
    if (x < 0):
        continue

    positive_sum = positive_sum + x

print("sum:",positive_sum)

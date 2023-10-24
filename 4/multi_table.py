'''
  print out a multiplication table
  a x b, where a = rows, b = columns
  i.e.
  a = 4
  b = 5

  1  2  3  4  5
  2  4  6  8  10
  3  6  9  12 15
  4  8  12 16 20
'''

a = int(input("a: "))
b = int(input("b: "))

# loop for rows
for r in range(1,a+1):
    # loop for columns
    for c in range(1,b+1):
        print(r*c, end="\t")
    print() # end the line

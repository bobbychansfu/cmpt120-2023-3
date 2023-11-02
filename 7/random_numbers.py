import random

ROWS = 3
COLUMNS = 4

def main():
    temp_row = [0] * COLUMNS    # [0,0,0,0]
    temp_row1 = temp_row[:]     # [0,0,0,0]
    temp_row2 = temp_row[:]     # [0,0,0,0]

    values = [temp_row,temp_row1,temp_row2]

    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(1,100)

    print(*values,sep='\n')
    # write a nested for loop to print all values

main()

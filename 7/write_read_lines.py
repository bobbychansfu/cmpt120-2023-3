def write_lines():
    foods = ['pizza\n','burger\n','fries\n']
    outfile = open("foods.txt","w")
    outfile.writelines(foods)
    outfile.close()

def read_lines():
    infile = open("foods.txt","r")
    content_list = infile.readlines()
    infile.close()
    return content_list

def main():
    write_lines()
    foods_list = read_lines()
    print(*foods_list, sep='')

main()

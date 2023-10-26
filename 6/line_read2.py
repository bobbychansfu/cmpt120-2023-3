def main():
    # open file
    infile = open('friends.txt','r')
    
    # process
    for line in infile:
        print(line.rstrip('\n'))

    # close file
    infile.close()

main()

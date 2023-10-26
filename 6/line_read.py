def main():
    # open file
    infile = open('friends.txt','r')
    
    # process
    f1 = infile.readline().rstrip('\n')
    f2 = infile.readline().rstrip('\n')
    f3 = infile.readline().rstrip('\n')
    print(f1)
    print(f2)
    print(f3)

    # close file
    infile.close()

main()

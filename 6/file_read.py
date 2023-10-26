def main():
    # open file
    infile = open('friends.txt','r')
    
    # process
    file_contents = infile.read()
    print(file_contents)

    # close file
    infile.close()

main()

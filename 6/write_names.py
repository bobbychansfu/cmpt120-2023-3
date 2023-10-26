def main():
    # open file
    outfile = open('friends.txt','a')
    
    # process
    fname = 'tmp'
    while(fname != ''):
        fname = input("next friend: ")
        if (fname != ''):
            outfile.write(fname + '\n')

    # close file
    outfile.close()

main()

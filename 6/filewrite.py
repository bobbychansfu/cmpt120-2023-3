def main():
    # open file
    outfile = open('friends.txt','w')
    
    # process
    outfile.write('Jason\n')
    outfile.write('Mary\n')
    outfile.write('Steve\n')

    # close file
    outfile.close()

main()

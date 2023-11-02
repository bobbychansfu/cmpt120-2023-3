'''
1. open a filename from user for reading
2. readline two times, converting each line
   to integer
3. output first_line_num / second_line_num
'''

def main():
    try:
        infile_name = input("Enter file name: ")
        infile = open(infile_name,'r')

        c1 = int(infile.readline().rstrip('\n'))
        c2 = int(infile.readline().rstrip('\n'))

        print(c1/c2)
    except ZeroDivisionError as err_msg:
        print(err_msg)
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("can't convert to int")
    except:
        print("Oops! General error!")
main()

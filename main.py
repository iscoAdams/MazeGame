import sys
import os

if not '__main__':
    pass
else:
    try:
        # if ONLINE_JUDGE:
        #     input = sys.stdin.readline
        #     output = sys.stdout.write
        # else:
        #     input = open(os.path.join(os.path.dirname(__file__), 'in.txt')).readline
        read_file   =    open("IO/in.txt", "r")
        write_file  =    open("IO/out.txt", "w") # write_file = sys.stdout  # write_file = sys.stderr


        # for line in read_file:
        #     listItems = line.split(",(")
        # print(str(listItems[::-1]), file=write_file)    
            
        # write_file.write() 
        read_file.close()
        write_file.close()
    except Exception as e:
        print(e)
        sys.exit(1)
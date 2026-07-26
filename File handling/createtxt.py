#creating text file

import sys

try:
    f=open("createtxt.txt",'w')
    f.write("Python\t")
    f.write("3.345\t")
    f.write('''\nPython 3.12 is a  a
            programming 
            language''')
    print("Data is written inside file")
    
except:
    e=sys.exc_info() 
    print(e[0])
finally:
    f.close()       